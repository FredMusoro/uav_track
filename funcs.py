import json


def read_track_data(file='track.json'):
    with open(file, 'r') as f:
        data = f.read()
        parsed_data = json.loads(data)
        route_points = parsed_data['route_points']
        return route_points
