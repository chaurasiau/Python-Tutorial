from celery_config import app


@app.task
def add(a, b):
    print(f"Sum of {a and b}is {a+b}")
    return a + b
