from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/login')
def login():
    return(render_template('login.html'))


@app.route('/user_home', methods=['POST'])
def user_home():
    username = request.form['username']
    return(render_template('home.html', username=username))


if __name__ == '__main__':
    app.run(debug=True)