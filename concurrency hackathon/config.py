import os

QUEUE_CAPACITY = int(os.getenv("QUEUE_CAPACITY", 20))
WORKER_COUNT = int(os.getenv("WORKER_COUNT", 4))