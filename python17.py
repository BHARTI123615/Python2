# 📂 One Code for DS (Python)
# Demonstrates List, Stack, Queue, Dictionary, Set

from collections import deque

def ds_demo():
    # 1. List (Dynamic Array)
    arr = [10, 20, 30]
    arr.append(40)
    print("List:", arr)

    # 2. Stack (LIFO)
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("Stack (before pop):", stack)
    stack.pop()
    print("Stack (after pop):", stack)

    # 3. Queue (FIFO)
    queue = deque()
    queue.append("A")
    queue.append("B")
    queue.append("C")
    print("Queue (before popleft):", queue)
    queue.popleft()
    print("Queue (after popleft):", queue)

    # 4. Dictionary (Key-Value Map)
    student = {"name": "Bharti", "course": "CSE", "year": 3}
    print("Dictionary:", student)
    print("Access by key:", student["course"])

    # 5. Set (Unique Elements)
    s = {1, 2, 2, 3, 4}
    print("Set (unique values):", s)

if __name__ == "__main__":
    ds_demo()
