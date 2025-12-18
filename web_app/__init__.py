import os

if __name__ == "__main__" and __package__ is None:
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from app.rps import determine_winner, generate_random_choice

app = Flask(__name__)

if os.getenv("DEBUGPY", "0") == "1" and os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    import debugpy

    debugpy.listen(("127.0.0.1", int(os.getenv("DEBUGPY_PORT", "8080"))))
    if os.getenv("DEBUGPY_WAIT", "0") == "1":
        debugpy.wait_for_client()


# when someone visits the home page "/" in the browser,
# trigger this "home" function, and return / display some value
@app.route('/')
def home():
    #return "THIS IS THE HOME PAGE"
    return render_template("home.html") # pass in the name of a file that exists in the templates dir


# when someone visits "/about" in the browser, it will
# trigger this "about" function, and return / display some
@app.route('/about')
def about():
    #return "THIS IS THE ABOUT PAGE"
    return render_template("about.html")


@app.route('/results', methods=['POST'])
def results():
    # this is the data the user sent in a POST request when they
    # submitted the form
    print(dict(request.form)) # like a dictionary with a key of "user_choice"

    # Get the user's choice from the form data
    user_choice = request.form.get('user_choice')
    computer_choice = generate_random_choice()
    outcome = determine_winner(user_choice, computer_choice)

    return render_template("results.html",
        x=5,
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )


if __name__ == '__main__':

    app.run(debug=True)
