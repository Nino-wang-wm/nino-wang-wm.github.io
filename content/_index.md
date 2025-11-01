---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: |
        <div style="margin-top: 2rem; padding: 2rem; background: #f7fafc; border-radius: 8px; border-left: 4px solid #667eea;">
          <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 1rem 0; color: #1a202c;">
            Research Projects and Code
          </h3>
          <p style="line-height: 1.8; margin: 0 0 1.5rem 0; color: #4a5568; font-size: 0.95rem;">
            Explore my research projects in optimization and machine learning, including implementations 
            of decomposition techniques, nonlinear optimization methods, and computational algorithms. 
            Each project includes theoretical foundations, code implementations, and empirical analysis.
          </p>
          <a href="/project-code/" style="display: inline-block; padding: 0.75rem 2rem; background: #667eea; color: white; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.95rem; transition: background 0.2s ease;">
            View Projects →
          </a>
        </div>
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: 'About Me'
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
---
