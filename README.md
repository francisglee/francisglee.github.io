# Francis G. Lee
This is my personal website.

###Built with:
1. [Pelican](https://blog.getpelican.com/)

### Plugins
1. [Jupyter](https://github.com/danielfrg/pelican-ipynb)


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
|    ├──
|    ├──
|    ├──
|    ├──
|    ├──
|    └──
└── output
     ├──
     ├──
     ├──
     ├──
     ├──

```

### TODO
1. Need to get the Menu in right order
2. Get rid of titles in pages
3. get FL box to go to home
4. get menu boxes to be highlighted?


### Getting Started

1. Convert content to HTML.

    ```bash
    (venv)$ pelican -s pelicanconf.py # generates HTML for entire content
    ```

    ```bash
    (venv)$ pelican --write-selected output/posts/MY-POST-TITLE.md # generates HTML for single article, MY-POST-TITLE
    ```

2. View generated files locally (http://localhost:8000/).

    ```bash
    (venv)$ cd output | python3 -m http.server
    ```
3. Once you're ready to deploy your site to production, you'll have to regenerate the HTML with any production-specific settings (e.g.- analytic feeds, etc.)

    ```bash
    (venv)$ pelican content -s publishconf.py
    ```

### Deploy to Github Pages

1. Push contents to dev branch on website repository.

    ```bash
    (venv)$ git checkout -b dev # remove `-b` tag if dev branch already exists.
    (venv)$ git add . 
    (venv)$ git commit -m "New Post"
    (venv)$ git push origin dev
    ```
2. Use `ghp-import` to extract contents of the output folder to the master branch.

    ```bash
    (venv)$ ghp-import output -b master
    (venv)$ git push origin master
    ```
