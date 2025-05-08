import threading
from queue import Queue
from processor import process_task
from db import store_result

class ThreadedQueueProcessor:
    def __init__(self, queue_size):
        self.queue = Queue(maxsize=queue_size)
        self.threads = []
        self.running = True

    def worker(self):
        while self.running or not self.queue.empty():
            try:
                task = self.queue.get(timeout=1)
                result = process_task(task)
                store_result(mode="thread", **result)
                self.queue.task_done()
            except:
                continue

    def start(self, num_threads=4):
        for i in range(num_threads):
            t = threading.Thread(target=self.worker, name=f"Thread-{i}", daemon=True)
            t.start()
            self.threads.append(t)

    def add_task(self, task):
        self.queue.put(task)

    def wait_completion(self):
        self.queue.join()

    def stop(self):
        self.running = False
        for t in self.threads:
            t.join()
