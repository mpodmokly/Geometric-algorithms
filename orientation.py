def orientation(a, b, c):
    det = a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - c[0] * b[1] * b[0] * a[1] - a[0] * c[1]
    return det
