from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_capacity):
    visited = set()
    queue = deque([(0, 0, [])])
    while queue:
        current_state = queue.popleft()
        a, b, steps = current_state
        if a == target_capacity or b == target_capacity:
            return steps + [(a, b)]
        if current_state[:2] in visited:
            continue
        visited.add(current_state[:2])
        # Fill jug 1
        if a < jug1_capacity:
            queue.append((jug1_capacity, b, steps + [(a, b)]))
        # Fill jug 2
        if b < jug2_capacity:
            queue.append((a, jug2_capacity, steps + [(a, b)]))
        # Empty jug 1
        if a > 0:
            queue.append((0, b, steps + [(a, b)]))
        # Empty jug 2
        if b > 0:
            queue.append((a, 0, steps + [(a, b)]))
        # Pour from jug 1 to jug 2
        pour_amount = min(a, jug2_capacity - b)
        if pour_amount > 0:
            queue.append((a - pour_amount, b + pour_amount, steps + [(a, b)]))
        # Pour from jug 2 to jug 1
        pour_amount = min(jug1_capacity - a, b)
        if pour_amount > 0:
            queue.append((a + pour_amount, b - pour_amount, steps + [(a, b)]))
    return None
def main():
    jug1_capacity = int(input("Enter the capacity of jug 1: "))
    jug2_capacity = int(input("Enter the capacity of jug 2: "))
    target_capacity = int(input("Enter the target capacity: "))
    result = water_jug_problem(jug1_capacity, jug2_capacity, target_capacity)
    if result:
        print("Solution:")
        for step in result:
            print(f"jug1: {step[0]} jug2: {step[1]}")
    else:
        print("No solution found.")
if _name_ == "_main_":
    main()
