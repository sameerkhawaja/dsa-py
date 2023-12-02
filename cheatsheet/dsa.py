from collections import deque

# stack
# use append to Push items to the end of the stack
# use pop to Pop items from the end of the stack
# LIFO
print("====Stack Demo====")
my_stack = []
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print(my_stack)
my_stack.pop()
print(my_stack)

# queue
# FIFO
print("====Queue Demo====")
my_queue = []
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print(my_queue)
print(f"Dequeueing value: {my_queue.pop(0)}")
print(f"Dequeueing value: {my_queue.pop(0)}")
print(f"Dequeueing value: {my_queue.pop(0)}")

# queue implemented with deque
my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print(my_queue)
print(f"Dequeueing value: {my_queue.popleft()}")
print(f"Dequeueing value: {my_queue.popleft()}")
print(f"Dequeueing value: {my_queue.popleft()}")
