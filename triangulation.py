def mat_det_2x2(a, b, c):
    det = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    return det

def color_vertex(polygon):
    n = len(polygon)
    colors = [4] * n

    for i in range(n):
        a = polygon[(i - 1) % n]
        b = polygon[i]
        c = polygon[(i + 1) % n]
        det = mat_det_2x2(a, b, c)

        if a[1] < b[1] and c[1] < b[1]:
            if det > 0:
                colors[i] = 0
            else:
                colors[i] = 3
        elif a[1] > b[1] and c[1] > b[1]:
            if det > 0:
                colors[i] = 1
            else:
                colors[i] = 2

    return colors

def is_y_monotonic(polygon):
    n = len(polygon)
    min_y = polygon[0][1]
    min_y_idx = 0

    for i in range(1, n):
        if polygon[i][1] < min_y:
            min_y = polygon[i][1]
            min_y_idx = i
    
    rev = False
    for i in range(min_y_idx, n + min_y_idx - 1):
        if polygon[i % n][1] == polygon[(i + 1) % n][1]:
            return False
        
        if not rev and polygon[i % n][1] > polygon[(i + 1) % n][1]:
            rev = True
        elif rev and polygon[i % n][1] < polygon[(i + 1) % n][1]:
            return False

    return True

def triangulation(polygon):
    if not is_y_monotonic(polygon):
        return False

    n = len(polygon)
    colors = color_vertex(polygon)

    for i in range(n):
        if colors[i] == 0:
            up = i
        elif colors[i] == 1:
            down = i
    
    left_chain = []
    right_chain = []
    idx = up

    while idx != down:
        left_chain.append(polygon[idx])
        idx = (idx + 1) % n
    
    idx = (up - 1) % n
    while idx != down:
        right_chain.append(polygon[idx])
        idx = (idx - 1) % n
    right_chain.append(polygon[idx])

    points = []
    order = []
    chain = []
    idx_l = 0
    idx_r = 0
    while True:
        while idx_l < len(left_chain) and left_chain[idx_l][1] > right_chain[idx_r][1]:
            points.append(left_chain[idx_l])
            order.append((idx_l + up) % n)
            chain.append(0)
            idx_l += 1
        
        if idx_l == len(left_chain):
            while idx_r < len(right_chain):
                points.append(right_chain[idx_r])
                order.append((len(left_chain) - 1 + len(right_chain) - idx_r + up) % n)
                chain.append(1)
                idx_r += 1
            break

        while idx_r < len(right_chain) and left_chain[idx_l][1] <= right_chain[idx_r][1]:
            points.append(right_chain[idx_r])
            order.append((len(left_chain) - 1 + len(right_chain) - idx_r + up) % n)
            chain.append(1)
            idx_r += 1
        
        if idx_r == len(right_chain):
            while idx_l < len(left_chain):
                points.append(left_chain[idx_l])
                order.append((idx_l + up) % n)
                chain.append(0)
                idx_l += 1
            break

    stack = [0, 1]
    tri = []

    for i in range(2, n):
        if chain[i] != chain[stack[-1]]:
            for j in range(len(stack)):
                v = stack.pop()

                if order[i] != (order[v] + 1) % n and order[i] != (order[v] - 1) % n:
                    tri.append([order[i], order[v]])
            
            stack = [i - 1, i]
        else:
            for j in range(len(stack) - 1):
                v = stack.pop()
                
                if order[i] != (order[stack[-1]] + 1) % n and order[i] != (order[stack[-1]] - 1) % n:
                    if chain[i] == 0:
                        if mat_det_2x2(points[i], points[v], points[stack[-1]]) < 0:
                            tri.append([order[i], order[stack[-1]]])
                        else:
                            stack.append(v)
                            break
                    else:
                        if mat_det_2x2(points[i], points[v], points[stack[-1]]) > 0:
                            tri.append([order[i], order[stack[-1]]])
                        else:
                            stack.append(v)
                            break
            
            stack.append(i)
    
    return tri
