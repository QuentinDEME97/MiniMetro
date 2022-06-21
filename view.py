import matplotlib.pyplot as plt
import math
import numpy as np

class View:

    def __init__(self, world):
        self.title = "Mini Metro"
        self.world = world

    def draw_stations(self, stations):
        for station in stations:
            x, y  = station.position[0], station.position[1]
            # Draw stations
            plt.scatter(x, y, s=100, color='Black',zorder=2, marker=station.marker)
            #circle = plt.Circle((x + 3, y), radius=1, fc='y')
            #rectangle = plt.Rectangle((x + 4.5, y - 1), 2, 2, fc='y')
            #plt.gca().add_patch(rectangle)
            #plt.gca().add_patch(circle)
            plt.scatter(x + 3, y, s=50, color='y', zorder=2, marker=station.marker)
            print("Drawing Station and dot on {} {}".format(x,y))

    def draw_lines(self, lines):
        width = 2
        for line in lines:
            print("Line == \n",line)
            p = line.stations[0]
            for i in range(1,len(line.stations)):
                station = line.stations[i]
                p_x, p_y = p.position[0], p.position[1]
                s_x, s_y = station.position[0], station.position[1]
                plt.plot([p_x, s_x], [p_y, s_y], linestyle=line.style, color=line.color, zorder=1, linewidth=width)

                x = [p_x, s_x]
                y = [p_y, s_y]

                o = np.subtract(s_y, p_y)
                q = np.subtract(s_x, p_x)
                slope = o / q

                # (m,p) are the new coordinates to plot the parallel line
                m = s_x +1
                p = s_y +1

                axes = plt.gca()
                x_val = np.array(x)
                y_val = np.array(slope * (x_val - m) + p)
                print(x,y)
                if slope <= 0:
                    plt.plot(np.array(x), np.array(y)-0.7, color=line.color, zorder=1,linewidth=width)
                else:
                    plt.plot(np.array(x)-0.7, np.array(y), color=line.color, zorder=1,linewidth=width)
                plt.scatter((p_x+s_x)/2,(p_y+s_y)/2,color="Red")
                p = station

    def draw(self):
        plt.figure(figsize=((7,7)))
        plt.xlim((-10,110))
        plt.ylim((-10, 110))
        p = self.world.w_stations[0]
        i = 0
        self.draw_stations(self.world.w_stations)
        print(self.world.w_lines)
        self.draw_lines(self.world.w_lines)

        plt.show()