from flask import Flask, render_template

# Init app
app = Flask(__name__)

# Route
@app.route('/')
def index():
    return "Hello Tanmoy. Great job for creating a new flask app"

# Adding HTMl

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():

    objective = 'Objective is to build a small and basic working flask app.'
    return render_template('about.html', objective = objective)

# Templating


if __name__ == '__main__':
    app.run(debug = True)