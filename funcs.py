import json


def read_track_data(file='track.json'):
    with open(file, 'r') as f:
        data = f.read()
        parsed_data = json.loads(data)
        route_points = parsed_data['route_points']
        return route_points

def read_base_points(file='base_points.json'):
    with open(file, 'r') as f:
        data  = f.read()
        parsed_data = json.loads(data)
        start_points = parsed_data['start_points']
        land_points = parsed_data['land_points']
        return start_points, land_points
