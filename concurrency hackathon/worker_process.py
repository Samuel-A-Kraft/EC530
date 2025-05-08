from multiprocessing import Process, Queue
from covid_client import fetch_covid_data

def process_worker(shared_queue: Queue):
    while True:
        country = shared_queue.get()
        if country is None:
            break
        result = fetch_covid_data(country)
        print("Processed Result:", result)

def start_processes(count: int, shared_queue: Queue):
    processes = []
    for _ in range(count):
        p = Process(target=process_worker, args=(shared_queue,), daemon=True)
        p.start()
        processes.append(p)
    return processes