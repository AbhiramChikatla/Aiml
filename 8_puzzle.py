import heapq


class Puzzle:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.n = int(len(start_state) ** 0.5)  # 3 for 8-puzzle

    def manhattan_distance(self, state):
        distance = 0
        for i in range(self.n * self.n):
            if state[i] != 0:
                goal_i, goal_j = divmod(self.goal_state.index(state[i]), self.n)
                curr_i, curr_j = divmod(i, self.n)
                distance += abs(goal_i - curr_i) + abs(goal_j - curr_j)
        return distance

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        i, j = divmod(zero_index, self.n)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                new_state = state[:]
                new_index = new_i * self.n + new_j
                new_state[zero_index], new_state[new_index] = new_state[new_index],new_state[zero_index],
                neighbors.append(new_state)

        return neighbors

    def solve(self):
        start_state = tuple(self.start_state)
        goal_state = tuple(self.goal_state)
        frontier = []
        heapq.heappush(
            frontier, (self.manhattan_distance(start_state), 0, start_state, [])
        )
        explored = set()

        while frontier:
            _, g, current_state, path = heapq.heappop(frontier)

            if current_state == goal_state:
                return path

            explored.add(current_state)

            for neighbor in self.get_neighbors(list(current_state)):
                neighbor_tuple = tuple(neighbor)
                if neighbor_tuple not in explored:
                    heapq.heappush(
                        frontier,
                        (
                            g + 1 + self.manhattan_distance(neighbor_tuple),
                            g + 1,
                            neighbor_tuple,
                            path + [neighbor_tuple],
                        ),
                    )

        return None


# Example Usage
start = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle = Puzzle(start, goal)
solution_path = puzzle.solve()

if solution_path:
    print("Solution Path:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")



# AIM:
# Implement an 8-puzzle solver using Heuristic search technique.

# DESCRIPTION:
# The 8-puzzle is a classic problem in artificial intelligence and search algorithms. It consists of a 3x3 grid with 8
# numbered tiles and one empty space. The goal is to rearrange the tiles to match a specific goal configuration using
# the least number of moves. The Heuristic search technique, specifically the A* (A-star) algorithm, is commonly
# used to solve this problem.
# A* search combines features of both uniform-cost search and pure heuristic search by minimizing the function:
# f(n)=g(n)+h(n) where:
#  g(n) is the cost to reach the current node.
#  h(n) is the heuristic estimate of the cost to reach the goal from the current node.
# Two common heuristics used in the 8-puzzle are:
# 1. Manhattan Distance: The sum of the absolute differences between the current position and the goal position
# of each tile.
# 2. Misplaced Tiles: The number of tiles not in their goal position.


# ALGORITHM:
# 1. Initialize the Start State:
#  Define the start state and goal state of the puzzle.
# 2. Heuristic Function:
#  Calculate the Manhattan Distance or the number of misplaced tiles for the current state.
# 3. Priority Queue (Min-Heap):
#  Use a priority queue to store nodes with their f(n) values. The node with the smallest f(n) is expanded
# first.
# 4. Expand Nodes:
#  For the current state, generate possible moves (up, down, left, right).
#  For each move, calculate the new state's f(n)=g(n)+h(n) and push it into the priority queue.
# 5. Check for Goal State:
#  If the current state matches the goal state, the puzzle is solved.
# 6. Repeat:
#  Repeat steps 4 and 5 until the goal state is found or the queue is empty.
# 7. Output Solution Path:
#  Once the goal state is reached, backtrack to retrieve the path and print the moves.
