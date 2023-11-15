from copy import copy

def mat_det_2x2(a, b, c):
    det = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    return det

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
            if mat_det_2x2(S[a], S[b], S[i]) < 0:
                b = i
        
        if b == left_idx:
            break
        
        if len(points) > 1 and mat_det_2x2(points[-2], points[-1], S[b]) == 0:
            points.pop()
        
        points.append(S[b])
        a = b
        b = (b + 1) % n

    return points
