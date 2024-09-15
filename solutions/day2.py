def part1():
    doubles = 0
    triples = 0
    with open("inputs/day2.txt", "r") as file:
        for line in file.read().splitlines():
            frequencies = {}
            for char in line:
                frequencies.update({char: frequencies.get(char, 0) + 1})
            for value in set(frequencies.values()):
                if value == 2:
                    doubles += 1
                elif value ==3:
                    triples += 1
        
        print(doubles * triples)
                 

def part2():
    ids = []
    with open("inputs/day2.txt", "r") as file:
        for line in file.read().splitlines():
            ids.append(line)
    
    for id1 in ids:
        for id2 in ids:
            indexes, count = getDiffChars(id1, id2)
            if count != 1:
                continue
            print(id1[:indexes[0]]+id1[indexes[0]+1:])
            return


def getDiffChars(str1, str2):
    if str1 == str2:
        return None, 0
    indexes = []
    index = 0
    for a,b in zip(str1, str2):
        if a != b:
            indexes.append(index)
        index += 1
    return indexes, len(indexes)
            

part1()
part2()
