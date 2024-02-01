import pyrunstat


def test_version() -> None:
    assert pyrunstat.__version__ != "999"
