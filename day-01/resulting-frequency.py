def resulting_frequency(fin):
    with open("input.txt") as fp:
        return sum(int(x) for x in fp)


def first_repeated_frequency(fin):
    frequency = 0
    seen = {frequency}

    with open(fin) as fp:
        frequency_changes = fp.read().splitlines()

    while True:
        for change in frequency_changes:
            frequency += int(change)
            if frequency in seen:
                return frequency
            else:
                seen.add(frequency)


if __name__ == "__main__":
    fin = "input.txt"
    print(resulting_frequency(fin))
    print(first_repeated_frequency(fin))
