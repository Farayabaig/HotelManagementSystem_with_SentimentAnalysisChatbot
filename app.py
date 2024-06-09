from flask import Flask, jsonify, request, render_template,json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/gallery')
def gallery():
    with open('static/gallery.json', 'r') as f:
        images = json.load(f)
    return render_template('gallery.html', images=images)




if __name__ == '__main__':
    app.run(debug=True)
