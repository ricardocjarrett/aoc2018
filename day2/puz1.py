def main():

    with open("puz1.txt") as f:
        puz1file = f.readlines()


    lines = []
    for line in puz1file:
        lines.append(line)

    twos = 0
    threes = 0

    for line in lines:
        twocheck = False
        threecheck = False
        for cha in line:
            if line.count(cha) == 2:
                twocheck = True
            if line.count(cha) == 3:
                threecheck = True
        if twocheck:
            twos = twos + 1
        if threecheck:
            threes = threes + 1

    print "2's"
    print twos
    print "3's"
    print threes
    print twos*threes

"""
    boxes = []
    for uline in lines:
        sortedline = []
        for cha in uline:
            print cha
            if len(sortedline) > 0:
                for s in sortedline:
                    if s == cha:
                        break
                    n = uline.count("cha")
                    linecollection.append((cha, n))
            else:
                n = line.count("cha")
                linecollection.append((cha, n))

        boxes.append(sortedline)
        print sortedline

    doubletotals = 0
    tripletotals = 0
    for box in boxes:
        length = len(box)-1
        while length > 1:
            double = False
            triple = False
            killlist = []
            for c in range(0, length, 1):
                if box[0] == box[c]:
                    count = count + 1
                    killlist.append(c)
            if(count == 2):
                double = True
            if(count == 3):
                triple = True
            if double and triple:
                break
            for k in killlist:
                box

        differences = []
        candidates = []
        for c in range(1, len(cumulatives) - 1, 1):
            for comp in range(0, c - 1, 1):
                firstcomp = cumulatives[c]
                secondcomp = cumulatives[comp]
                negater = 1 * (firstcomp / abs(firstcomp)) * (secondcomp / abs(secondcomp))
                diff = abs(firstcomp - (negater * secondcomp))
                if diff != 0:
                    if (diff % 510) == 0.00000:
                        candidates.append((firstcomp, secondcomp, (diff / 510), comp))
        winner = candidates[0]
        for index in range(1, len(candidates) - 1, 1):
            if candidates[index][2] < winner[2]:
                winner = candidates[index]
            elif candidates[index][2] == winner[2]:
                if candidates[index][3] < winner[3]:
                    winner = candidates[index]
        print winner

        loop = 0
        currenttotal = 0
        while True:
            for num in numlist:
                currenttotal = currenttotal + num
                for tot in totals:
                    if currenttotal == tot:
                        return tot
                totals.append(currenttotal)
            loop = loop + 1

            print loop
            print len(totals) - 1    
        """