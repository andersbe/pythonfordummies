import time


def compute(x):
    response = expensive_api_call()
    return response +x
def expensive_api_call():
    time.sleep(1000)
    return 123