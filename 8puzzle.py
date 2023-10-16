import heapq
goal_state = []
moves = [(0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left'), (-1, 0, 'up')]
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                h += abs(i - goal_row) + abs(j - goal_col)
    return h
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def astar(initial_state):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_set = set()
    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)
        if current_state == goal_state:
            return path
        closed_set.add(tuple(map(tuple, current_state)))
        zero_x, zero_y = 0, 0
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    zero_x, zero_y = i, j
        for move_x, move_y, move_dir in moves:
            new_x, new_y = zero_x + move_x, zero_y + move_y
            if is_valid(new_x, new_y):
                new_state = [list(row) for row in current_state]
                new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]
                if tuple(map(tuple, new_state)) not in closed_set:
                    h = heuristic(new_state)
                    new_path = path + [(new_state, move_dir)]
                    heapq.heappush(open_list, (g + 1 + h, g + 1, new_state, new_path))
   
    return None

initial_state = []
print("enter the start state")
for i in range(3):
    c=list(map(int,input().split()))
    initial_state.append(c)
print("enter the goal state")
for i in range(3):
    c=list(map(int,input().split()))
    goal_state.append(c)
path = astar(initial_state)
if path is not None:
    for step, (state, direction) in enumerate(path):
        print(f'Step {step+1}: Move the 0 to {direction}\n')
        for row in state:
            for i in row:
                print(i, end=" ")
            print('\n')
    print("Goal state is reached")
else:
    print('No solution found.')