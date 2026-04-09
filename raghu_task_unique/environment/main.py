import json
import os

def load_numbers(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except:
        return []

    values = data.get("values", [])

    nums = []
    for v in values:
        if isinstance(v, (int, float)):
            nums.append(v)

    return nums


def compute_avg(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def save_result(path, avg):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump({"average": avg}, f)


def main():
    input_path = "/app/input.json"

    if not os.path.exists(input_path):
        with open(input_path, "w") as f:
            json.dump({"values": []}, f)

    nums = load_numbers(input_path)
    avg = compute_avg(nums)
    save_result("/app/result.json", avg)


if __name__ == "__main__":
    main()