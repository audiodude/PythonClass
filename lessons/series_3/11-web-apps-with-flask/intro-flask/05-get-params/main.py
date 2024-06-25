import datetime

import flask

app = flask.Flask(__name__)

@app.route('/goodbye')
def goodbye():
  return flask.render_template(
    'greeting.html',
    greeting='Goodbye!',
    time_value=datetime.datetime.now())

@app.route('/greet')
@app.route('/greet/<name>')
def greet_by_name(name=None):
  # If name isn't None, it means that Flask passed it
  # to our function, because it was part of the URL.
  #
  # Otherwise we got here by GET params, not /greet/Foo,
  # so we get the params from the GET args. Like a dict,
  # the default value is used if the param isn't present.
  if name is None:
    name = flask.request.args.get('name', 'World')
    
  greeting = f'Hello {name}!'
  return flask.render_template(
    'greeting.html',
    greeting=greeting,
    time_value='')

@app.route('/')
def index():
  return flask.render_template('index.html')