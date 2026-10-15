from scripts.check_once import check_url


def test_unreachable_domain_is_down():
    result = check_url("https://this-site-does-not-exist-apiwatch.com")

    assert result.is_up is False
    assert result.status_code is None
    assert result.error == "ConnectError"


def test_missing_page_is_down():
    result = check_url("https://www.google.com/this-page-does-not-exist")

    assert result.is_up is False
    assert result.status_code == 404
    assert result.error is None
