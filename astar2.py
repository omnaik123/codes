from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        # Manhattan distance heuristic
        cost = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    cost += abs(i - goal_i) + abs(j - goal_j)
        return cost + self.depth

    def get_children(self):
        children = []
        zero_i, zero_j = next((i, j) for i, row in enumerate(self.state) for j, val in enumerate(row) if val == 0)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for di, dj in moves:
            new_i, new_j = zero_i + di, zero_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_i][zero_j] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0
                children.append(PuzzleNode(new_state, parent=self, action=(di, dj), depth=self.depth + 1))
        return children

def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    initial_node.cost = initial_node.calculate_cost()
    frontier = PriorityQueue()
    frontier.put(initial_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_node)
        explored.add(tuple(map(tuple, current_node.state)))

        for child in current_node.get_children():
            if tuple(map(tuple, child.state)) not in explored:
                child.cost = child.calculate_cost()
                frontier.put(child)
    
    return None

def print_solution(solution):
    if solution:
        for node in solution:
            for row in node.state:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    initial_state = []
    print("Enter the initial state of the puzzle (one row at a time, separate numbers with spaces):")
    for i in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)
    solution = a_star(initial_state)
    print_solution(solution)
