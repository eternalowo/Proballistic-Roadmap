import Graph
from random import randint
from math import sqrt, inf

X_MAX_CRUTOI = 961
Y_MAX_CRUTOI = 720

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


class Ugolnic:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.point_min = (x1, y1)
        self.point_max = (x2, y2)
        self.points = [self.point_min,
                       self.point_max,
                       (self.point_min[0], self.point_max[1]),
                       (self.point_max[0], self.point_min[1])]

    def vnutri(self, x, y):
        if ((x >= self.x1) and (x <= self.x2)) and ((y >= self.y1) and (y <= self.y2)):
            return True
            # print("точка внутри прямоугольника")
        else:
            return False
            # print("снаружи")


def RandomSample():  # возвращает рандомные координаты точки
    x = randint(20, X_MAX_CRUTOI)
    y = randint(20, Y_MAX_CRUTOI)
    return x, y


def CollisionFree(x, y, obstacles):
    flag = True
    for obstacle in obstacles:
        res = cohen_sutherland_line_clip(x, y, obstacle.point_min, obstacle.point_max)
        if res[0]:
            flag = False
            break
    return flag


# -----------------------------------------------------------------------------------------------------------------
# Алгоритм для пересечения прямоугольников с отрезками

def compute_out_code(point, rect_min, rect_max):
    code = INSIDE
    if point[0] < rect_min[0]:
        code = code | LEFT
    elif point[0] > rect_max[0]:
        code = code | RIGHT
    if point[1] < rect_min[1]:
        code = code | BOTTOM
    elif point[1] > rect_max[1]:
        code = code | TOP
    return code


def cohen_sutherland_line_clip(segment_first, segment_second, rect_min, rect_max):
    out_code0 = compute_out_code(segment_first, rect_min, rect_max)
    out_code1 = compute_out_code(segment_second, rect_min, rect_max)
    segment_first = list(segment_first)
    segment_second = list(segment_second)
    collision = False

    while True:
        if not (out_code0 | out_code1):
            collision = True
            break
        elif out_code0 & out_code1:
            break
        else:
            if out_code1 > out_code0:
                outcode_out = out_code1
            else:
                outcode_out = out_code0
            if outcode_out & TOP:
                x = segment_first[0] + (segment_second[0] - segment_first[0]) * (rect_max[1] - segment_first[1]) / (
                        segment_second[1] - segment_first[1])
                y = rect_max[1]
            if outcode_out & BOTTOM:
                x = segment_first[0] + (segment_second[0] - segment_first[0]) * (rect_min[1] - segment_first[1]) / (
                        segment_second[1] - segment_first[1])
                y = rect_min[1]
            if outcode_out & RIGHT:
                y = segment_first[1] + (segment_second[1] - segment_first[1]) * (rect_max[0] - segment_first[0]) / (
                        segment_second[0] - segment_first[0])
                x = rect_max[0]
            if outcode_out & LEFT:
                y = segment_first[1] + (segment_second[1] - segment_first[1]) * (rect_min[0] - segment_first[0]) / (
                        segment_second[0] - segment_first[0])
                x = rect_min[0]
            if outcode_out == out_code0:
                segment_first[0] = x
                segment_first[1] = y
                out_code0 = compute_out_code(segment_first, rect_min, rect_max)
            else:
                segment_second[0] = x
                segment_second[1] = y
                out_code1 = compute_out_code(segment_second, rect_min, rect_max)
    return collision, list(map(round, segment_first)), list(map(round, segment_second))


# -----------------------------------------------------------------------------------------------------------------

def get_distance(first_point, second_point):
    return sqrt((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2)


def add_point(g, x, obstacles):
    weights = []
    verts = g.get_vertices()
    for vert in verts:
        weights.append(get_distance(x, vert))
    for i in range(len(verts)):
        ind = weights.index(min(weights))
        if CollisionFree(verts[ind], x, obstacles):
            g.add_edge(x, verts[ind])
            return True
        else:
            weights.remove(min(weights))
            verts.remove(verts[ind])
    return False


def Near(G, x, k):
    dist = []  # список всех весов
    result = []  # список к ближайших вершин
    vershini = G.get_vertices()
    if x in vershini:
        vershini.remove(x)
    for i in vershini:
        dist.append(get_distance(x, i))
    for i in range(k):
        ind = dist.index(min(dist))
        result.append(vershini[ind])
        dist.remove(min(dist))
        vershini.remove(vershini[ind])
    return result


def dijkstra_algorithm(g, start_node):
    unvisited_nodes = g.get_vertices()
    shortest_path = {}
    previous_nodes = {}
    for node in unvisited_nodes:
        shortest_path[node] = inf
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbours = g.get_adjacent(current_min_node)
        for neighbour in neighbours:
            tentative_value = shortest_path[current_min_node] + g.get_edge_weight(current_min_node, neighbour)
            if tentative_value < shortest_path[neighbour]:
                shortest_path[neighbour] = tentative_value
                previous_nodes[neighbour] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        if node not in previous_nodes:
            return [], ''
        node = previous_nodes[node]

    path.append(start_node)

    return path, shortest_path[target_node]


def PRM(N, k, Qinit, Qgoal, obstacles):
    main_flag = True
    for obst in obstacles:
        if obst.vnutri(*Qinit) or obst.vnutri(*Qgoal):
            main_flag = False
    G = Graph.Graph()  # пустой граф
    while len(G.get_vertices()) < N:
        Qrand = RandomSample()
        flag = True
        for obstacle in obstacles:
            if obstacle.vnutri(Qrand[0], Qrand[1]):
                flag = False
                break
        if flag:
            G.add_vertex(Qrand)
    for Q in G.get_vertices():
        Qnear = Near(G, Q, k)
        for Qn in Qnear:
            if CollisionFree(Q, Qn, obstacles):
                G.add_edge(Q, Qn)
    if (add_point(G, Qinit, obstacles) == False) or (add_point(G, Qgoal, obstacles) == False):
        main_flag = False
    if main_flag:
        add_point(G, Qinit, obstacles)
        add_point(G, Qgoal, obstacles)
        previous_nodes, shortest_path = dijkstra_algorithm(G, Qinit)
        for key, item in shortest_path:
            if item == inf:
                return G.edges, G.get_vertices(), [], ''
        result, message = print_result(previous_nodes, shortest_path, Qinit, Qgoal)
        return G.edges, G.get_vertices(), result, message
    return G.edges, G.get_vertices(), [], ''
