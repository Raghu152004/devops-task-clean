import json
import os

def test_file_exists():
    assert os.path.exists("/app/result.json")

def test_average():
    with open("/app/result.json") as f:
        data = json.load(f)

    assert "average" in data
    assert abs(data["average"] - 13.33) < 0.1