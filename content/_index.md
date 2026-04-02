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
      filters:
        folders:
          - blog
        exclude_featured: false
      count: 3
      order: desc
    design:
      view: card
      columns: 3
      show_tags: true
      show_author: false
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
    id: skills
    content:
      title: "Tech Stack"
      subtitle: "My Skills"
      categories:
        - name: Programming & Analysis
          items:
            - name: Python
              icon: devicon/python
            - name: R
              icon: devicon/r
            - name: Stata
              icon: media/pictures/stata
            - name: SmartPLS
              icon: media/pictures/smartpls
            - name: SPSS
              icon: media/pictures/spss
        - name: Mapping & Visualization
          items:
            - name: ArcMap
              icon: media/pictures/arcgis
            - name: Origin
              icon: media/pictures/origin
            - name: CiteSpace
              icon: media/pictures/citespace
        - name: Research & Reference
          items:
            - name: NVivo
              icon: media/pictures/nvivo
            - name: Zotero
              icon: media/pictures/zotero
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
      title: Contact
      subtitle: "Let's build something amazing together"
      text: |-
        I'm always interested in hearing about new projects and opportunities.
        Whether you're looking to hire, collaborate, or just want to say hi, feel free to reach out!
      email: liuyuxin254@mails.ucas.ac.cn
      autolink: true
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
