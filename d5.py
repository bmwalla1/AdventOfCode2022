

p1_stack1 = ['S', 'C', 'V', 'N']
p1_stack2 = ['Z', 'M', 'J', 'H', 'N', 'S']
p1_stack3 = ['M', 'C', 'T', 'G', 'J', 'N', 'D']
p1_stack4 = ['T', 'D', 'F', 'J', 'W', 'R', 'M']
p1_stack5 = ['P', 'F', 'H']
p1_stack6 = ['C', 'T', 'Z', 'H', 'J']
p1_stack7 = ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z']
p1_stack8 = ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W']
p1_stack9 = ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']

p2_stack1 = ['S', 'C', 'V', 'N']
p2_stack2 = ['Z', 'M', 'J', 'H', 'N', 'S']
p2_stack3 = ['M', 'C', 'T', 'G', 'J', 'N', 'D']
p2_stack4 = ['T', 'D', 'F', 'J', 'W', 'R', 'M']
p2_stack5 = ['P', 'F', 'H']
p2_stack6 = ['C', 'T', 'Z', 'H', 'J']
p2_stack7 = ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z']
p2_stack8 = ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W']
p2_stack9 = ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']


def run():
    inputfile = open('d5input.txt', 'r')
    Lines = inputfile.readlines()

    for line in Lines:
        split = line.replace('\n', '').split(' ')
        numberToMove = int(split[1])
        stackFrom = int(split[3])
        stackTo = int(split[5])

        for x in range(numberToMove):
            getP1Stack(stackTo).append(getP1Stack(stackFrom).pop())

    # part 1
    print(p1_stack1[-1] + p1_stack2[-1] + p1_stack3[-1] + p1_stack4[-1] + p1_stack5[-1] + p1_stack6[-1] + p1_stack7[-1] + p1_stack8[-1] + p1_stack9[-1])

    for line in Lines:
        split = line.replace('\n', '').split(' ')
        numberToMove = int(split[1])
        stackFrom = int(split[3])
        stackTo = int(split[5])

        tempStack = []
        for x in range(numberToMove):
            tempStack.append(getP2Stack(stackFrom).pop())

        for x in range(numberToMove):
            getP2Stack(stackTo).append(tempStack.pop())

    # part 2
    print(p2_stack1[-1] + p2_stack2[-1] + p2_stack3[-1] + p2_stack4[-1] + p2_stack5[-1] + p2_stack6[-1] + p2_stack7[-1] + p2_stack8[-1] + p2_stack9[-1])


def getP1Stack(num):
    if num == 1:
        return p1_stack1
    if num == 2:
        return p1_stack2
    if num == 3:
        return p1_stack3
    if num == 4:
        return p1_stack4
    if num == 5:
        return p1_stack5
    if num == 6:
        return p1_stack6
    if num == 7:
        return p1_stack7
    if num == 8:
        return p1_stack8
    if num == 9:
        return p1_stack9


def getP2Stack(num):
    if num == 1:
        return p2_stack1
    if num == 2:
        return p2_stack2
    if num == 3:
        return p2_stack3
    if num == 4:
        return p2_stack4
    if num == 5:
        return p2_stack5
    if num == 6:
        return p2_stack6
    if num == 7:
        return p2_stack7
    if num == 8:
        return p2_stack8
    if num == 9:
        return p2_stack9


if __name__ == '__main__':
    run()
