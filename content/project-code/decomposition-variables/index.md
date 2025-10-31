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
      title: '<div style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.5rem;">⚡ Decomposition-complicated Variables</div>'
      subtitle: '<div style="font-size: 1.1rem; color: #718096; margin-bottom: 2rem;">Benders Decomposition for Complex Variable Optimization</div>'
      text: |-
        <div style="max-width: 1200px; margin: 0 auto;">
        
        <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568; margin-bottom: 3rem;">
          This implementation demonstrates Benders decomposition, a powerful technique for solving 
          optimization problems with complicated variables. The algorithm iteratively adds cutting planes 
          to converge to the optimal solution by separating the problem into a master problem and subproblems.
        </p>
        
        ## 📚 Documentation
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
        
        <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); transition: all 0.3s ease;">
          <div style="font-size: 2rem; margin-bottom: 1rem;">📊</div>
          <h3 style="font-size: 1.2rem; font-weight: 700; margin: 0 0 0.5rem 0; color: #2d3748;">
            Calculation Document
          </h3>
          <p style="color: #718096; margin: 0 0 1rem 0; line-height: 1.6;">
            Detailed PDF document with calculations, theoretical background, and numerical examples.
          </p>
          <a href="/data/calculation.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #f5576c; text-decoration: none; font-weight: 600; transition: color 0.3s ease;">
            View PDF <span style="margin-left: 0.5rem;">→</span>
          </a>
        </div>
        
        </div>
        
        ## 💻 Code Implementation
        
        <div style="background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%); border-radius: 16px; padding: 2.5rem; margin: 2rem 0; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);">
        
        <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
          <div style="font-size: 2rem; margin-right: 1rem;">🐍</div>
          <div>
            <h3 style="font-size: 1.5rem; font-weight: 700; margin: 0; color: white;">
              benders.py
            </h3>
            <p style="color: #a0aec0; margin: 0.5rem 0 0 0;">
              Python implementation using Gurobi optimizer
            </p>
          </div>
        </div>
        
        <p style="color: #cbd5e0; line-height: 1.8; margin-bottom: 1.5rem;">
          Complete implementation of the Benders decomposition algorithm. The code includes a direct solve 
          method for baseline comparison, subproblem and master problem solvers, and the main Benders 
          decomposition driver with iteration tracking.
        </p>
        
        <div style="background: rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0;">
          <h4 style="color: #f7fafc; font-weight: 600; margin: 0 0 1rem 0;">Key Components:</h4>
          <ul style="color: #cbd5e0; line-height: 2; margin: 0; padding-left: 1.5rem;">
            <li><strong style="color: #fbb6ce;">Direct solve method</strong>: Baseline solver for comparison</li>
            <li><strong style="color: #fbb6ce;">Subproblem solver</strong>: Solves the subproblem at a fixed x value</li>
            <li><strong style="color: #fbb6ce;">Master problem solver</strong>: Solves the master problem with accumulated Benders cuts</li>
            <li><strong style="color: #fbb6ce;">Benders decomposition driver</strong>: Main algorithm with iteration tracking</li>
          </ul>
        </div>
        
        <a href="/data/benders.py" download style="display: inline-flex; align-items: center; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 0.875rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; transition: transform 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);">
          <span style="margin-right: 0.5rem;">⬇️</span> Download Code
        </a>
        
        </div>
        
        </div>
    design:
      columns: '1'
---
