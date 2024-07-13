import sys
import math

def read_circle_info(file_path): # данные Т центра и радиус из файла
    with open(file_path, 'r') as file:
        center = list(map(float, file.readline().strip().split()))
        radius = float(file.readline().strip())
    # print(center, radius) чек
    return center, radius

def read_points_info(file_path): # данные для поикска точки
    with open(file_path, 'r') as file:
        points = [list(map(float, line.strip().split())) for line in file][:100]
    # print(points) чек
    return points

def check_position(center, radius, point):
    x_center, y_center = center
    x_point, y_point = point
    radius_kuadr = radius ** 2
    dist_kuadr = (x_point - x_center) ** 2 + (y_point - y_center) ** 2 # чек

    if dist_kuadr == radius_kuadr:
        return 0
    elif dist_kuadr < radius_kuadr:
        return 1
    else:
        return 2

if __name__ == "__main__":
    circul_data = sys.argv[1] # первый фаил - для данных круга
    points_data = sys.argv[2] # второй фаил - для данных точек

    center, radius = read_circle_info(circul_data)
    points = read_points_info(points_data)

    for point in points: # для каждой точки
        position = check_position(center, radius , point)
        print(position)