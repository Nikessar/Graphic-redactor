import numpy as np
import matplotlib.pyplot as plt


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def resize(self, dx, dy):
        self.x2 += dx
        self.y2 += dy

    def rotated_points(self, angle):
        centre = [self.x1 + (self.x2 - self.x1) / 2, self.y1 + (self.y2 - self.y1) / 2]
        st_points = [[self.x1, self.y1], [self.x2, self.y2]]
        rot_points = []

        theta = np.radians(angle)
        for i in range(len(st_points)):
            x = (st_points[i][0] - centre[0]) * np.cos(theta) - (st_points[i][1] - centre[1]) * np.sin(theta)
            y = (st_points[i][0] - centre[0]) * np.sin(theta) + (st_points[i][1] - centre[1]) * np.cos(theta)
            rot_points.append([x + centre[0], y + centre[1]])
        return rot_points


class Square():
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side = side_length

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, new_side):
        self.side = new_side

    def start_points(self, x, y, side):
        p1 = (x, y)
        p2 = (x, y + side)
        p3 = (x + side, y + side)
        p4 = (x + side, y)
        return p1, p2, p3, p4, p1

    def rotated_points(self, angle):
        centre = [self.x + self.side / 2, self.y + self.side / 2]
        st_points = self.start_points(self.x, self.y, self.side)
        rot_points = []

        theta = np.radians(angle)
        for i in range(len(st_points)):
            x = (st_points[i][0] - centre[0]) * np.cos(theta) - (st_points[i][1] - centre[1]) * np.sin(theta)
            y = (st_points[i][0] - centre[0]) * np.sin(theta) + (st_points[i][1] - centre[1]) * np.cos(theta)
            rot_points.append([x + centre[0], y + centre[1]])
        return rot_points


class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def start_points(self, x, y, width, height):
        p1 = (x, y)
        p2 = (x, y + height)
        p3 = (x + width, y + height)
        p4 = (x + width, y)
        return p1, p2, p3, p4, p1

    def rotated_points(self, angle):
        centre = [self.x + self.width / 2, self.y + self.height / 2]
        st_points = self.start_points(self.x, self.y, self.width, self.height)
        rot_points = []

        theta = np.radians(angle)
        for i in range(len(st_points)):
            x = (st_points[i][0] - centre[0]) * np.cos(theta) - (st_points[i][1] - centre[1]) * np.sin(theta)
            y = (st_points[i][0] - centre[0]) * np.sin(theta) + (st_points[i][1] - centre[1]) * np.cos(theta)
            rot_points.append([x + centre[0], y + centre[1]])
        return rot_points


class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, new_radius):
        self.radius = new_radius



fig, ax = plt.subplots()

line = Line(1, 4, 3, 6)
ax.plot([line.x1, line.x2], [line.y1, line.y2], color='blue',linewidth = 3)

square = Square(1, 1, 2)
ax.add_artist(plt.Rectangle((square.x, square.y), width=square.side, height=square.side, edgecolor='red', facecolor='none', linewidth = 3))

rectangle = Rectangle(4, 0, 4, 2)
ax.add_artist(plt.Rectangle((rectangle.x, rectangle.y), width=rectangle.width, height=rectangle.height, edgecolor='green', facecolor='none', linewidth = 3))

circle = Circle(6, 5, 1)
ax.add_patch(plt.Circle((circle.x, circle.y), radius=circle.radius, edgecolor='purple', facecolor='none', linewidth = 3))

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
plt.grid(linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Создание')
plt.show()



fig, ax = plt.subplots()

line.move(0, 1)
ax.plot([line.x1, line.x2], [line.y1, line.y2], color='blue',linewidth = 3)

square.move(0, 1)
ax.add_artist(plt.Rectangle((square.x, square.y), width=square.side, height=square.side, edgecolor='red', facecolor='none', linewidth = 3))

rectangle.move(0, 1)
ax.add_artist(plt.Rectangle((rectangle.x, rectangle.y), width=rectangle.width, height=rectangle.height, edgecolor='green', facecolor='none', linewidth = 3))

circle.move(0, 1)
ax.add_patch(plt.Circle((circle.x, circle.y), radius=circle.radius, edgecolor='purple', facecolor='none', linewidth = 3))

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
plt.grid(linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Перемещение')
plt.show()



fig, ax = plt.subplots()

line.resize(1, 1)
ax.plot([line.x1, line.x2], [line.y1, line.y2], color='blue',linewidth = 3)

square.resize(1)
ax.add_artist(plt.Rectangle((square.x, square.y), width=square.side, height=square.side, edgecolor='red', facecolor='none', linewidth = 3))

rectangle.resize(3,2)
ax.add_artist(plt.Rectangle((rectangle.x, rectangle.y), width=rectangle.width, height=rectangle.height, edgecolor='green', facecolor='none', linewidth = 3))

circle.resize(2)
ax.add_patch(plt.Circle((circle.x, circle.y), radius=circle.radius, edgecolor='purple', facecolor='none', linewidth = 3))

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
plt.grid(linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Изменение размера')
plt.show()



fig, ax = plt.subplots()

ax.plot(*zip(*line.rotated_points(45)), color='blue',linewidth = 3)

ax.plot(*zip(*square.rotated_points(45)), color='red',linewidth = 3)

ax.plot(*zip(*rectangle.rotated_points(45)), color='green',linewidth = 3)

ax.add_patch(plt.Circle((circle.x, circle.y), radius=circle.radius, edgecolor='purple', facecolor='none', linewidth = 3))

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
plt.grid(linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Поворот')
plt.show()