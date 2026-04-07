---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.avatar
    id: about
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      # Override your bio text from `authors/admin/_index.md`?
      text:
  - block: collection
    id: featured
    content:
      title: Selected Publications
      text: |-
        Explore the full [publications archive](/publication/) for papers and linked materials.
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      columns: '2'
      view: citation
  #- block: features
   # content:
    #  title: Skills
     # items:
      #  - name: R
       #   description: 90%
        #  icon: r-project
         # icon_pack: fab
        #- name: Statistics
        #  description: 100%
        #  icon: chart-line
        #  icon_pack: fas
        #- name: Photography
        #  description: 10%
        #  icon: camera-retro
        #  icon_pack: fas
  - block: experience
    content:
      title: Education
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: PhD Candidate
          company: Harvard University
          company_url: ''
          company_logo: org-gc
          location: Cambridge MA, USA
          date_start: '2022-08-31'
          date_end: ''
          description: ''
        - title: Bachelor of Science in Applied Mathematics
          company: Instituto Tecnológico Autónomo de México
          company_url: ''
          company_logo: org-x
          location: Mexico City, Mexico
          date_start: '2015-08-09'
          date_end: '2019-12-30'
          description: Graduated with honors by acquiring a special mention thanks to my thesis titled “A study concerning the Chebyshev Center problem in finite-dimensional normed vector spaces” under the supervision of Dr. Cesar Garcia-Garcia.
    design:
      columns: '2'
  #- block: accomplishments
  #  content:
  #    # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
  #    title: 'Accomplish&shy;ments'
  #    subtitle:
      # Date format: https://wowchemy.com/docs/customization/#date-format
  #    date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
  #    items:
       # - certificate_url: https://www.coursera.org
   #       date_end: ''
          #date_start: '2021-01-25'
          #description: ''
          #organization: Coursera
          #organization_url: https://www.coursera.org
          #title: Neural Networks and Deep Learning
        # #url: ''
        #- certificate_url: https://www.edx.org
         # date_end: ''
          #date_start: '2021-01-01'
          #description: Formulated informed blockchain models, hypotheses, and use cases.
        #  organization: edX
        #  organization_url: https://www.edx.org
        #  title: Blockchain Fundamentals
        #  url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
        #- certificate_url: https://www.datacamp.com
        #  date_end: '2020-12-21'
        #  date_start: '2020-07-01'
        #  description: ''
        #  organization: DataCamp
        #  organization_url: https://www.datacamp.com
        #  title: 'Object-Oriented Programming in R'
        # url: ''
    #design:
      #columns: '2'
  #- block: collection
  #  id: posts
   # content:
    #  title: Recent Posts
     # subtitle: ''
      #text: ''
      # Choose how many pages you would like to display (0 = all pages)
      #count: 5
      # Filter on criteria
      #filters:
       # folders:
        #  - post
        #author: ""
        #category: ""
        #tag: ""
        ##exclude_featured: false
        #exclude_future: false
        #exclude_past: false
        #publication_type: ""
      # Choose how many pages you would like to offset by
      #offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      #order: desc
    #design:
     # # Choose a layout view
      #view: compact
      #columns: '2'
  #- block: portfolio
  #  id: projects
   # content:
    #  title: Projects
     ###   - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      #default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      #buttons:
       # - name: All
        #  tag: '*'
       # - name: Deep Learning
        #  tag: Deep Learning
        #- name: Other
        #  tag: Demo
    #design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
     # columns: '1'
     # view: showcase
      # For Showcase view, flip alternate rows?
     # flip_alt_rows: false
  #- block: markdown
   # content:
  #    title: Gallery
   #   subtitle: ''
   #   text: |-
  #      {{< gallery album="demo" >}}
  #  design:
 #     columns: '1'
  #- block: collection
   # id: featured
    #content:
     # title: Featured Publications
      #filters:
       # folders:
        #  - publication
        #featured_only: true
    #design:
     # columns: '2'
      #view: card
  #- block: collection
  #  id: talks
  ##  content:
   #   title: Recent & Upcoming Talks
   #   filters:
    #    folders:
    #      - event
    #design:
    #  columns: '2'
    #  view: compact
  #- block: tag_cloud
  #  content:
   #   title: Popular Topics
   # design:
    #  columns: '2'
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        Email is the best way to reach me. You can also use the profile links above for Google Scholar, GitHub, LinkedIn, and my CV.
      # Contact (add or remove contact options as necessary)
      email: jtelloayala [at] g [dot] harvard [dot] edu
      #phone: 888 888 88 88
      #appointment_url: 'https://calendly.com'
      #address:
      #  street: 450 Serra Mall
      #  city: Stanford
      #  region: CA
      #  postcode: '94305'
      #  country: United States
      #  country_code: US
      #directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      #office_hours:
      #  - 'Monday 10:00 to 13:00'
      #  - 'Wednesday 09:00 to 10:00'
      #contact_links:
      #  - icon: twitter
      #    icon_pack: fab
      #    name: DM Me
       #   link: 'https://twitter.com/Twitter'
      #  - icon: skype
      #    icon_pack: fab
      #    name: Skype Me
      #    link: 'skype:echo123?call'
      #  - icon: video
       #   icon_pack: fas
      #    name: Zoom Me
       #   link: 'https://zoom.com'
      # Automatically link email and phone or display as text?
      autolink: true
      contact_links:
        - icon: graduation-cap
          icon_pack: fas
          name: Google Scholar
          link: https://scholar.google.com/citations?user=EAJekCcAAAAJ&hl=es
        - icon: github
          icon_pack: fab
          name: GitHub
          link: https://github.com/robtelloayala
        - icon: linkedin
          icon_pack: fab
          name: LinkedIn
          link: https://www.linkedin.com/in/josé-roberto-tello-ayala-339b04129/
        - icon: cv
          icon_pack: ai
          name: CV
          link: uploads/resume.pdf
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '2'
---
