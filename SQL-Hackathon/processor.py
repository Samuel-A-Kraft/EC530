import time
import numpy as np
from datetime import datetime

def process_task(task):
    a, b = task
    start_time = time.time()
    result = np.matmul(a, b)
    end_time = time.time()

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "shape": f"{a.shape} x {b.shape}",
        "duration": round(end_time - start_time, 4)
    }
