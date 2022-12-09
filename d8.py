forest = []


def run():
    inputfile = open('d8input.txt', 'r')
    Lines = inputfile.readlines()

    x = 0
    y = 0
    for row in Lines:
        forest.append([])
        y = 0
        for col in row.replace('\n', ''):
            forest[x].append(col)
            y += 1
        x += 1

    totalVisible = 0
    bestSoFar = 0
    for i in range(x):
        for j in range(y):
            if isEdge(i, j, x, y):
                totalVisible += 1
            else:
                result = checkIfVisible(i, j, x, y)
                if result[0]:
                    totalVisible += 1
                if result[1] > bestSoFar:
                    bestSoFar = result[1]

    print(totalVisible)
    print(bestSoFar)


def checkIfVisible(i, j, i_max, j_max):
    tree = forest[i][j]

    # check left
    left = True
    leftScore = 0
    x = j - 1
    while x >= 0:
        if tree <= forest[i][x]:
            left = False
            leftScore += 1
            break
        leftScore += 1
        x -= 1

    # check right
    right = True
    rightScore = 0
    x = j + 1
    while x < j_max:
        if tree <= forest[i][x]:
            right = False
            rightScore += 1
            break
        rightScore += 1
        x += 1

    # check up
    up = True
    upScore = 0
    x = i - 1
    while x >= 0:
        if tree <= forest[x][j]:
            up = False
            upScore += 1
            break
        x -= 1
        upScore += 1

    # check down
    down = True
    downScore = 0
    x = i + 1
    while x < i_max:
        if tree <= forest[x][j]:
            down = False
            downScore += 1
            break
        x += 1
        downScore += 1

    return left or right or up or down, (leftScore * rightScore * downScore * upScore)


def isEdge(i, j, i_max, j_max):
    if i == 0 or j == 0 or i == i_max - 1 or j == j_max - 1:
        return True
    return False


if __name__ == '__main__':
    run()
