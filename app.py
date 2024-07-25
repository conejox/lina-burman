from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/worshops')
def workshops():
    return render_template('workshops.html')

if __name__ == '__main__':
    app.run(debug=True)