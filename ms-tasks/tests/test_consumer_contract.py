# ms_tasks/tests/test_consumer_contract.py
from pathlib import Path
from typing import Generator

import pytest
import requests
from pact import Pact


@pytest.fixture
def pact() -> Generator[Pact, None, None]:
    pact = Pact(
        consumer="ms-tasks",
        provider="ms-tags",
    ).with_specification("V4")

    yield pact

    pact.write_file(Path(__file__).parent / "pacts")


def test_get_tag_contract(pact: Pact):
    response_body = {"tag_id": "123"}

    (
        pact.upon_receiving("a tag request")
        .given("tag exists", id="123")
        .with_request("GET", "/tags/123")
        .will_respond_with(200)
        .with_body(response_body, content_type="application/json")
    )

    with pact.serve() as srv:
        response = requests.get(f"{srv.url}/tags/123")
        data = response.json()

        assert "tag_id" in data
        assert data["tag_id"] == "123"
