
import queue as q


custom_queue = q.Queue(maxsize=3)
print(custom_queue.qsize())
custom_queue.put(1)
custom_queue.put(2)
custom_queue.put(3)
print(custom_queue.full())
print(custom_queue.get())
print(custom_queue.qsize())
