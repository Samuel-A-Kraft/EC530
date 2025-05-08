import threading
from queue_manager import job_queue
from covid_client import fetch_covid_data

def worker_thread():
    while True:
        country = job_queue.get()
        if country is None:
            break
        result = fetch_covid_data(country)
        print("Threaded Result:", result)
        job_queue.task_done()

def start_threads(count: int):
    threads = []
    for _ in range(count):
        t = threading.Thread(target=worker_thread, daemon=True)
        t.start()
        threads.append(t)
    return threads