# Dr. Jia-Sheng Hong - Personal Academic Website

This repository contains the source code for a minimal, responsive academic personal website built with [Jekyll](https://jekyllrb.com/) and [Tailwind CSS](https://tailwindcss.com/). It is designed to be hosted seamlessly on GitHub Pages.

## Features
- **Zero Configuration Deployment:** Push to GitHub and it goes live automatically on GitHub Pages.
- **Data-Driven:** Separate your content from your code. Update `_data/publications.yml` and the site updates automatically.
- **Responsive & Accessible:** Fully responsive design using Tailwind CSS with mobile navigation.
- **Dark Mode:** Built-in Light/Dark mode toggle that respects system preferences.
- **Academic Focused:** Includes a dynamic Publications page with year/type filtering, search, and one-click BibTeX citation copying.

## How to Deploy to GitHub Pages

1. **Create Repository:** 
   Push this folder to a new public GitHub repository. For the easiest setup, name the repository exactly `EternityJH.github.io`.
2. **Enable GitHub Pages:**
   - Go to your repository settings on GitHub.
   - On the left sidebar, click **Pages**.
   - Under **Build and deployment**, select **Deploy from a branch**.
   - Select the `main` (or `master`) branch, and the `/` (root) folder.
   - Click **Save**.
3. **Wait 1-2 minutes:** GitHub will automatically build and deploy your site to `https://eternityjh.github.io`.

## How to Update Your Information

This site is built so you rarely need to touch the HTML files. All primary content is driven by configuration and data files.

### 1. Update Core Information
Open `_config.yml` to change your name, email, social links, and Google Scholar ID.

### 2. Update Publications
To add a new paper, just open `_data/publications.yml` and add a new entry to the top:
```yaml
- title: "Your new awesome paper title here"
  authors: "JS Hong, A Einstein, I Newton"
  venue: "Nature"
  year: 2026
  citations: 0
  type: "journal" # Options: journal, conference, review
  doi: "10.1038/s41586-xxx"
  pdf_link: "https://example.com/paper.pdf"
```
Once you push this change to GitHub, the publications page will automatically update, including the filters and BibTeX copying!

### 3. Add CV and Profile Picture
- Place your CV PDF inside the repository (e.g., in an `assets/` folder) and update the `href` on the `cv.html` download button.
- Place a profile photo in the repository and uncomment the `<img src="...` line in `index.html`.

## Local Development (Testing before pushing)

If you want to view the site on your computer before pushing to GitHub:

1. You need Ruby installed on your computer.
2. Open terminal in this directory and run:
   ```bash
   gem install bundler jekyll
   bundle install
   bundle exec jekyll serve
   ```
3. Open `http://localhost:4000` in your browser.
