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

curr_x = 0
curr_y = 0
hypotenuse = 0

for i in range(len(points_coords)):
    curr_x = int(points_coords[i][0])
    curr_y = int(points_coords[i][2])
    hypotenuse = math.sqrt(curr_x ** 2 + curr_y ** 2)

    if hypotenuse < circle_rad:
        print(1)
    elif hypotenuse > circle_rad:
        print(2)
    else:
        print(0)
