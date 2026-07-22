# 🌐 DevOps Portfolio Website

A modern, responsive portfolio website showcasing my experience, technical skills, projects, and resume as a Cloud & DevOps Engineer.

**Live Website**

👉 https://debuntu.github.io/portfolio-v2/

---

# 📸 Preview

![Portfolio Screenshot](assets/images/profile.jpg)

---

# 🚀 Features

- Responsive design (Desktop, Tablet & Mobile)
- Professional landing page
- About Me section
- Featured DevOps Projects
- Downloadable Resume
- Contact Form powered by Formspree
- GitHub Pages hosting
- Automatic deployment using GitHub Actions
- Bootstrap 5 UI
- Clean HTML, CSS and JavaScript

---

# 🛠️ Tech Stack

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Git
- GitHub
- GitHub Actions
- GitHub Pages
- Formspree

---

# 📂 Project Structure

```
portfolio-v2/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── assets/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   ├── images/
│   │   └── profile.jpg
│   │
│   └── files/
│       └── resume_latest.pdf
│
├── favicon.ico
├── index.html
├── about.html
├── projects.html
├── resume.html
├── contact.html
└── README.md
```

---

# 💻 Run Locally

Clone the repository

```bash
git clone https://github.com/Debuntu/portfolio-v2.git
```

Go into the project directory

```bash
cd portfolio-v2
```

Open the website

```
index.html
```

or use VS Code Live Server.

---

# 🚀 Deployment using GitHub Pages

## Step 1

Push the project to GitHub.

---

## Step 2

Go to

```
Repository

↓

Settings

↓

Pages
```

---

## Step 3

Under **Build and Deployment**

Choose

```
Source

GitHub Actions
```

---

## Step 4

Create the following workflow

```
.github/workflows/deploy.yml
```

with the following contents

```yaml
name: Deploy Portfolio to GitHub Pages

on:
  push:
    branches:
      - main

  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  deploy:

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/configure-pages@v5

      - uses: actions/upload-pages-artifact@v3
        with:
          path: .

      - id: deployment
        uses: actions/deploy-pages@v4
```

---

# 📧 Contact Form (Formspree)

Since GitHub Pages only hosts static websites, it cannot process form submissions directly.

This project uses **Formspree** to receive messages from visitors.

## Create a Formspree Account

Visit

```
https://formspree.io
```

Sign up using

- GitHub
- Google
- Email

---

## Create a New Form

Click

```
New Form
```

Give the form a name, for example

```
Portfolio Contact
```

After creation, Formspree provides an endpoint similar to

```
https://formspree.io/f/xxxxxxxxx
```

---

## Update contact.html

Replace

```html
<form action="https://formspree.io/f/YOUR_FORM_ID"
      method="POST">
```

with

```html
<form action="https://formspree.io/f/xxxxxxxxx"
      method="POST">
```

using your own Formspree endpoint.

---

## Verify Your Email

After submitting the first test message, Formspree will send a verification email.

Click the verification link.

Once verified, all future messages submitted through the website will be delivered directly to your email.

---

# 📄 Resume

Replace

```
assets/files/resume_latest.pdf
```

with your latest resume whenever you want to update it.

No additional configuration is required.

---

# 🎨 Favicon

Generate a favicon from your profile picture using

https://favicon.io/favicon-converter/

Copy

```
favicon.ico
```

to the project root.

---

# 📷 Updating Your Profile Photo

Replace

```
assets/images/profile.jpg
```

with a new image using the same filename.

---

# 📈 Future Improvements

- Dark Mode
- Blog Section
- GitHub API Integration
- Visitor Analytics
- Project Filtering
- GitHub Contributions Graph
- Resume Version History

---

# 👨‍💻 Author

**Debashish Talukder**

Senior Cloud & DevOps Engineer

GitHub

https://github.com/Debuntu

LinkedIn

(Add your LinkedIn profile here)

Portfolio

https://debuntu.github.io/portfolio-v2/

---

# 📄 License

This project is licensed under the MIT License.

Feel free to fork, customize, and use it as inspiration for your own portfolio.