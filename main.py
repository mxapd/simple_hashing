import matplotlib.pyplot as pyplot


def uniformity_test():
    filename = 'Uniformity_test.txt'

    rows = set(load_file(filename))
    hashes = simple_hash(rows)

    plot_histogram(hashes)
    for row, hash_value in zip(rows, hashes):
        print(f"Line: {row} => Hash: {hash_value}")


def avalanche_test():
    filename = 'Avalanche_test.txt'

    rows = load_file(filename)
    hashes = simple_hash(rows)

    diffs = []
    for i in range(len(hashes)-1):
        diffs.append(calculate_bit_diff(hashes[i], hashes[i+1]))

    zerocounter = 0
    for diff in diffs:
        if diff == 0:
            zerocounter += 1

    print(f'probability of no change: {zerocounter/len(diffs)}')


def calculate_bit_diff(original, modified):
    original_bits = bin(original)[2:]
    modified_bits = bin(modified)[2:]
    diff = 0

    for og, mod in zip(original_bits, modified_bits):
        if og != mod:
            diff += 1
    return diff


def load_file(filename):
    with open(filename, 'r') as file:
        rows = []
        for row in file:
            rows.append(row)
    return rows


def simple_hash(rows):
    hashes = []
    for row in rows:
        hashvalue = 0
        for char in row:
            hashvalue += (hashvalue * 35742549198872617291353508656626642567) ^ ord(char)
        hashvalue = hashvalue % 256
        hashes.append(hashvalue)

    return hashes


def plot_histogram(hashes):
    pyplot.figure(figsize=(10, 5))
    pyplot.hist(hashes, bins=range(257), color='blue', alpha=0.7, edgecolor='black')
    pyplot.xlabel("Hash Value")
    pyplot.ylabel("Frequency")
    pyplot.title("Uniformity Test: Distribution of Hash Values")
    pyplot.show()


print('''
What test would you like to run?

[1] Uniformity
[2] Avalance
''')

match input():
    case '1':
        uniformity_test()
    case '2':
        avalanche_test()
