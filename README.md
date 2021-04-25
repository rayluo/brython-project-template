# brython-project-template

## What is it?

This template contains the following characteristics that are likely useful
when starting a new [Brython](https://brython.info)-powered project.

* The index.html embeds a loading animation to give end user a hint to be patient.
  This can be helpful because the first time loading of Brython is slower.
  (Note to Developer: The loading animation does *not* represent the real progress.
  If your website stuck with the loading animation,
  open the browser console to check for error messages.)
* Although not a Brython-relevant feature,
  this template includes a github workflow to deploy your each push to Github Pages
  (After the first deployment which prepares your website into the default `gh-pages` branch,
  you need a one-time effort to
  [enable Github Pages](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
   for your github repo.)
* The index.html automatically loads latest released version of Brython from CDN.
  You can easily switch to use the not-yet-released latest Brython source from github.
* The index.html references bootstrap from CDN for better layout.
* An optional browser-console simulator, useful if you are browsing from Android device.
  (All these can be easily comment or uncomment from the index.html.)
* The website root directory is nested inside this project.
  This setup would provide better separation
  when you also creates virtual env `.venv` inside your project directory.
  (Otherwise you could hit [a known issue](https://github.com/brython-dev/brython/issues/1603).)

## How to use?

You can use this repo as a template to start your own project.

1. Your options are:
   * [use this repo as a template to start your project on github](https://github.com/rayluo/brython-project-template/generate),
   * or manually clone [this project](https://github.com/rayluo/brython-project-template)
   * or [download its zip package](https://github.com/rayluo/brython-project-template/archive/refs/heads/main.zip)
2. Run `python3 -m http.server` to start a web server,
   and then visit `http://localhost:8000` to see it in action.

That is all. Once you are familiar with this project's structure,
you can modify it by changing the content between
`<!-- The real project content starts from here -->` and `<!-- The real project content ends here -->`
in `index.html`,
and content inside `main.py`.

Alternatively, if you already have an existing project,
you can add the loading animation by including this snippet into your `index.html`

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<script src="https://rayluo.github.io/brython-project-template/loader.js"></script>
<script type="text/javascript">start_loader("Loading System...")</script>
```
