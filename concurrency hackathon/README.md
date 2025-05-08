# COVID-19 Queue Processor

This system accepts country names via a FastAPI endpoint and queues them for processing. It uses either threads or processes to fetch COVID-19 statistics from the disease.sh API.

## Features
- Queues COVID data jobs by country name
- Uses either `threading` or `multiprocessing`
- Configurable queue size and worker count
- Includes load test script to simulate API flooding

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Config

Edit `config.py` to change queue size and number of workers.

## Load Testing

```bash
python stress_test.py
```

## Example Endpoint

```bash
curl -X POST http://localhost:8000/covid -H "Content-Type: application/json" -d '{"country": "Italy"}'
```

## Notes

- API used: https://disease.sh/v3/covid-19/countries/{country}
- No API key required