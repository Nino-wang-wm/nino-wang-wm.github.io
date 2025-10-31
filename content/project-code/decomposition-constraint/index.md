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
      title: '<div style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.5rem;">🔗 Decomposition-complicated Constraint</div>'
      subtitle: '<div style="font-size: 1.1rem; color: #718096; margin-bottom: 2rem;">Column Generation Methods for Complex Constraint Optimization</div>'
      text: |-
        <div style="max-width: 1200px; margin: 0 auto;">
        
        <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568; margin-bottom: 3rem;">
          This implementation demonstrates column generation techniques for solving linear programs with 
          complicating constraints. The algorithm decomposes the problem into block-structured subproblems 
          and iteratively generates columns to converge to the optimal solution.
        </p>
        
        ## 📚 Documentation
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
        
        <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); transition: all 0.3s ease;">
          <div style="font-size: 2rem; margin-bottom: 1rem;">📄</div>
          <h3 style="font-size: 1.2rem; font-weight: 700; margin: 0 0 0.5rem 0; color: #2d3748;">
            CVLP1 Document
          </h3>
          <p style="color: #718096; margin: 0 0 1rem 0; line-height: 1.6;">
            Comprehensive PDF document detailing constraint-based decomposition methods and theoretical foundations.
          </p>
          <a href="/data/cvlp1.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #667eea; text-decoration: none; font-weight: 600; transition: color 0.3s ease;">
            View PDF <span style="margin-left: 0.5rem;">→</span>
          </a>
        </div>
        
        <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); transition: all 0.3s ease;">
          <div style="font-size: 2rem; margin-bottom: 1rem;">📄</div>
          <h3 style="font-size: 1.2rem; font-weight: 700; margin: 0 0 0.5rem 0; color: #2d3748;">
            CVLP2 Document
          </h3>
          <p style="color: #718096; margin: 0 0 1rem 0; line-height: 1.6;">
            Additional documentation on constraint decomposition with advanced examples and case studies.
          </p>
          <a href="/data/cvlp2.pdf" target="_blank" style="display: inline-flex; align-items: center; color: #667eea; text-decoration: none; font-weight: 600; transition: color 0.3s ease;">
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
              cvlp3.py
            </h3>
            <p style="color: #a0aec0; margin: 0.5rem 0 0 0;">
              Python implementation using Gurobi optimizer
            </p>
          </div>
        </div>
        
        <p style="color: #cbd5e0; line-height: 1.8; margin-bottom: 1.5rem;">
          Complete implementation of the column generation algorithm for problems with complicating constraints. 
          The code includes initialization, master problem solving, and iterative column generation.
        </p>
        
        <div style="background: rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0;">
          <h4 style="color: #f7fafc; font-weight: 600; margin: 0 0 1rem 0;">Key Components:</h4>
          <ul style="color: #cbd5e0; line-height: 2; margin: 0; padding-left: 1.5rem;">
            <li><strong style="color: #90cdf4;">Block solver</strong>: Solves subproblems for each block with modified costs</li>
            <li><strong style="color: #90cdf4;">Master problem solver</strong>: Always-feasible master with penalty variables</li>
            <li><strong style="color: #90cdf4;">Column generation loop</strong>: Iterative algorithm that adds columns until convergence</li>
            <li><strong style="color: #90cdf4;">Full LP solver</strong>: Direct solve for comparison with the decomposition approach</li>
          </ul>
        </div>
        
        <a href="/data/cvlp3.py" download style="display: inline-flex; align-items: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.875rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; transition: transform 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">
          <span style="margin-right: 0.5rem;">⬇️</span> Download Code
        </a>
        
        </div>
        
        </div>
    design:
      columns: '1'
---
