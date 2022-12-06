

def run():
    inputfile = open('d6input.txt', 'r')
    Lines = inputfile.readlines()

    line = Lines[0]

    index = getCode(4, line)

    # part 1
    print(index)

    index = getCode(14, line)
    # part 2
    print(index)


def getCode(size, line):
    index = 0
    buffer = []
    for c in line:
        index += 1
        buffer.append(c)
        if len(buffer) != size:
            continue
        if len(set(buffer)) == len(buffer):
            return index
        else:
            buffer.pop(0)
    return -1


if __name__ == '__main__':
    run()
