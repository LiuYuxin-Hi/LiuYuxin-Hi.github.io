---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-01-05
type: landing

design:
  # Default section spacing
  spacing: '0'

sections:
  # Developer Hero - Gradient background with name, role, social, and CTAs
  - block: dev-hero
    id: hero
    content:
      username: me
      greeting: "Hi, I'm"
      show_status: true
      show_scroll_indicator: true
      social_links:
        - icon: at-symbol
          label: liuyuxin254@mails.ucas.ac.cn
          url: mailto:liuyuxin254@mails.ucas.ac.cn
        - icon: github
          label: GitHub
          url: https://github.com/LiuYuxin-Hi
      typewriter:
        enable: true
        prefix: "I have published"
        strings:
          - "1 SSCI paper"
          - "2 CSSCI papers"
        type_speed: 70
        delete_speed: 40
        pause_time: 2500
      cta_buttons:
        - text: View My Work
          url: "#blog"
          icon: arrow-down
        - text: Get In Touch
          url: "#contact"
          icon: envelope
    design:
      style: centered
      avatar_shape: circle
      animations: true
      background:
        color:
          light: "#fafafa"
          dark: "#0a0a0f"
      spacing:
        padding: ["6rem", "0", "4rem", "0"]


  # Education Timeline
  - block: resume-experience
    id: experience
    content:
      title: Education
      date_format: Jan 2006
      items:
        - title: M.A. Public Policy
          company: University of Chinese Academy of Sciences
          company_url: 'https://www.ucas.ac.cn/'
          location: Beijing, China
          date_start: '2025-09-01'
          date_end: '2028-06-30'
          description: |2-
            * School of Public Policy and Management
            * Research Focus: Artificial Intelligence Governance, Digital Government
        - title: B.A. Public Affairs Management
          company: Southwest Jiaotong University
          company_url: 'https://www.swjtu.edu.cn/'
          location: Chengdu, China
          date_start: '2021-09-01'
          date_end: '2025-06-30'
          description: |2-
            * School of Public Administration
            * Rank: 1/67, GPA: 3.84/4.0, Comprehensive Score: 94.49
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]


# Recent Blog Posts
  - block: collection
    id: blog
    content:
      title: Papers
      subtitle: 'My Creativity'
      text: ''
      filters:
        folders:
          - blog
        exclude_featured: false
      count: 3
      order: desc
    design:
      view: card
      columns: 3
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]



  # Filterable Portfolio - Alpine.js powered project filtering
  - block: portfolio
    id: projects
    content:
      title: "Interships"
      subtitle: "My Practice"
      count: 0
      filters:
        folders:
          - projects
      buttons:
        - name: All
          tag: '*'
        - name: Full-Stack
          tag: Full-Stack
        - name: Frontend
          tag: Frontend
        - name: Backend
          tag: Backend
      default_button_index: 0
      # Archive link auto-shown if more projects exist than 'count' above
      # archive:
      #   enable: false  # Set to false to explicitly hide
      #   text: "Browse All"  # Customize text
      #   link: "/work/"  # Custom URL
    design:
      columns: 3
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # Visual Tech Stack - Icons organized by category
  - block: tech-stack
    id: Tech Stack
    content:
      title: "Tech Stack"
      subtitle: "My Advantages"
      categories:
        - name: Programming & Analysis
          items:
            - name: Python
              icon: devicon/python
            - name: R
              icon: devicon/r
            - name: Stata
              icon: custom/stata
            - name: SmartPLS
              icon: custom/smartpls
            - name: SPSS
              icon: custom/spss
        - name: Mapping & Visualization
          items:
            - name: ArcMap
              icon: custom/arcgis
            - name: Origin
              icon: custom/origin
            - name: CiteSpace
              icon: custom/citespace
        - name: Research & Reference
          items:
            - name: NVivo
              icon: custom/nvivo
            - name: Zotero
              icon: custom/zotero
    design:
      style: grid
      show_levels: false
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]



  # Contact Section
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Let's build something amazing together"
      text: |-
        I'm always interested in hearing about new opportunities.
        Whether you're looking to hire, collaborate, or just want to say hi, feel free to reach out!
      email: liuyuxin254@mails.ucas.ac.cn
      autolink: true
      links:
        - icon: "github"
          label: "Find me on"
          url: "https://github.com/LiuYuxin-Hi"
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # CTA Card
  - block: cta-card
    content:
      title: "Open to Opportunities"
      text: |-
        I'm currently looking for **new opportunities**.

        Let's connect and discuss how I can help your team.
      button:
        text: 'Download Resume'
        url: uploads/resume.pdf
        new_tab: true
    design:
      card:
        # Light mode: soft pastel theme gradient | Dark mode: rich deep gradient
        css_class: 'bg-gradient-to-br from-primary-200 via-primary-100 to-secondary-200 dark:from-primary-600 dark:via-primary-700 dark:to-secondary-700'
        text_color: dark
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "6rem", "0"]
---
