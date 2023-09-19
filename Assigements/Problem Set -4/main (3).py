from collections import deque

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Define the possible moves (Up, Down, Left, Right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (row_change, col_change)

def create(initial_state, level):
    def is_valid_move(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def apply_move(state, x, y, new_x, new_y):
        new_state = [list(row) for row in state]
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state

    def print_state(state):
        for row in state:
            print(" ".join(map(str, row)))
        print()

    initial_state = [list(row) for row in initial_state]

    visited = set()
    queue = deque([(initial_state, 0)])

    while queue:
        current_state, current_level = queue.popleft()

        if current_level > level:
            break

        if current_state == goal_state:
            print("Goal state reached at level", current_level)
            print_state(current_state)
            break

        print("Level", current_level)
        print_state(current_state)
        visited.add(tuple(tuple(row) for row in current_state))

        for dx, dy in moves:
            x, y = None, None
            for i in range(3):
                for j in range(3):
                    if current_state[i][j] == 0:
                        x, y = i, j
                        break

            new_x, new_y = x + dx, y + dy

            if is_valid_move(new_x, new_y):
                new_state = apply_move(current_state, x, y, new_x, new_y)
                new_state_tuple = tuple(tuple(row) for row in new_state)
                if new_state_tuple not in visited:
                    queue.append((new_state, current_level + 1))

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

level = 20  # You can adjust the level as needed
create(initial_state, level)
