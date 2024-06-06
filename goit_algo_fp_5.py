import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def update_colors(nodes, color_map):
    # Зміна кольору відповідно до порядку обходу
    n = len(nodes)
    colors = []
    for i, node in enumerate(nodes):
        # Генерування кольору: світліші кольори для пізніших вузлів
        intensity = 255 - int(255 * (i / n))
        color = f"#{intensity:02x}{intensity:02x}ff"  # відтінки синього
        colors.append(color)
        color_map[node] = color
    return colors

def bfs(tree, start_node):
    queue = deque([start_node])
    order = []
    color_map = {}
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order, color_map

def dfs(tree, start_node):
    stack = [start_node]
    order = []
    color_map = {}
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order, color_map

def draw_tree(tree, traversal_func, start_node):
    order, color_map = traversal_func(tree, start_node)
    update_colors(order, color_map)

    pos = {}
    labels = {}
    tree_graph = nx.DiGraph()
    def add_node(node, x=0, y=0, layer=1):
        if node:
            tree_graph.add_node(node.id, color=color_map.get(node, node.color), label=node.val)
            labels[node.id] = node.val
            pos[node.id] = (x, y)
            if node.left:
                tree_graph.add_edge(node.id, node.left.id)
                add_node(node.left, x - 1 / 2 ** layer, y - 1, layer + 1)
            if node.right:
                tree_graph.add_edge(node.id, node.right.id)
                add_node(node.right, x + 1 / 2 ** layer, y - 1, layer + 1)
    add_node(start_node)

    colors = [node[1]['color'] for node in tree_graph.nodes(data=True)]
    plt.figure(figsize=(10, 6))
    nx.draw(tree_graph, pos, labels=labels, arrows=False, node_color=colors, node_size=2000)
    plt.show()

# Створення бінарного дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення DFS і BFS
print("DFS traversal:")
draw_tree(root, dfs, root)
print("BFS traversal:")
draw_tree(root, bfs, root)
