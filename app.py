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

@app.route('/image001')
def image001():
    return render_template('image001.html')

@app.route('/image002')
def image002():
    return render_template('image002.html')

if __name__ == '__main__':
    app.run(debug=True)