## Introduction to Flask

### What do we want to accomplish?
You might be unfamiliar with what goes into creating a web application,
so let's go over what we're trying to accomplish.

We want users to be able to visit web pages created by our application,
so we'll need some way to *route requests to content.*
Flask, which has [an excellent tutorial](http://flask.pocoo.org/docs/0.10/),
will provide this functionality.

Maybe this content already exists,
or maybe *the application has to generate it upon request.*
To generate new content, we'd like to create template pages
that our application can fill out for the user.
Flask includes the [Jinja2](http://jinja.pocoo.org/)
templating library by default for this purpose,
but we could always choose a different one like
[Mako](http://www.makotemplates.org/).

Finally, we'd like to keep our data -
which will be used to fill out our template documents -
in a database.
To avoid maintaining a lot of queries directly in SQL,
we can use a library like [SQLAlchemy](https://www.sqlalchemy.org/)
for [object relational mapping](https://en.wikipedia.org/wiki/Object-relational_mapping).
That's a long phrase that just means we'd like to
*call methods on Python objects instead of writing SQL.*

1. ##### Today's deep dive: [Run Flask](http://flask.pocoo.org/)

    ```bash
    # This part goes in your bash shell.
    # you must have python-virtualenv and python-pip installed to use a virtualenv
    $ mkdir sampleapp
    $ cd sampleapp
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install flask
    ```

    ```python
    from flask import Flask
    app = Flask(__name__)

	# never leave this on in production or someone will break your site.
	app.debug = True

    @app.route("/")
    def hello():
        return "Hello world!"

    if __name__ == "__main__":
        app.run()
		# app.run(0.0.0.0) # will run your site on all public IPs. No need to do this.
    ```

    1. Ok... how do I see my work?
        1. Run your application `$ python app.py`
        2. In a browser, go to `http://localhost:5000`
        3. You should see these words: `Hello world!`

    2. Other topics we will cover today:
        1. Accessing a template
        2. Organizing your templates
        3. Static assets


2. ##### Lets get this working with a template!

    1. Flask [uses Jinja2](http://jinja.pocoo.org/docs/dev/).
        1. We just import it. There is [a tutorial](http://flask.pocoo.org/docs/0.10/tutorial/templates/) for this.
        2. Lets update our code to have the extra import and a new route/template.

            ```python
            from flask import Flask, render_template, url_for
            
            # lets add a new route
            @app.route("/sample-page/")
            def samplepage():
                return render_template("sample-page.html")
            ```

        3. This sample is from the tutorial's template page. Put this in `/templates/sample-page.html`. `/templates/` is the default path in a Flask project.

            ```html
            <!doctype html>
            <title>Sample Template</title>
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
            <div class=page>
              <h1>This is our sample app!</h1>
              {% block body %}
              {% endblock %}
            </div>
            ```
        4. Make a directory `static` in your project and add an empty `style.css` file to it.

        5. The [key features of templates](http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/) are `{% block MYBLOCK %}`, `import`, and `extends`.
            1. Usually you will use a base template that will just have blocks.
                1. Some default blocks: `header`, `head`, `title`, `body`, `footer`, `footerjs`
                2. Then inside the base template you'll `include` different files.
                3. Finally, on your actual pages, you'll `extend` your base template with actual content.
                4. If you want to see a template system, check out [library-org](https://github.com/robbintt/library-org)
            2. ###### We won't cover these details today, please review this in detail and try it out.
        


3. ##### The final piece today is a Model! This wires a database into our app.

    1. [There are a lot of ways to use Flask-SQLAlchemy](http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/).
        1. We will follow the [Flask-SQLAlchemy Extension](http://flask-sqlalchemy.pocoo.org/2.1/) pattern.
        2. The following code is cribbed from [here](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application). Please put this code in `sample_model.py`.

            ```python
			from flask import Flask
			from flask_sqlalchemy import SQLAlchemy

			app = Flask(__name__)
			app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
			db = SQLAlchemy(app)

			class User(db.Model):
				id = db.Column(db.Integer, primary_key=True)
				username = db.Column(db.String(80), unique=True)
				email = db.Column(db.String(120), unique=True)

				def __init__(self, username, email):
					self.username = username
					self.email = email

				def __repr__(self):
					return '<User %r>' % self.username
            ```

        2. Lets take the rest of the course just to take a look at this.
            1. Perform the db creation step.
            2. Continue typing the commands in the howto.
        
        3. Possible Class Extension 
            1. Get this code integrated into our basic app!  
            2. Too long for today.

### Summary
We just implemented a standard web application using what Django calls
the Model-Template-View (MTV) pattern.
Django is designed around this concept,
and makes a number of decisions about your application
to make it easier to develop.

As we saw, Flask required us to pick our own dependencies.
This is nice when building lightweight applications,
or when the MTV pattern isn't so relevant to your design.

A good heuristic for deciding between Flask and Django might be,
"Am I designing an application that users should be able to log in to?"
If so, Django will help you create such an application quickly
without having to reinvent the wheels of user data modeling,
authentication, etc.
If not, give Flask a spin!
