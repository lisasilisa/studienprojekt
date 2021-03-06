def bezier_point_by_normal_vector(bezier_coords, start, end, position, side, hdc):

    x1 = position[start][0]
    y1 = position[start][1]
    x2 = position[end][0]
    y2 = position[end][1]

    gradient = (y2 - y1) / (x2 - x1)
    new_gradient = -(1 / gradient)

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    intercept = midpoint_y - (new_gradient * midpoint_x)

    if side == 1:
        bezier_coords[0].append(midpoint_x + (0.35 * hdc))
        bezier_coords[1].append(new_gradient * (midpoint_x + (0.35 * hdc)) + intercept)
    elif side == -1:
        bezier_coords[0].append(midpoint_x - (0.35 * hdc))
        bezier_coords[1].append(new_gradient * (midpoint_x - (0.35 * hdc)) + intercept)
