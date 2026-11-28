path = "..."
with open (path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
count = 0
for line in lines[1:]:
    parts = line.split("//")
    name = parts[0]
    value = [float(x) for x in parts[1:]]
    avg = sum(value) / len(value)
    if all(v >= 10 for v in value) and avg >= 15:
        print(name)
        count += 1
print("nume", count)