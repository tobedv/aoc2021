input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def read_input():
    with open("input.txt", "r") as f:
        input = f.readlines()
        return [i.rstrip("\n") for i in input]


def chunk(input):
    matrix = [[] for i in range(len(input[0]))]
    for i in input:
        for j, value in enumerate(i):
            matrix[j] += [int(value)]
    return matrix


def most_freq(matrix):
    val = []
    for m in matrix:
        if m.count(1) > m.count(0):
            val.append("1")
        else:
            val.append("0")
    return "".join(val)


def least_freq(matrix):
    val = []
    for m in matrix:
        if m.count(1) > m.count(0):
            val.append("0")
        else:
            val.append("1")
    return "".join(val)

m = chunk(read_input())
gamma = int(most_freq(m), 2)
epsilon = int(least_freq(m), 2)
print(gamma * epsilon)
