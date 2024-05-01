# ---- LIBRARIES ----
from flask import Flask # Import Flask, a lightweight web framework for creating web applications.
from threading import Thread # Import Thread, which enables concurrent execution of code by creating separate threads.

# Create a Flask object named, "app".
app = Flask('') # This creates a Flask object named, "app" which will handle incoming HTTP requests and route them appropriately.

# Create the home page by calling the route() function, which is built into the Flask object.
@app.route('/') # This is a decorator which defines the route for the root URL ("/"). When a user accesses the root of the URL, the home() function is called.
def home():
    return "Hello. I am alive!"

# Create a function to run the Flask app.
def run():
  app.run(host='0.0.0.0',port=8080) # This comand runs the Flask development server, allowing the app to listen for incoming requests.

# Create a function to create separate threads for running the Flask app.
def keep_alive():
    t = Thread(target=run) # Create a new Thread object named, "t".
    t.start() # Run the start() function, which is built into the Thread object, against the newly created thread, "t".