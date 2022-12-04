

def run():
    inputfile = open('d4input.txt', 'r')
    Lines = inputfile.readlines()

    totalCompleteOverlap = 0
    totalOverlap = 0
    for line in Lines:
        elves = line.replace('\n','').split(',')
        e1min = int(elves[0].split('-')[0])
        e1max = int(elves[0].split('-')[1])
        e2min = int(elves[1].split('-')[0])
        e2max = int(elves[1].split('-')[1])

        e1range = range(e1min, e1max + 1)
        e2range = range(e2min, e2max + 1)
        if e2min in e1range and e2max in e1range:
            totalCompleteOverlap += 1
        elif e1min in e2range and e1max in e2range:
            totalCompleteOverlap += 1

        if e2min in e1range or e2max in e1range:
            totalOverlap += 1
        elif e1min in e2range or e1max in e2range:
            totalOverlap += 1

    # part1
    print(totalCompleteOverlap)

    # part2
    print(totalOverlap)




if __name__ == '__main__':
    run()
