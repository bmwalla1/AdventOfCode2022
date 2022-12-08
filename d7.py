class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.childrenDirs = []
        self.files = []

    def getChildDir(self, name):
        for child in self.childrenDirs:
            if child.name == name:
                return child
        return None


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name


def run():
    inputfile = open('d7input.txt', 'r')
    Lines = inputfile.readlines()

    root = Directory("/", None)
    cwd = root

    for line in Lines:
        split = line.replace('\n', '').split(' ')
        if split[0] == '$' and split[1] == 'cd':
            if split[2] == '/':
                cwd = root
            elif split[2] == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.getChildDir(split[2])
        elif split[0] == '$' and split[1] == 'ls':
            # no op
            continue
        elif split[0] == 'dir':
            cwd.childrenDirs.append(Directory(split[1], cwd))
        else:
            cwd.files.append(File(int(split[0]), split[1]))

    part1 = []
    part2 = []
    rootSize = dfs(root, part1, part2)

    p1Total = 0
    for total in part1:
        p1Total += total

    # part 1
    print(p1Total)

    currentFree = 70000000 - rootSize
    needToDelete = 30000000 - currentFree

    p2Filtered = []
    for p2 in part2:
        if p2 >= needToDelete:
            p2Filtered.append(p2)

    print(min(p2Filtered))


def dfs(root, part1, part2):
    dirTotal = 0
    for child in root.childrenDirs:
        dirTotal += dfs(child, part1, part2)
    for file in root.files:
        dirTotal += file.size
    if dirTotal <= 100000:
        part1.append(dirTotal)
    part2.append(dirTotal)
    return dirTotal


if __name__ == '__main__':
    run()
