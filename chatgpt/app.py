import os
from flask import Flask, render_template

import random
app = Flask(__name__)


@app.route('/')
def index():
    # List all the images in the static folder
    images = os.listdir('./static')
    # Select a random image from the list
    image = random.choice(images)
    return render_template('index.html', image=image)


if __name__ == '__main__':
    app.run()
