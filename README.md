# brython-project-template

## What is it?

This template contains the following characteristics that are likely useful
when starting a new [Brython](https://brython.info)-powered project.

* The index.html embeds a loading animation to give end user a hint to be patient.
  This can be helpful because the first time loading of Brython is slower.
  (Note to Developer: The loading animation does *not* represent the real progress.
  If your website stuck with the loading animation,
  open the browser console to check for error messages.)
* The index.html references bootstrap and Brython from their CDN;
  You can easily switch to use the not-yet-released latest Brython source from github;
  An optional browser-console simulator, useful if you are browsing from Android device.
  (All these can be easily comment or uncomment from the index.html.)
* The website root directory is nested inside this project.
  This setup would provide better separation
  when you also creates virtual env `.venv` inside your project directory.
  (Otherwise you could hit [a known issue](https://github.com/brython-dev/brython/issues/1603).)

## How to use?

You can use this repo as a template to start your own project.

1. [One click to use this repo as a template to start your project on github](https://github.com/rayluo/brython-project-template/generate),
   or manually clone or download this repo as your starting point.
2. Run `python3 -m http.server` to start a web server,
   and then visit `http://localhost:8000` to see it in action.

That is all. Once you are familiar with this project's structure,
you can modify it by changing
the content inside `<div id="main" ...>...</div>` from `index.html`
and content inside `main.py`.

