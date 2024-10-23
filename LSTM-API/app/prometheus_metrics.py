from prometheus_client import generate_latest, Counter, Histogram

REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latency of requests')
REQUEST_COUNT = Counter('request_count', 'Total count of requests')

@app.middleware("http")
async def add_prometheus_metrics(request: Request, call_next):
    with REQUEST_LATENCY.time():
        response = await call_next(request)
    REQUEST_COUNT.inc()
    return response

@app.get("/metrics")
def metrics():
    return generate_latest()
