import multiprocessing
from processor import process_task
from db import store_result

class ProcessQueueProcessor:
    def __init__(self, queue_size):
        self.queue = multiprocessing.Queue(maxsize=queue_size)
        self.processes = []
        self.running = multiprocessing.Value('b', True)

    def worker(self, running_flag):
        while running_flag.value or not self.queue.empty():
            try:
                task = self.queue.get(timeout=1)
                result = process_task(task)
                store_result(mode="process", **result)
            except:
                continue

    def start(self, num_procs=4):
        for i in range(num_procs):
            p = multiprocessing.Process(target=self.worker, args=(self.running,), name=f"Process-{i}")
            p.start()
            self.processes.append(p)

    def add_task(self, task):
        self.queue.put(task)

    def wait_completion(self):
        self.queue.close()
        self.queue.join_thread()

    def stop(self):
        self.running.value = False
        for p in self.processes:
            p.join()
