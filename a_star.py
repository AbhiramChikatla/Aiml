import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost estimate to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_algorithm(grid, start, goal):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Goal reached
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate neighbors (up, down, left, right)
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for new_position in neighbors:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # Check boundaries
            if (
                node_position[0] > (len(grid) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(grid[0]) - 1)
                or node_position[1] < 0
            ):
                continue

            # Check if it's an obstacle
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            neighbor = Node(node_position, current_node)

            if neighbor.position in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heapq.heappush(open_list, neighbor)

    return None  # No path found


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor.position == node.position and neighbor.g > node.g:
            return False
    return True


# Example grid (0 = open, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
]



start = (0, 0)
goal = (5, 5)
path = a_star_algorithm(grid, start, goal)
print("Path:", path)



# Implement A* algorithm on any problem.

# DESCRIPTION:
# The A* (A-star) algorithm is a popular pathfinding and graph traversal algorithm used to find the shortest path
# between two nodes in a weighted graph. It is widely used in various applications, including GPS navigation
# systems, video games, and AI systems. A* is an informed search algorithm, meaning it uses knowledge of the
# goal to make decisions that are likely to lead to the optimal path.
# The A* algorithm combines features of Dijkstra's algorithm and Greedy Best-First-Search. It uses a heuristic
# function to estimate the cost from a node to the goal, allowing it to prioritize paths that appear to be more
# promising.
# Problem Statement
# We will implement the A* algorithm to solve the problem of finding the shortest path in a grid. The grid will
# have obstacles, and the algorithm will need to navigate around these obstacles to find the shortest path from the
# start position to the goal.

# ALGORITHM:
# 1. Initialize:
#  Create an open list containing the start node. The open list keeps track of nodes that need to be
# evaluated.
#  Create a closed list, initially empty, to keep track of nodes that have already been evaluated.
# 2. Loop until the open list is empty:
# 1. Select the node with the lowest f(n) value (where f(n) = g(n) + h(n)) from the open list. Set this
# node as the current node.
# 2. If the current node is the goal, trace the path from the start node to the goal and return the path.
# 3. Move the current node to the closed list.
# 4. For each neighbor of the current node:
# 1. If the neighbor is in the closed list, skip it.
# 2. Calculate the tentative g score (the cost to reach this neighbor).
# 3. If the neighbor is not in the open list, add it and calculate the f(n) value. Set its parent to the
# current node.
# 4. If the neighbor is in the open list but the new g score is lower, update the neighbor's g and f
# values and change its parent to the current node.
# Return:
#  If the open list is empty and the goal has not been reached, return that no path exists.
