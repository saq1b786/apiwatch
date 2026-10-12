import time

import httpx

url = "https://www.google.com/this-page-does-not-exist"
start = time.perf_counter()


try:
    response = httpx.get(url, follow_redirects=True)
except httpx.RequestError as exc:
    print(f"{url} -> DOWN ({type(exc).__name__}): {exc}")
else:
    elapsed_ms = (time.perf_counter() - start) * 1000
    status = "UP" if response.is_success else "DOWN"
    print(f"{url} -> {status} ({response.status_code}) in {elapsed_ms:.0f} ms")



