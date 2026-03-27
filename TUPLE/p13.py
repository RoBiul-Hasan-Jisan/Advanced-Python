t = (1, 2, 3, 4, 5)
n = 2  # Number of positions to rotate right


rotated_left = tuple(t[n:] + t[:n])
rotated_right = tuple(t[-n:] + t[:-n])