from flask import Flask, render_template
from settings import DEBUG


app = Flask(__name__)
app.debug = DEBUG


@app.route('/', methods=['GET'])
def index():
    #return render_template('index.html')
    return 'hello, Heroku.'


if __name__ == '__main__':
    app.run()