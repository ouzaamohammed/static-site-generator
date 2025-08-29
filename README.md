# Static Site Generator

A simple static site generator built with Python.

## Motivation / why

Learning exercise on [boot.dev](https://boot.dev/courses/build-static-site-generator-python) to understand how static site generators like [Hugo](https://gohugo.io/) work under the hood.

## Features

- Converts Markdown to HTML
- Copy static files to `/docs` directory
- Deploys the final generated site to github pages

## Usage

Clone the repository

```bash
git clone https://github.com/ouzaamohammed/static-site-generator
cd static-site-generator
```

Open the project inside your text editor of choice.

Create your Markdown pages inside `/content` directory, and copy your assets to `/static` directory.

Run these commands

```bash
chmod +x main.sh
./main.sh
```

This should generate your site in `/docs` directory and copy all assets from `/content`.

Visit http://localhost:8888/ to see your site.

## How it works?

![static site generator example](/assets/images/static-site-generator-example.png)
