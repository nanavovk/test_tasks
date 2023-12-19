import argparse
import math

parser = argparse.ArgumentParser(description='Points on circle')
parser.add_argument('circle_characteristics_path', type=str, help='path to the file with characteristics of circle')
parser.add_argument('points_coord_path', type=str, help='path to the file with points coordinates')
args = parser.parse_args()

with open(args.circle_characteristics_path, 'r') as file:
    circle_chars = [line.strip() for line in file.readlines()]

with open(args.points_coord_path, 'r') as file1:
    points_coords = [line.strip() for line in file1.readlines()]

circle_rad = int(circle_chars[1])
circle_x = int(circle_chars[0][0])
circle_y = int(circle_chars[0][2])

curr_x = 0
curr_y = 0
dist = 0

for i in range(len(points_coords)):
    curr_x = int(points_coords[i][0])
    curr_y = int(points_coords[i][2])
    dist = math.sqrt((curr_x - circle_x) ** 2 + (curr_y - circle_y) ** 2)

    if dist == circle_rad:
        print(0)
    elif dist > circle_rad:
        print(2)
    elif dist < circle_rad:
        print(1)



