from queue import Queue
from config import QUEUE_CAPACITY

job_queue = Queue(maxsize=QUEUE_CAPACITY)