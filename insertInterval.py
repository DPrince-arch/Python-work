class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def insert(intervals, intervalInsert):
    merged = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i].end < intervalInsert.start:
        merged.append(intervals[i])
        i += 1  

    while i < len(intervals) and intervals[i].start <= intervalInsert.end:
        intervalInsert.start = min(intervalInsert.start, intervals[i].start)
        intervalInsert.end = max(intervalInsert.end, intervals[i].end)
        i += 1

    merged.append(intervalInsert)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged

       
    
if __name__ == "__main__":
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    new_interval = Interval(4, 6)
    result = insert(intervals, new_interval)
    print("Intervals after inserting the new interval: ", [f"[{i.start}, {i.end}]" for i in result])