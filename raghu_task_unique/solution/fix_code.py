import json

with open("/app/input.json") as f:
    data = json.load(f)

values = []

for v in data["values"]:
    try:
        values.append(float(v))
    except:
        continue

total = sum(values)
count = len(values)

average = total / count

with open("/app/result.json", "w") as f:
    json.dump({"average": average}, f)