import numpy as np

def run():
    inputfile = open('d1input.txt', 'r')
    Lines = inputfile.readlines()

    array = np.array([])

    currentCount = 0
    for line in Lines:
        if line == "\n":
            array = np.append(array, currentCount)
            currentCount = 0
        else:
            currentCount += int(line)

    array = np.sort(array)[::-1]
    # part 1 answer
    print(array[0])

    # part 2 answer
    print(array[0] + array[1] + array[2])


if __name__ == '__main__':
    run()
