import time

import httpx

url = "https://google.com"
start = time.perf_counter()

try:
    response = httpx.get(url, follow_redirects=True)
except httpx.RequestError as exc:
    print(f"{url} -> DOWN ({type(exc).__name__}): {exc}")
else:
    elapsed_ms = (time.perf_counter() - start) * 1000 
    print(f"{url} -> {response.status_code} in {elapsed_ms:.0f} ms")


