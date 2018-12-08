from operator import itemgetter
def main():

    with open("puz1.txt") as f:
        puz1file = f.readlines()

    records = []
    for line in puz1file:
        time, tmp = line.split("]")
        time = time[1:]
        tmp = tmp[1:-1]
        date, time = time.split(" ")
        date = date.split("-")
        date = date[1:]
        month, day = date
        time = time.split(":")
        hour, min = time
        if tmp[0] == "f":
            msg = tmp[0]
        elif tmp[0] == "w":
            msg = tmp[0]
        elif tmp[0] == "G":
            msg = tmp.split("#")
            msg = msg[1]
            msg = msg.split(" ")
            msg = msg[0]
        records.append((int(month), int(day), int(hour), int(min), msg))

    records = sorted(records, key=itemgetter(0, 1, 2, 3))
    guards = []
    changes = []
    for i_r, r in enumerate(records, 0):
        if not(r[4] == "f") and not(r[4] == "w"):
            changes.append(i_r)
            duplicate = False
            for g in guards:
                if r[4] == g:
                    duplicate = True
            if not(duplicate):
                guards.append((r[4],[]))

    shifts = []
    """Loop all changes"""
    for i_c, c in enumerate(changes, 0):
        shift = []
        """Not the last guard change"""
        if i_c < (len(changes)-1):
            for r in records[c:changes[i_c+1]]:
                shift.append(r)
        else:
            for r in records[c:]:
                shift.append(r)
        if len(shift) > 1:
            shifts.append(shift)

    breakTotals = []
    for shift in shifts:
        sleeps = []
        sleeps.append(int(shift[0][4]))
        for i in range(1, len(shift)-1, 2):
            min = shift[i][3]
            cmin = shift[i+1][3]
            if cmin < min:
                mindif = (60-min)+cmin
            else:
                mindif = cmin-min

            hour = shift[i][2]
            chour = shift[i+1][2]
            if chour < hour:
                hourdif = (24-hour)+chour
            else:
                hourdif = chour-hour

            day = shift[i][1]
            cday = shift[i+1][1]
            if cday < day:
                if shift[0] == 9 or shift[0] == 4 or shift[0] == 6 or shift[0] == 11:
                    daydif = (30-day)+cday
                else:
                    daydif = (31-day)+cday
            else:
                daydif = cday-day

            month = shift[i][0]
            cmonth = shift[i+1][0]
            monthdif = cmonth-month
            mins = min
            mine = cmin
            sleeps.append((mins, mine))
        breakTotals.append(sleeps)

    for i_b, b in enumerate(breakTotals, 0):
        for comp in breakTotals[i_b+1:]:
            if b[0] == comp[0]:
                for i in comp[1:]:
                    b.append(i)
                breakTotals.remove(comp)

    biggestMin = []
    for b in breakTotals:
        sleptMins = []
        totalSleep = 0
        for s,e in b[1:]:
            for min in range(s, e, 1):
                sleptMins.append(min)
                totalSleep = totalSleep + (e-s)
        winningMin = [0, 0]
        for s in sleptMins:
            if sleptMins.count(s) > winningMin[1]:
                winningMin = (s, sleptMins.count(s))
        biggestMin.append((b[0], winningMin, totalSleep))

    winner = [0, (0, 0), 0]
    for b in biggestMin:
        if b[1][1] > winner[1][1]:
            winner = b

    print winner
    print (winner[0] * winner[1][0])