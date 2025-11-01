---
title: 'Decomposition-complicated Variables'
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
          Benders Decomposition for Optimization Problems with Complicating Variables
        </h1>
        <h2 style="font-size: 1.25rem; font-weight: 500; color: #cbd5e0; margin: 0 0 3rem 0; font-style: italic;">
          Decomposition-complicated Variables
        </h2>
        
        <div style="border-left: 4px solid #48bb78; padding-left: 2rem; margin-bottom: 3rem;">
          <p style="font-size: 1.05rem; line-height: 1.9; color: #e2e8f0; margin: 0; text-align: justify;">
            This project implements Benders decomposition, a classical decomposition method for mixed-integer 
            and linear programming problems with complicating variables. The algorithm separates the problem 
            into a master problem (containing complicating variables) and subproblems, iteratively generating 
            Benders cuts to approximate the value function. The implementation includes convergence analysis 
            and numerical validation against direct solution methods.
          </p>
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 3rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Theoretical Documentation</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin: 2rem 0;">
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3); transition: all 0.2s ease;">
          <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Calculation and Analysis Document
          </h3>
          <p style="color: #e2e8f0; margin: 0 0 1.25rem 0; line-height: 1.7; font-size: 0.95rem;">
            Detailed documentation covering the mathematical foundations of Benders decomposition, including 
            dual formulations, cut generation procedures, convergence proofs, and numerical examples with 
            computational results.
          </p>
          <a href="/data/calculation.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #90cdf4; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s ease;">
            Access PDF Document <span style="margin-left: 0.5rem; font-size: 1rem;">→</span>
          </a>
        </div>
        
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 4rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Computational Implementation</h2>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2.5rem; margin: 2rem 0;">
        
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.35rem; font-weight: 700; margin: 0 0 0.5rem 0; color: #ffffff;">
            Benders Decomposition for "LP with Complicating Variables"
          </h3>
          <p style="color: #cbd5e0; margin: 0; font-size: 0.95rem;">
            Python implementation using Gurobi Optimizer (Version 10.0+)
          </p>
        </div>
        
        <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 2rem; font-size: 1rem;">
          Complete implementation of the Benders decomposition algorithm for optimization problems with 
          complicating variables. The codebase provides a direct solve method for baseline comparison, 
          subproblem solvers that generate dual information, a master problem solver that accumulates 
          Benders cuts, and the main decomposition driver with iteration tracking and convergence monitoring.
        </p>
        
        <div style="background: #2d3748; border: 1px solid #4a5568; border-radius: 6px; padding: 1.75rem; margin: 1.5rem 0;">
          <h4 style="color: #ffffff; font-weight: 600; margin: 0 0 1rem 0; font-size: 1.1rem;">Algorithm Components</h4>
          <ul style="color: #e2e8f0; line-height: 1.9; margin: 0; padding-left: 1.5rem; font-size: 0.95rem;">
            <li><strong style="color: #90cdf4;">Direct solve method</strong>: Baseline solver for validation and performance comparison</li>
            <li><strong style="color: #90cdf4;">Subproblem solver</strong>: Solves subproblem at fixed master variables and extracts dual information</li>
            <li><strong style="color: #90cdf4;">Master problem solver</strong>: Accumulates Benders cuts and solves master problem iteratively</li>
            <li><strong style="color: #90cdf4;">Benders decomposition driver</strong>: Main algorithm loop with gap computation and convergence checking</li>
          </ul>
        </div>
        
        <a href="/data/benders.py" download style="display: inline-flex; align-items: center; background: #48bb78; color: white; padding: 0.875rem 2rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: background 0.2s ease; box-shadow: 0 2px 8px rgba(72, 187, 120, 0.25);">
          Download Source Code
        </a>
        
        </div>
        
        </div>
    design:
      columns: '1'
---
