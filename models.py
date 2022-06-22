import random
from typing import List
from itertools import count

colors = ["#f0cb16", "#eb2827", "#1d347e", "#019ad1", "#008d3d"]


class World:

    def __init__(self, seed=None):
        self.w_stations = []
        self.w_lines = []
        self.w_trains = []
        random.seed(seed)
        self.markers = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
        # The network map will be a dict {<Lines, Stations>}

    def add_station_random(self):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        marker = self.markers[random.randint(0, len(self.markers))]
        self.w_stations.append(Station(x, y, marker))

    def add_stations_random(self, n):
        for i in range(n):
            self.add_station_random()

    def add_station(self, x, y, marker_index=None):
        if marker_index is None:
            index = random.randint(0, len(self.markers) - 1)
            print(index)
            marker = self.markers[index]
        else:
            marker = self.markers[marker_index]
        s = Station(x, y, marker)
        self.w_stations.append(s)
        return s

    def add_line(self, line):
        self.w_lines.append(line)


class Station:
    _ids = count(0)

    def __init__(self, x, y, marker):
        self.position = (x, y)
        self.marker = marker
        self.id = next(self._ids)

    def __repr__(self):
        return "{} : {}, {}".format(self.id, self.position, self.marker)


class MetroLine:

    def __init__(self, color, style):
        self.color = color
        self.stations = []
        self.style = style

    def add_stations(self, stations):
        for station in stations:
            self.stations.append(station)

    def __repr__(self):
        return "Line with {} station(s) ({})".format(len(self.stations), self.stations)


class LineSegment:
    start: Station = None
    end: Station = None

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.id = self.build_id()

    def build_id(self):
        min_id = min(self.start.id, self.end.id)
        max_id = max(self.start.id, self.end.id)
        return "{}_{}".format(min_id, max_id)


class Metro:
    current_segment: LineSegment = None
    wagons = [];

    def __init__(self):
        pass


class Wagon(Metro):
    metro: Metro = None

    def __init__(self):
        pass
