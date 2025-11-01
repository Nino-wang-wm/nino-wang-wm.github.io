---
title: 'Project and Code'
date: 2024-10-10
type: landing

design:
  spacing: '6rem'
  css_style: 'max-width: 1400px; margin: 0 auto; padding: 3rem 2rem;'

sections:
  - block: markdown
    content:
      # title: 'Research Projects and Code Repository'
      subtitle: 'Advanced Optimization Methods and Machine Learning Applications'
      text: |-
        <div style="max-width: 1400px; margin: 0 auto; padding-top: 1rem;">
        
        <p style="font-size: 1.05rem; line-height: 1.9; color: #e2e8f0; margin-bottom: 4rem; text-align: justify;">
          This project contains implementations and analyses of advanced optimization algorithms, 
          including decomposition techniques for large-scale linear programs and nonlinear optimization 
          methods applied to machine learning problems. Each project includes theoretical foundations, 
          computational implementations, and empirical evaluations.
        </p>
        
        <div class="project-grid" style="display: grid; grid-template-columns: 1fr; gap: 2.5rem; margin-top: 3rem;">
        
        <!-- Project 1: Decomposition Techniques -->
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); transition: all 0.3s ease; border-left: 4px solid #4a5568; display: flex; align-items: center; gap: 3rem;">
          <div style="flex: 1;">
            <h3 style="font-size: 1.75rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff; letter-spacing: -0.02em;">
              Decomposition Techniques in Optimization
            </h3>
            <p style="line-height: 1.85; margin: 0; color: #e2e8f0; font-size: 1rem;">
              Column generation and Benders decomposition methods for addressing large-scale optimization 
              problems with complicating constraints and variables. Implementations leverage commercial 
              solvers (Gurobi) with algorithmic enhancements for improved convergence properties.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; flex-shrink: 0;">
            <a href="decomposition-constraint/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              Constraint Decomposition
            </a>
            <a href="decomposition-variables/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              Variable Decomposition
            </a>
          </div>
        </div>
        
        <!-- Project 2: Advanced Non-linear Optimization -->
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); transition: all 0.3s ease; border-left: 4px solid #2d3748; display: flex; align-items: center; gap: 3rem;">
          <div style="flex: 1;">
            <h3 style="font-size: 1.75rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff; letter-spacing: -0.02em;">
              Advanced Non-linear Optimization in Machine Learning
            </h3>
            <p style="line-height: 1.85; margin: 0; color: #e2e8f0; font-size: 1rem;">
              Computational methods for solving nonlinear optimization problems arising in machine learning 
              applications. This project includes gradient-based algorithms, convergence analysis, and 
              numerical experiments with real-world datasets.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; flex-shrink: 0;">
            <a href="advanced-nonlinear-optimization/homework1/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              Example 1
            </a>
            <a href="advanced-nonlinear-optimization/homework2/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              Example 2
            </a>
          </div>
        </div>
        
        <!-- Project 3: Linear Algebra in Optimization -->
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); transition: all 0.3s ease; border-left: 4px solid #48bb78; display: flex; align-items: center; gap: 3rem;">
          <div style="flex: 1;">
            <h3 style="font-size: 1.75rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff; letter-spacing: -0.02em;">
              Linear Algebra in Optimization
            </h3>
            <p style="line-height: 1.85; margin: 0; color: #e2e8f0; font-size: 1rem;">
              Essential linear algebra concepts that form the mathematical foundation for optimization theory 
              and algorithms. Covers matrix operations, eigenvalue decomposition, SVD, and their applications 
              in solving linear and nonlinear optimization problems.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; flex-shrink: 0;">
            <a href="linear-algebra-optimization/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              View Materials
            </a>
          </div>
        </div>
        
        <!-- Project 4: Larson Hypercube Replication -->
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); transition: all 0.3s ease; border-left: 4px solid #667eea; display: flex; align-items: center; gap: 3rem;">
          <div style="flex: 1;">
            <h3 style="font-size: 1.75rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff; letter-spacing: -0.02em;">
              Larson Hypercube Queuing Model Replication
            </h3>
            <p style="line-height: 1.85; margin: 0; color: #e2e8f0; font-size: 1rem;">
              Implementation of Larson's 1974 hypercube queuing model for facility location and redistricting 
              in urban emergency services. Features dual model implementation, performance analytics, and 
              comprehensive visualization tools.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; flex-shrink: 0;">
            <a href="larson-hypercube-replication/" style="display: inline-block; padding: 0.75rem 1.75rem; background: transparent; color: #e2e8f0; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #718096; white-space: nowrap; text-align: center;">
              View Project
            </a>
          </div>
        </div>
        
        </div>
        
        <style>
          @media (max-width: 768px) {
            .project-grid {
              grid-template-columns: 1fr !important;
            }
            .project-grid > div {
              flex-direction: column !important;
              align-items: flex-start !important;
            }
            .project-grid > div > div:last-child {
              margin-top: 1.5rem;
              width: 100%;
            }
            .project-grid > div > div:last-child a {
              width: 100%;
            }
          }
          a[href*="decomposition-constraint"],
          a[href*="decomposition-variables"],
          a[href*="advanced-nonlinear-optimization"],
          a[href*="linear-algebra-optimization"],
          a[href*="larson-hypercube-replication"] {
            cursor: pointer;
          }
          a[href*="decomposition-constraint"]:hover,
          a[href*="decomposition-variables"]:hover,
          a[href*="advanced-nonlinear-optimization"]:hover,
          a[href*="linear-algebra-optimization"]:hover,
          a[href*="larson-hypercube-replication"]:hover {
            background: #4a5568 !important;
            border-color: #a0aec0 !important;
            color: #ffffff !important;
          }
        </style>
        
        </div>
    design:
      columns: '1'
---

