# FrancisGLee.com

### Built with:

1.  [Pelican](https://blog.getpelican.com/)

### Plugins:

1.  [Jupyter](https://github.com/danielfrg/pelican-ipynb)
2.  [Disqus](https://github.com/getpelican/pelican-plugins/tree/master/disqus_static)
3.  [Render Math](https://github.com/getpelican/pelican-plugins/tree/master/render_math). This cannot be updated using `git submodule add` !!! :( (I had to copy repo manually) I should add the entire plugin repo as a submodule...

### Directory

```
├── requirements.txt
├── README.md
├── pelicanconf.py
├── publishconf.py
├── Makefile
├── fabfile.py
├── develop_server.sh
├── .gitignore
├── venv
├── themes
|    └── portfolio
├── plugins
|    ├── Jupyter
|    ├── Google Analytics
|    ├── Disqus
|    ├──
|    ├──
|    ├──
|    └──
├── contents
|    ├── images
|    ├── pages
|    ├── pdfs
|    └── posts
└── output
     ├──
     ├──
     ├──
     ├──
     ├──
     └──
```

### TODO

1.  Need to get the Menu in right order
2.  Get rid of titles in pages
3.  get FL box to go to home
4.  get menu boxes to be highlighted?
5.  get blog to have the index.html layout
6.  creating submenus
7.  Fix URL
8.  Get widgets on every page

### Getting Started

1.  Clone this repository with associated submodules.

    ```bash
    $ git clone --recurse-submodules https://www.github.com/francisglee/francisglee.github.io
    ```

2.  Activate virtual environment and install Python packages.

    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv)$ pip3 install -r requirements.txt
    ```

### Develop Locally

1.  Convert content to HTML.

    ```bash
    (venv)$ pelican -s pelicanconf.py # generates HTML for entire content
    ```

    ```bash
    (venv)$ pelican --write-selected output/posts/MY-POST-TITLE.md # generates HTML for single article, MY-POST-TITLE
    ```

2.  View generated files locally (http://localhost:8000/).

    ```bash
    (venv)$ cd output | python3 -m http.server
    ```

3.  Once you're ready to deploy your site to production, you'll have to regenerate the HTML with any production-specific settings (e.g.- analytic feeds, etc.)

    ```bash
    (venv)$ pelican content -s publishconf.py
    ```

### Deploy to Github Pages

1.  Push contents to dev branch on website repository.

    ```bash
    (venv)$ git checkout -b dev # remove `-b` tag if dev branch already exists.
    (venv)$ git add .
    (venv)$ git commit -m "New Post"
    (venv)$ git push origin dev
    ```

2.  Use `ghp-import` to extract contents of the output folder to the master branch.

    ```bash
    (venv)$ ghp-import output -b master
    (venv)$ git push origin master
    ```

### Resources

1. http://blog.gabrielrezzonico.com/data-science-portfolio-using-pelican.html
2. https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
3. https://jjakimoto.github.io/articles/2018/Mar/01/start_blog/
4. 