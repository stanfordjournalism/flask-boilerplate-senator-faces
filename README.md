# Faces of Senators Flask Boilerplate App

## Getting started

From your command line, run the following to download the repo to your own computer:

```sh
$ git clone https://github.com/stanfordjournalism/flask-boilerplate-senator-faces.git
```

To run the app, which starts a webserver on your own machine at the address (URL) of `127.0.0.1:5000` (aka `localhost:5000`:

```sh
$ cd flask-boilerplate-senator-faces
$ python app.py
```

## Exploratory edits/tasks

Best way to get acquainted with the moving parts of this web application is to edit the code yourself.

Open the project folder in your text editor:

![img](http://i.imgur.com/2jgqBhB.png)


### Editing plain old HTML

A web application can serve up plain old *static* HTML, i.e. a text file that never changes. 

#### Messing around with CSS

This app includes the Bootstrap 4 (Alpha) framework, which is documented here:
https://v4-alpha.getbootstrap.com/


### Understanding Jinja templating and dynamic pages

Jinja is a mini-programming language that allows the use of code in otherwise plain HTML files:

- http://jinja.pocoo.org/docs/2.9/templates/
- https://realpython.com/blog/python/primer-on-jinja-templating/

### Changing the application code in app.py

- Add a proper 404 page
  + An example of a badly routed system: https://www.reddit.com/r/politics/comments/6a0tqp/donald_trumps_muslim_ban_disappears_from_website/dhaxxz8/
  + The pattern for ``/press-releases/someblahblahblah/`` would not 404 but go to the press releases pages:
    - It's fixed now: https://www.donaldjtrump.com/press-releases/my-plan-to-fuck-the-poor
    - Archive snapshot: https://web.archive.org/web/20170509073233/https://www.donaldjtrump.com/press-releases/my-plan-to-fuck-the-poor

- Let's create a non-dynamic route listing Senator twitter accounts
- Let's create a dynamic route that lists all senators who were born on a given day

### Changing how the data is wrangled in the helpers code





More step-by-step here: http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/


## References

Senator images from: https://github.com/unitedstates/images

Legislator data: https://sunlightlabs.github.io/congress/#legislator-spreadsheet

The legislator data as a [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1DFuMVHfnTAWGIbXHJIh_gcIAA8Yv96BsHTe6Juzr76k/edit#gid=0).

[Sen. Ted Cruz on ProPublica Represent](https://projects.propublica.org/represent/members/C001098-ted-cruz)


Flask app tutorial: http://www.compjour.org/homework/flask-app-101/



