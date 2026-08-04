class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def merge(intervalsA, intervalsB):
    result = []
    i, j = 0, 0

    while i < len(intervalsA) and j < len(intervalsB):
        AOver = intervalsA[i][0] >= intervalsB[j][0] and intervalsA[i][0] <= intervalsB[j][1]
        Bover = intervalsB[j][0] >= intervalsA[i][0] and intervalsB[j][0] <= intervalsA[i][1]
        if AOver or Bover:
           result.append([max(intervalsA[i][0], intervalsB[j][0]), min(intervalsA[i][1], intervalsB[j][1])])

        if intervalsA[i][1] < intervalsB[j][1]:
            i += 1
        else:
            j += 1
    return result

def main():
    intervalsA = [[1, 3], [5, 6], [7, 9]]
    intervalsB = [[2, 3], [5, 7]]
    print("Merged intervals: " + str(merge(intervalsA, intervalsB)))

main()