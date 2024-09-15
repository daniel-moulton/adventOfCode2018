def part1():
    with open('inputs/day1.txt') as f:
        data = f.read().strip()
        sum = 0
        for line in data.split('\n'):
            sum += int(line)
        print(sum)

def part2():
    with open('inputs/day1.txt') as f:
        data = f.read().strip()
        sum = 0
        set = {0}
        found = False
        while not found:
            for line in data.split('\n'):
                sum += int(line)
                if sum in set:
                    print(sum)
                    found = True
                    break
                set.add(sum)

part1()
part2()
