---
title: ''
summary: ''
date: 2026-01-05
type: landing

design:
  spacing: '0'

sections:
  # Education / Experience
  - block: resume-experience
    id: experience
    content:
      title: Education
      date_format: Jan 2006
      items:
        - title: "Institute for Contemporary China Studies, Tsinghua University"
          company: "Research Assistant"
          company_url: ''
          company_logo: ''
          location: Beijing, China
          date_start: '2025-09-01'
          date_end: '2026-02-28'
          description: |2-
            * Assisted research on contemporary China studies projects
        - title: "JiuLiTi North Community, Jinniu District, Chengdu"
          company: "Financial Assistant"
          company_url: ''
          company_logo: ''
          location: Chengdu, China
          date_start: '2023-06-01'
          date_end: '2023-07-31'
          description: |2-
            * Supported community financial operations and reporting
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # Papers
  - block: collection
    id: blog
    content:
      title: Papers
      subtitle: 'My publications and research papers'
      filters:
        folders:
          - papers
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

  # Internships / Projects
  - block: collection
    id: projects
    content:
      title: Internships
      subtitle: 'Professional experience and projects'
      filters:
        folders:
          - projects
      count: 3
      order: desc
    design:
      view: card
      columns: 3
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # Skills / Tech Stack
  - block: tech-stack
    id: skills
    content:
      title: Skills
      subtitle: "Technologies I use"
      categories:
        - name: Languages
          items:
            - name: TypeScript
              icon: devicon/typescript
            - name: Python
              icon: devicon/python
            - name: JavaScript
              icon: devicon/javascript
        - name: Frontend
          items:
            - name: React
              icon: devicon/react
            - name: Next.js
              icon: devicon/nextjs
            - name: Tailwind CSS
              icon: devicon/tailwindcss
        - name: Backend
          items:
            - name: Node.js
              icon: devicon/nodejs
            - name: Express
              icon: devicon/express
            - name: PostgreSQL
              icon: devicon/postgresql
    design:
      style: grid
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # Contact
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Let's connect"
      text: |-
        I'm open to opportunities and collaborations. Reach out via email!
      email: alex@example.com
      autolink: true
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
---