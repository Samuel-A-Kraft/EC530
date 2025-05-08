import time
import argparse
import numpy as np
from queue_threaded import ThreadedQueueProcessor
from queue_multiproc import ProcessQueueProcessor
from config import QUEUE_SIZE, REQUEST_COUNT, DELAY, MATRIX_SIZE

def generate_matrix(size):
    return np.random.rand(size, size)

def simulate_requests(processor):
    for i in range(REQUEST_COUNT):
        a = generate_matrix(MATRIX_SIZE)
        b = generate_matrix(MATRIX_SIZE)
        processor.add_task((a, b))
        time.sleep(DELAY)
    processor.wait_completion()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Concurrent Matrix Job Processor")
    parser.add_argument("--mode", choices=["thread", "process"], default="thread", help="Concurrency mode to use")
    args = parser.parse_args()

    print(f"Starting job processor in {args.mode} mode...")
    processor = ThreadedQueueProcessor(QUEUE_SIZE) if args.mode == "thread" else ProcessQueueProcessor(QUEUE_SIZE)

    processor.start()
    simulate_requests(processor)
    processor.stop()
    print("All jobs completed and stored in the database.")
