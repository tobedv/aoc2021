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


def split(input, i):
    o = []
    z = []
    for j in input:
        if int(j[i]) == 1:
            o.append(j)
        else:
            z.append(j)
    return o, z


def most_common(input, i=0):
    o, z = split(input, i)
    if len(o) >= len(z):
        return o
    return z


def least_common(input, i=0):
    o, z = split(input, i)
    if len(o) >= len(z):
        return z
    return o


def oxygen():
    r = input
    for i in range(len(input[0])):
        r = most_common(r, i)
        if len(r) == 1:
            break
    return r


def co2():
    r = input
    for i in range(len(input[0])):
        r = least_common(r, i)
        if len(r) == 1:
            break
    return r


input = read_input()
print(oxygen())
print(co2())


oxygen = int(oxygen()[0], 2)
co2 = int(co2()[0], 2)

print(oxygen * co2)
