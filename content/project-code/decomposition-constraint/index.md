---
title: 'Decomposition-complicated constraint'
date: 2024-10-10
type: landing

design:
  spacing: '4rem'
  css_style: 'max-width: 1200px; margin: 0 auto; padding: 2rem 1rem;'

sections:
  - block: markdown
    content:
      text: |-
        <div style="max-width: 1200px; margin: 0 auto;">
        
        <h1 style="font-size: 2.5rem; font-weight: 700; color: #ffffff; margin: 0 0 0.5rem 0; letter-spacing: -0.02em;">
          Column Generation for Optimization Problems with Complicating Constraints
        </h1>
        <h2 style="font-size: 1.25rem; font-weight: 500; color: #cbd5e0; margin: 0 0 3rem 0; font-style: italic;">
          Decomposition-complicated Constraint
        </h2>
        
        <div style="border-left: 4px solid #667eea; padding-left: 2rem; margin-bottom: 3rem;">
          <p style="font-size: 1.05rem; line-height: 1.9; color: #e2e8f0; margin: 0; text-align: justify;">
            This project presents an implementation of column generation algorithms for solving linear 
            programming problems with complicating constraints. The approach decomposes the original problem 
            into block-structured subproblems and employs an iterative column generation scheme to converge 
            to the optimal solution. The master problem is formulated with penalty variables to ensure 
            feasibility throughout the optimization process.
          </p>
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 3rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Theoretical Documentation</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin: 2rem 0;">
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3); transition: all 0.2s ease;">
          <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Constraint-Based Decomposition Methods
          </h3>
          <p style="color: #e2e8f0; margin: 0 0 1.25rem 0; line-height: 1.7; font-size: 0.95rem;">
            Comprehensive documentation detailing the theoretical foundations of constraint-based decomposition 
            methods, including problem formulation, duality theory, and convergence analysis.
          </p>
          <a href="/data/project/cvlplp1.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #90cdf4; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s ease;">
            Access PDF Document <span style="margin-left: 0.5rem; font-size: 1rem;">→</span>
          </a>
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3); transition: all 0.2s ease;">
          <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Advanced Decomposition Techniques
          </h3>
          <p style="color: #e2e8f0; margin: 0 0 1.25rem 0; line-height: 1.7; font-size: 0.95rem;">
            Extended documentation covering advanced decomposition techniques, implementation strategies, 
            and computational case studies with numerical results.
          </p>
          <a href="/data/project/cvlplp2.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #90cdf4; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s ease;">
            Access PDF Document <span style="margin-left: 0.5rem; font-size: 1rem;">→</span>
          </a>
        </div>
        
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 4rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Computational Implementation</h2>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2.5rem; margin: 2rem 0;">
        
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.35rem; font-weight: 700; margin: 0 0 0.5rem 0; color: #ffffff;">
            Column Generation for "LP with Complicating Constraints"
          </h3>
          <p style="color: #cbd5e0; margin: 0; font-size: 0.95rem;">
            Python implementation using Gurobi Optimizer (Version 10.0+)
          </p>
        </div>
        
        <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 2rem; font-size: 1rem;">
          Complete implementation of the column generation algorithm for linear programs with complicating 
          constraints. The codebase includes problem initialization, master problem formulation with penalty 
          variables, subproblem solvers for block-structured components, and an iterative column generation 
          loop with convergence criteria.
        </p>
        
        <div style="background: #2d3748; border: 1px solid #4a5568; border-radius: 6px; padding: 1.75rem; margin: 1.5rem 0;">
          <h4 style="color: #ffffff; font-weight: 600; margin: 0 0 1rem 0; font-size: 1.1rem;">Algorithm Components</h4>
          <ul style="color: #e2e8f0; line-height: 1.9; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;">
            <li><strong style="color: #90cdf4;">Block solver</strong>: Solves subproblems for each block with modified cost coefficients</li>
            <li><strong style="color: #90cdf4;">Master problem solver</strong>: Always-feasible formulation with penalty variables (big-M method)</li>
            <li><strong style="color: #90cdf4;">Column generation loop</strong>: Iterative algorithm with dual information and convergence checking</li>
            <li><strong style="color: #90cdf4;">Full LP solver</strong>: Baseline direct solve for validation and comparison</li>
          </ul>
        </div>
        
        <a href="/data/project/cvlplp3.py" download style="display: inline-flex; align-items: center; background: #667eea; color: white; padding: 0.875rem 2rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: background 0.2s ease; box-shadow: 0 2px 8px rgba(102, 126, 234, 0.25);">
          Download Source Code
        </a>
        
        </div>
        
        </div>
    design:
      columns: '1'
---
