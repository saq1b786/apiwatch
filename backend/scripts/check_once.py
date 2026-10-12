import time

from dataclasses import dataclass

import httpx

@dataclass
class CheckResult:
    url: str
    is_up: bool
    status_code: int | None
    latency_ms: float
    error: str | None

def check_url(url: str) -> CheckResult:

    start = time.perf_counter()

    try:
        response = httpx.get(url, follow_redirects=True)
    except httpx.RequestError as exc:
        latency_ms = (time.perf_counter() - start) * 1000
        return CheckResult(url=url, is_up=False, status_code=None, latency_ms=latency_ms, error=type(exc).__name__)
    else:
        latency_ms = (time.perf_counter() - start) * 1000
        return CheckResult(url=url, is_up=response.is_success, status_code=response.status_code, latency_ms=latency_ms, error=None)

result = check_url("https://this-site-does-not-exist-apiwatch.com")
print(result)


