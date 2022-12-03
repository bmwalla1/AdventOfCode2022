from itertools import islice

def run():
    inputfile = open('d3input.txt', 'r')
    Lines = inputfile.readlines()

    sum = 0
    for line in Lines:
        n = len(line)
        compartment1 = line[0:n // 2]
        compartment2 = line[n // 2:]

        commonLetter = list(set(compartment1)&set(compartment2))

        sum += getLetterScore(commonLetter)

    # Part 1
    print(sum)

    sum = 0
    with open('d3input.txt', 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break

            item1 = next_n_lines[0].replace('\n', '')
            item2 = next_n_lines[1].replace('\n', '')
            item3 = next_n_lines[2].replace('\n', '')

            commonLetter = list(set(item1)&set(item2)&set(item3))

            sum += getLetterScore(commonLetter)

    # Part 2
    print(sum)


def getLetterScore(commonLetter):
    if commonLetter[0].isupper():
        return ord(commonLetter[0].lower()) - 96 + 26
    else:
        return ord(commonLetter[0].lower()) - 96


if __name__ == '__main__':
    run()
