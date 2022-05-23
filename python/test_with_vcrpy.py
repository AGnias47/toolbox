#!/usr/bin/env python3

import pytest
import requests
import vcr

def test_python_org():
    with vcr.use_cassette('fixtures/vcr_cassettes/python_org.yaml'):
        data = requests.get("https://www.python.org/")
        assert "Python" in data.text

if __name__ == "__main__":
    pytest.main()
