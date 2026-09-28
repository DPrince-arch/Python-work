from __future__  import print_function

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def printInterval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    @staticmethod
    def merge(intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        merged = []
        current_start = intervals[0].start
        current_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start <= current_end:
                current_end = max(current_end, interval.end)
            else:
                merged.append(Interval(current_start, current_end))
                current_start = interval.start
                current_end = interval.end

        merged.append(Interval(current_start, current_end))
        return merged
    
if __name__ == "__main__":
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    print("Merged intervals: ", end='')
    merged = Interval.merge(intervals)
    for i in merged:
        i.printInterval()
        print(" ", end='')
    print()