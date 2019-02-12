from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def track():
    map = {'track_map': 'This is track map'}
    return render_template('index.html', map=map)

if __name__ == '__main__':
    app.run(debug=True)