import sys
import math
import arrow
import numpy as np
from collections import defaultdict

class HypercubeQ:
    """
    Hypercube Queueing Model with Zero-line or Infinite-line Capacity.
    
    Simplified implementation with two main assumptions:
    1. eta_{ij} = 1: Only one optimal unit for each dispatch
    2. t_{ij} = tau_{ij}: Units are always in home atom when available
    
    Reference:
    Larson, R. C. (1974). A hypercube queuing model for facility location and 
    redistricting in urban emergency services. Computers & Operations Research.
    """

    def __init__(self, n_atoms, Lam=None, T=None, P=None, cap="zero", max_iter=10, q_len=100):
        """
        Initialize Hypercube Queuing Model.
        
        Args:
            n_atoms (int): Number of geographical atoms (= number of response units)
            Lam (array): Arrival rates vector for each atom
            T (array): Traffic time matrix from atom i to atom j
            P (array): Dispatch policy matrix
            cap (str): Capacity type - 'zero' or 'inf'
            max_iter (int): Maximum iterations for convergence
            q_len (int): Queue length for infinite capacity case
        """
        # Model configuration
        self.cap = cap
        self.n_atoms = n_atoms
        
        # Initialize arrival rates (with normalization)
        self.Lam = np.array(Lam, dtype=float) if Lam is not None else np.random.rand(self.n_atoms)
        self.Lam = self.Lam / self.Lam.sum()
        
        # Initialize traffic and preference matrices
        self.T = np.array(T, dtype=float) if T is not None else np.random.rand(self.n_atoms, self.n_atoms)
        self.P = np.array(P, dtype=int) if P is not None else np.random.rand(self.n_atoms, self.n_atoms).argsort()

        # Validate parameter dimensions
        self._validate_parameters()

        # Initialize model state
        print(f"[{arrow.now()}] Initializing model state...", file=sys.stderr)
        self.S = self._generate_tour()
        self.all_busy_state_idx = np.array([self.S[i].sum() for i in range(2 ** self.n_atoms)]).argmax()
        self.all_zero_state_idx = 0

        # Calculate transition rates
        print(f"[{arrow.now()}] Calculating transition rates...", file=sys.stderr)
        self.Lam_ij = self._calculate_upward_transitions()

        # Calculate steady-state probabilities
        print(f"[{arrow.now()}] Computing steady-state probabilities...", file=sys.stderr)
        self.Pi = self._compute_steady_state_probs(cap=self.cap, max_iter=max_iter)

        # Handle infinite capacity case
        if self.cap == "inf":
            self.Pi_Q = np.array([self._queue_state_prob(j) for j in range(1, q_len)])
            self.Pi_Q_prime = self.Pi_Q.sum() + self.Pi[self.all_busy_state_idx]
        else:
            self.Pi_Q = []
            self.Pi_Q_prime = 0

        # Calculate performance metrics
        print(f"[{arrow.now()}] Computing performance metrics...", file=sys.stderr)
        self.Rho_1, self.Rho_2 = self._compute_dispatch_fractions(cap=self.cap)
        self.Tu = self._compute_travel_times(cap=self.cap)

    def _validate_parameters(self):
        """Validate input parameter dimensions."""
        assert self.n_atoms == self.Lam.shape[0] == self.T.shape[0] == \
               self.T.shape[1] == self.P.shape[0] == self.P.shape[1], \
               "Invalid parameter dimensions"

    def _generate_tour(self):
        """Generate complete unit-step tour of hypercube."""
        # Initialize tour array
        S = np.zeros((2 ** self.n_atoms, self.n_atoms))
        S[1, 0] = 1
        m, i = 2, 2

        # Generate tour sequence
        for n in range(1, self.n_atoms):
            S[i:i+m, n] = 1
            S[i:i+m, :n] = np.flip(S[int(i-m):i, :n], axis=0)
            i += m
            m *= 2
        return S

    def _calculate_upward_transitions(self):
        """Calculate upward transition rates."""
        Upoptn = self._find_optimal_neighbors()
        Lam_ij = defaultdict(lambda: 0)

        for k in range(self.n_atoms):
            for i in range(2 ** self.n_atoms):
                if self.S[i].sum() < self.n_atoms:
                    Lam_ij[(i, Upoptn[k, i])] += self.Lam[k]
        return Lam_ij

    def _find_optimal_neighbors(self):
        """Find optimal upward neighbors for each state."""
        def get_state_index(state):
            """Find index of a given state."""
            for i in range(2 ** self.n_atoms):
                if np.count_nonzero(state - self.S[i]) == 0:
                    return i

        # Initialize optimal neighbors matrix
        Upopts = np.zeros((self.n_atoms, 2 ** self.n_atoms), dtype=int)
        
        # Find optimal neighbors for each state and atom
        for k in range(self.n_atoms):
            for i in range(2 ** self.n_atoms):
                idle_units = np.where(self.S[i] == 0)[0]
                if len(idle_units) > 0:
                    disp_units = self.P[k]
                    for unit in disp_units:
                        if unit in idle_units:
                            new_state = np.zeros(self.n_atoms, dtype=int)
                            new_state[unit] = 1
                            upward_state = self.S[i] + new_state
                            Upopts[k, i] = get_state_index(upward_state)
                            break
                else:
                    Upopts[k, i] = -1
        return Upopts

    def _compute_steady_state_probs(self, cap, max_iter):
        """Compute steady-state probabilities."""
        Pi = self._initialize_probabilities(cap)
        
        for _ in range(max_iter):
            Pi = self._update_probabilities(Pi)
        return Pi

    def _initialize_probabilities(self, cap):
        """Initialize probability distribution."""
        Pi_0 = np.zeros(2 ** self.n_atoms)
        
        for n_busy in range(self.n_atoms + 1):
            # Calculate denominator based on capacity type
            if cap == "zero":
                denominator = sum([
                    self.Lam.sum() ** j / math.factorial(j)
                    for j in range(self.n_atoms + 1)
                ])
            else:
                denominator = sum([
                    self.Lam.sum() ** j / math.factorial(j)
                    for j in range(self.n_atoms + 1)
                ]) + (self.Lam.sum() ** self.n_atoms / math.factorial(self.n_atoms)) * \
                    (self.Lam.sum() / self.n_atoms / (1 - self.Lam.sum() / self.n_atoms))

            # Calculate initial probabilities
            n_states = sum(1 for i in range(2 ** self.n_atoms) if self.S[i].sum() == n_busy)
            init_prob = (self.Lam.sum() ** n_busy / math.factorial(n_busy)) / denominator / n_states
            
            # Assign probabilities to states
            for i in range(2 ** self.n_atoms):
                if self.S[i].sum() == n_busy:
                    Pi_0[i] = init_prob
        return Pi_0

    def _update_probabilities(self, Pi_n):
        """Update probability distribution for one iteration."""
        Pi_next = np.copy(Pi_n)
        
        for j in range(2 ** self.n_atoms):
            if self.S[j].sum() != 0 and self.S[j].sum() != self.n_atoms:
                upward_sum = downward_sum = 0
                
                for i in range(2 ** self.n_atoms):
                    changed_units = np.nonzero(self.S[j] - self.S[i])[0]
                    
                    if len(changed_units) == 1:
                        if (self.S[j] - self.S[i]).sum() == 1:
                            upward_sum += Pi_n[i] * self.Lam_ij[(i, j)]
                        elif (self.S[j] - self.S[i]).sum() == -1:
                            downward_sum += Pi_n[i]
                
                Pi_next[j] = (upward_sum + downward_sum) / (self.Lam.sum() + self.S[j].sum())
        return Pi_next

    def _queue_state_prob(self, n_waiting):
        """Calculate probability of n customers waiting in queue."""
        assert n_waiting >= 1, "n_waiting must be at least 1"
        
        denominator = sum([
            self.Lam.sum() ** j / math.factorial(j)
            for j in range(self.n_atoms + 1)
        ]) + (self.Lam.sum() ** self.n_atoms / math.factorial(self.n_atoms)) * \
            (self.Lam.sum() / self.n_atoms / (1 - self.Lam.sum() / self.n_atoms))
        
        return (self.Lam.sum() ** self.n_atoms / math.factorial(self.n_atoms)) * \
               (self.Lam.sum() / self.n_atoms) ** n_waiting / denominator

    def _compute_dispatch_fractions(self, cap):
        """Compute dispatch fractions for each unit-atom pair."""
        def find_optimal_dispatch_states(n, j):
            """Find states where unit n is optimal for atom j."""
            states = []
            for i in range(2 ** self.n_atoms):
                disp_units = self.P[j]
                idle_units = np.where(self.S[i] == 0)[0]
                if n in idle_units:
                    n_priority = disp_units.tolist().index(n)
                    other_priorities = [
                        disp_units.tolist().index(u)
                        for u in idle_units if u != n
                    ]
                    if len(other_priorities) == 0 or n_priority <= min(other_priorities):
                        states.append(i)
            return states

        # Calculate dispatch fractions
        E_nj = {}
        for n in range(self.n_atoms):
            for j in range(self.n_atoms):
                E_nj[(n, j)] = find_optimal_dispatch_states(n, j)

        # Initialize result matrices
        Rho_1 = np.zeros((self.n_atoms, self.n_atoms), dtype=float)
        Rho_2 = np.zeros((self.n_atoms, self.n_atoms), dtype=float)

        # Fill matrices based on capacity type
        for n in range(self.n_atoms):
            for j in range(self.n_atoms):
                if cap == "zero":
                    denominator = self.Lam.sum() * (1 - self.Pi[self.all_busy_state_idx])
                    numerator = sum(self.Lam[j] * self.Pi[i] for i in E_nj[(n, j)])
                    Rho_1[n, j] = numerator / denominator
                else:
                    Rho_2[n, j] = self.Lam[j] / self.Lam.sum() * self.Pi_Q_prime / self.n_atoms
                    Rho_1[n, j] = sum(self.Lam[j] / self.Lam.sum() * self.Pi[i] 
                                    for i in E_nj[(n, j)])

        return Rho_1, Rho_2

    def _compute_travel_times(self, cap):
        """Compute average travel times for each unit."""
        Tu = np.zeros(self.n_atoms)
        f = self.Lam / self.Lam.sum()
        T_Q = np.matmul(f, np.matmul(self.T, f))

        for n in range(self.n_atoms):
            if cap == "zero":
                numerator = (self.T[n, :] * self.Rho_1[n, :]).sum()
                denominator = self.Rho_1[n, :].sum()
            else:
                numerator = (self.T[n, :] * self.Rho_1[n, :]).sum() + \
                           T_Q * self.Pi_Q_prime / self.n_atoms
                denominator = self.Rho_1[n, :].sum() + self.Pi_Q_prime / self.n_atoms
            
            Tu[n] = numerator / denominator
        return Tu