from copy import copy
from functools import cmp_to_key
from math import sqrt

def mat_det_2x2(a, b, c):
    det = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    return det

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def graham_algorithm(Q):
    n = len(Q)
    if n < 3:
        return Q

    S = copy(Q)
    P = S[0]
    
    for i in range(1, n):
        if S[i][1] < P[1]:
            P = S[i]
        elif S[i][1] == P[1]:
            if S[i][0] < P[0]:
                P = S[i]
    
    S.remove(P)

    def cmp(p1, p2):
        det = mat_det_2x2(P, p2, p1)

        if det == 0:
            return distance(P, p1) - distance(P, p2)
        else:
            return det

    S.sort(key=cmp_to_key(cmp))
    S.insert(0, P)

    T = [P]
    for i in range(n - 2):
        if mat_det_2x2(S[i], S[i + 1], S[i + 2]) != 0:
            T.append(S[i + 1])
    
    T.append(S[-1])
    if len(T) <= 3:
        return T

    points = []
    points.append(T[0])
    points.append(T[1])
    points.append(T[2])

    ptr = 3
    while ptr < len(T):
        det = mat_det_2x2(points[-2], points[-1], T[ptr])

        if det > 0:
            points.append(T[ptr])
            ptr += 1
        else:
            points.pop()
            
            if det == 0:
                points.append(T[ptr])
                ptr += 1
    
    return points
