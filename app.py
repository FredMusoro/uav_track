from flask import Flask, render_template
from funcs import read_track_data

app = Flask(__name__)

@app.route('/')
def track():
    points = read_track_data()
    lat_lon = [[point[1], point[2]] for point in points]
    return render_template('index.html', lat_lon=lat_lon)

if __name__ == '__main__':
    app.run(debug=True)