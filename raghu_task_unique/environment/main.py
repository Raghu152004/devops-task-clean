import json

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
    with open(path, "w") as f:
        json.dump({"average": avg}, f)


def main():
    numbers = load_numbers("/app/input.json")
    avg = compute_avg(numbers)
    save_result("/app/result.json", avg)


if __name__ == "__main__":
    main()