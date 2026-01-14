# ms_tags/tests/test_provider_contract.py
import subprocess
import time
from pact import Verifier


def test_verify_pacts():
    process = subprocess.Popen(["uvicorn", "ms-tags.main:app", "--port", "8001"])
    time.sleep(2)

    verifier = (
        Verifier(
            "ms-tags",
        )
        .add_transport(url="http://localhost:8001")
        .broker_source(
            "http://localhost:9292",
        )
    )

    result = verifier.verify()

    assert result 

    process.terminate()
