class Appointment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def can_attend_all_appointments(appointments):
    appointments.sort(key=lambda x: x.start)

    for i in range(1, len(appointments)):
        if appointments[i].start < appointments[i - 1].end:
            return False

    return True

def main():
    appointments = [Appointment(1, 4), Appointment(4, 5), Appointment(7, 9)]
    print("Can attend all appointments: " + str(can_attend_all_appointments(appointments)))

main()