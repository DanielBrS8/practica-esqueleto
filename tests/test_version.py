import re

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    assert re.fullmatch(r"\d+\.\d+", r.json()["version"])