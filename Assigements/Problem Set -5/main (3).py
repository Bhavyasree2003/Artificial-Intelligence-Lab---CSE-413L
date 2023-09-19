from collections import deque

# Define the goal state and initial state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Example goal state
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]  # Example initial state

# Define a function to calculate the heuristic value (number of misplaced tiles)
def calculate_heuristic(state):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

# Define a function to generate new states
def generate_new_states(state):
    new_states = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    empty_row, empty_col = None, None
    
    # Find the position of the empty tile
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
    
    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]  # Create a deep copy of the current state
            # Move the empty tile in the specified direction
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            new_states.append(new_state)
    
    return new_states

# Define the Create function
def Create(initial_state, level):
    queue = deque([(initial_state, 0)])  # Initialize the queue with the initial state and its level
    visited = set()  # To keep track of visited states
    
    while queue:
        state, current_level = queue.popleft()
        
        if current_level > level:
            break
        
        # Calculate the heuristic value for the current state
        heuristic_value = calculate_heuristic(state)
        
        # Print the current state and its heuristic value
        print("Level:", current_level)
        for row in state:
            print(row)
        print("Heuristic Value:", heuristic_value)
        print()
        
        # Mark the current state as visited
        visited.add(tuple(map(tuple, state)))
        
        # Generate and enqueue new states
        for new_state in generate_new_states(state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, current_level + 1))

# Usage example
Create(initial_state, 2)  # Generate states up to level 2
