class MeetingRoom:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x.start)
    rooms = [intervals[0]]

    for i in range(1, len(intervals)):
        for j in range(len(rooms)):
            if intervals[i].start >= rooms[j].end:
                rooms[j] = intervals[i]
                break
        else:
            rooms.append(intervals[i])

    return len(rooms)

def main():
    intervals = [MeetingRoom(1, 4), MeetingRoom(2, 5), MeetingRoom(7, 9)]
    print("Minimum number of meeting rooms required: " + str(meeting_rooms(intervals)))

main()