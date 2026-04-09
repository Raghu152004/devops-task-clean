import json
import os
import subprocess

def run_app(data):
    # write input
    with open("/app/input.json", "w") as f:
        json.dump(data, f)

    # run app safely (will fail loudly if error)
    subprocess.run(["python3", "/app/main.py"], check=True)

    # ensure result file exists
    assert os.path.exists("/app/result.json")

    # read output
    with open("/app/result.json") as f:
        return json.load(f)


def test_file_exists():
    data = {"values": [1, 2, 3]}
    run_app(data)

    assert os.path.exists("/app/result.json")


def test_average():
    data = {"values": [10, 20, 10]}
    out = run_app(data)

    assert "average" in out
    assert abs(out["average"] - 13.33) < 0.1


def test_ignore_invalid():
    data = {"values": [10, "a", 20]}
    out = run_app(data)

    assert abs(out["average"] - 15.0) < 0.1


def test_empty_input():
    data = {"values": []}
    out = run_app(data)

    assert out["average"] == 0.0


def test_mixed_types():
    data = {"values": [10, "5", 15]}
    out = run_app(data)

    assert abs(out["average"] - 12.5) < 0.1


def test_multiple_values():
    data = {"values": [10, 20, 30]}
    out = run_app(data)

    assert abs(out["average"] - 20.0) < 0.1