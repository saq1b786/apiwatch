import httpx
import respx

from app.services.checker import check_url

URL = "https://example.com"


@respx.mock
def test_successful_response_is_up():
    respx.get(URL).mock(return_value=httpx.Response(200))

    result = check_url(URL)

    assert result.is_up is True
    assert result.status_code == 200
    assert result.error is None


@respx.mock
def test_server_error_is_down():
    respx.get(URL).mock(return_value=httpx.Response(500))

    result = check_url(URL)

    assert result.is_up is False
    assert result.status_code == 500
    assert result.error is None


@respx.mock
def test_connection_error_is_down():
    respx.get(URL).mock(side_effect=httpx.ConnectError)

    result = check_url(URL)

    assert result.is_up is False
    assert result.status_code is None
    assert result.error == "ConnectError"


@respx.mock
def test_timeout_is_down():
    respx.get(URL).mock(side_effect=httpx.ConnectTimeout)

    result = check_url(URL)
    assert result.is_up is False
    assert result.status_code is None
    assert result.error == "ConnectTimeout"
