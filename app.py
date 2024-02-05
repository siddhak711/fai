from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/chapters')
def chapters():
    return render_template('chapters.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/guest-lectures')
def guest_lectures():
    return render_template('guest-lectures.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)