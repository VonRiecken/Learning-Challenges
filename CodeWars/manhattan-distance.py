def manhattan_distance(pointA, pointB):
    horizontal_distance = abs(pointA[0] - pointB[0])
    vertical_distance = abs(pointA[1] - pointB[1])
    return horizontal_distance + vertical_distance
