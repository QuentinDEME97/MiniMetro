from models import *
from view import *
import random

def example_2_lines_3_stations():
    world = World(2223)
    s1 = world.add_station(60, 0, 0) # O
    s2 = world.add_station(5, 5, 1) # V
    s3 = world.add_station(95, 95, 2) # ^
    s4 = world.add_station(20, 80, 3) # <
    s5 = world.add_station(100, 0, 7)  # p
    # colors = ["#f0cb16", "#eb2827", "#1d347e", "#019ad1", "#008d3d"]
    ls = ['-', '--', '-.', ':']
    line_a = MetroLine("#f0cb16",'-')
    line_a.add_stations([s1, s2, s4])
    line_b = MetroLine("#1d347e",'--')
    line_b.add_stations([s1, s3])
    line_c = MetroLine("#019ad1",'-.')
    line_c.add_stations([s5, s1, s2, s4])
    world.add_line(line_a)
    world.add_line(line_b)
    world.add_line(line_c)
    view = View(world)
    print(world.w_lines)
    view.draw()

def main():
    world = World(2223)
    world.add_stations_random(5)
    view = View(world)
    view.draw()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("== Mini Metro ==")
    example_2_lines_3_stations()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
