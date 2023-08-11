from collections import deque

# deque to create a queue with capacity


custom_queue = deque(maxlen=3)
print(custom_queue)

custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)
custom_queue.append(4)

print(custom_queue)  # deque([2, 3, 4], maxlen=3)
print(custom_queue.popleft())

print(custom_queue)  # deque([3, 4], maxlen=3)
custom_queue.clear()
print(custom_queue)
