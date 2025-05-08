# Concurrent Matrix Job Processor

This project is a concurrency-focused Python application that simulates processing multiple matrix multiplication jobs using either multithreading or multiprocessing. It demonstrates queue-based task handling, performance logging, and use of a relational database.

## 📦 Features

- Choose between **threaded** and **multiprocess** execution (`--mode thread` or `--mode process`)
- Each job performs a matrix multiplication using NumPy
- Results are stored in an SQLite database including:
  - Timestamp
  - Job type (thread/process)
  - Matrix shape
  - Duration in seconds
- Fully configurable queue size, matrix size, delay between tasks, and job count

## 🔧 Configuration

All configuration is handled in `config.py`:
```python
MATRIX_SIZE = 100     # N x N matrix
REQUEST_COUNT = 50    # Number of jobs to run
DELAY = 0.1           # Time delay between submissions (in seconds)
QUEUE_SIZE = 10       # Queue max size
```

## 🚀 Run the App

Install dependencies:
```bash
pip install -r requirements.txt
```

Then run:
```bash
python main.py --mode thread      # or --mode process
```

## 🗃️ Database

Results are saved to `results.db` and can be viewed using any SQLite browser or with CLI tools.

## ✅ Requirements

- Python 3.8+
- NumPy
