---
title: 'Larson Hypercube Replication'
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
          Larson Hypercube Queuing Model Replication
        </h1>
        <h2 style="font-size: 1.25rem; font-weight: 500; color: #cbd5e0; margin: 0 0 3rem 0; font-style: italic;">
          A hypercube queuing model for facility location and redistricting in urban emergency services
        </h2>
        
        <div style="border-left: 4px solid #48bb78; padding-left: 2rem; margin-bottom: 3rem;">
          <p style="font-size: 1.05rem; line-height: 1.9; color: #e2e8f0; margin: 0; text-align: justify;">
            This project implements Larson's 1974 hypercube queuing model, a fundamental framework for analyzing 
            facility location and redistricting problems in urban emergency services. The implementation includes 
            both zero-line and infinite-line capacity models with comprehensive analysis tools, visualization 
            capabilities, and performance evaluation metrics. The model provides insights into system workload 
            distributions, response time analysis, and optimization strategies for emergency service deployments.
          </p>
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; margin: 2rem 0; display: flex; align-items: center; gap: 2rem;">
          <div style="flex: 1;">
            <h3 style="font-size: 1.35rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
              Open Source Implementation
            </h3>
            <p style="color: #e2e8f0; margin: 0; line-height: 1.8; font-size: 1rem;">
              Explore the complete implementation with examples, notebooks, and comprehensive documentation on GitHub.
            </p>
          </div>
          <a href="https://github.com/Nino-wang-wm/larson-paper-replication" target="_blank" style="display: inline-flex; align-items: center; background: transparent; color: #90cdf4; padding: 1rem 2.5rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: all 0.2s ease; border: 1px solid #4a5568; white-space: nowrap;">
            View on GitHub
          </a>
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 4rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Project Features</h2>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin: 2rem 0;">
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 1.5rem; transition: all 0.2s ease;">
          <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Dual Model Implementation
          </h4>
          <p style="color: #e2e8f0; margin: 0; line-height: 1.7; font-size: 0.95rem;">
            Both zero-line and infinite-line capacity models with comprehensive state space analysis
          </p>
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 1.5rem; transition: all 0.2s ease;">
          <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Performance Analytics
          </h4>
          <p style="color: #e2e8f0; margin: 0; line-height: 1.7; font-size: 0.95rem;">
            Workload distributions, response time metrics, and queue length analysis
          </p>
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 1.5rem; transition: all 0.2s ease;">
          <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Visualization Tools
          </h4>
          <p style="color: #e2e8f0; margin: 0; line-height: 1.7; font-size: 0.95rem;">
            Static plots with matplotlib and interactive dashboards using Plotly
          </p>
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 1.5rem; transition: all 0.2s ease;">
          <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.75rem 0; color: #ffffff;">
            Sensitivity Analysis
          </h4>
          <p style="color: #e2e8f0; margin: 0; line-height: 1.7; font-size: 0.95rem;">
            Comprehensive tools for system optimization and parameter sensitivity studies
          </p>
        </div>
        
        </div>
        
        <h2 style="font-size: 1.5rem; font-weight: 700; color: #ffffff; margin: 4rem 0 1.5rem 0; border-bottom: 2px solid #4a5568; padding-bottom: 0.75rem;">Technical Details</h2>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        
        <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff;">
          Core Components
        </h3>
        
        <ul style="color: #e2e8f0; line-height: 2; margin: 0; padding-left: 1.5rem; font-size: 1rem;">
          <li>Hypercube state sequence generation and management</li>
          <li>Steady-state probability computation with iterative methods</li>
          <li>Transition rate matrix handling for Markov chain analysis</li>
          <li>Performance metrics calculation (utilization, response times)</li>
          <li>Model comparison utilities and optimization tools</li>
        </ul>
        
        </div>
        
        <div style="background: #1a202c; border: 1px solid #4a5568; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        
        <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 1rem 0; color: #ffffff;">
          Implementation Highlights
        </h3>
        
        <div style="color: #e2e8f0; line-height: 1.8; font-size: 1rem;">
          <p style="margin: 0 0 1rem 0;">
            The implementation follows Larson's original paper methodology while incorporating modern Python 
            libraries for computational efficiency. Key features include configurable system parameters (number 
            of units, arrival/service rates), flexible dispatch policies (MCM, district-based, workload-based), 
            and comprehensive analysis tools for comparing model behaviors under different utilization levels.
          </p>
          <p style="margin: 0;">
            The project architecture separates core algorithmic components, model implementations, analysis 
            tools, and visualization modules, ensuring modularity and extensibility for future enhancements 
            and research applications.
          </p>
        </div>
        
        </div>
        
        </div>
    design:
      columns: '1'
---

