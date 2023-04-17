from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    celebs = ['Tom Cruise', 'Beyonce', 'Brad Pitt', 'Angelina Jolie', 'Leonardo DiCaprio', 'Jennifer Aniston']
    celeb_left = random.choice(celebs)
    celeb_right = random.choice(celebs)
    return render_template('index.html', celeb_left=celeb_left, celeb_right=celeb_right)

if __name__ == '__main__':
    app.run(debug=True)
