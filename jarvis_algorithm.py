from copy import copy
from math import sqrt

def mat_det_2x2(a, b, c):
    det = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    return det

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def jarvis_algorithm(Q):
    n = len(Q)

    if n < 3:
        return Q
    
    S = copy(Q)
    points = []
    left_idx = 0

    for i in range(1, n):
        if S[i][1] < S[left_idx][1]:
            left_idx = i
        elif S[i][1] == S[left_idx][1]:
            if S[i][0] < S[left_idx][0]:
                left_idx = i

    points.append(S[left_idx])
    a = left_idx
    b = 0
    if b == left_idx:
        b = 1

    while True:
        for i in range(n):
            det = mat_det_2x2(S[a], S[b], S[i])
            if det < 0 or (det == 0 and distance(S[a], S[i]) > distance(S[a], S[b])):
                b = i
        
        if b == left_idx:
            break
        
        points.append(S[b])
        a = b
        b = (b + 1) % n

    return points
