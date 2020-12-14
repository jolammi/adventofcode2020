import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = [int(i.strip("\n")) for i in handle.readlines()]
    return data


def parse_adapters(data):
    one_jolt_diff = 0
    three_jolt_diff = 0
    current = 0
    while data:
        diff = min(data) - current
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        current = min(data)
        data.remove(current)
    return one_jolt_diff, three_jolt_diff + 1


if __name__ == "__main__":
    try:
        data = read_data()
        one_jolt, three_jolt = parse_adapters(data)
        # assert first_faulty == 177777905
        assert one_jolt*three_jolt == 2775
        print(f"One-jolt difference multiplied by three-jolt differences is {one_jolt*three_jolt}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
