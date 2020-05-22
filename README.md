

Website of Philip Shemella - https://smalldata.dev/about

[![Build Status](https://api.travis-ci.org/philshem/smalldata.github.io.svg?branch=master)](https://travis-ci.org/philshem/smalldata.github.io)

This page is built with [Pelican](https://github.com/getpelican/pelican/) and the [Bulrush](https://github.com/textbook/bulrush) theme.


---

## setup

get the code (clone this repository)

create/load virtual environment

    python3.7 -m venv venv
    source venv/bin/activate

install dependencies

    pip install -r requirements.txt

    brew install node
    npm install less --global

get plugins as git submodule

```
git submodule add https://github.com/getpelican/pelican-plugins.git
git submodule init
git submodule update --init --recursive
```

## build and deploy

development server

    make clean && make devserver

make changes live (this is automatically done by CI/CD tool at time of each `git push` to master)

```
make clean && make html
ghp-import output -b gh-pages
git push git@github.com:smalldata/smalldata.github.io.git gh-pages:master
```