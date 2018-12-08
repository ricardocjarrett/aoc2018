def main():

    with open("puz1_input.txt") as f:
        numberfile = f.readlines()
    numlist = []
    total = 0
    cumulatives = []
    for number in numberfile:
        if number[:1] == "-":
            value = (-1*int(number[1:]))
        elif number[:1] == "+":
            value = (int(number[1:]))
        numlist.append(value)
        total = total + value
        cumulatives.append(total)
    increase = cumulatives[len(cumulatives)-1]
    
    differences = []
    candidates = []
    for c in range(1, len(cumulatives)-1, 1):
        for comp in range(0, c-1, 1):
            firstcomp = cumulatives[c]
            secondcomp = cumulatives[comp]
            negater = 1 * (firstcomp / abs(firstcomp)) * (secondcomp / abs(secondcomp))
            diff = abs(firstcomp - (negater * secondcomp))
            if diff != 0:
                if (diff % 510) == 0.00000:
                    candidates.append((firstcomp, secondcomp, (diff / 510), comp))
    winner = candidates[0]
    for index in range(1, len(candidates)-1, 1):
        if candidates[index][2] < winner[2]:
            winner = candidates[index]
        elif candidates[index][2] == winner[2]:
            if candidates[index][3] < winner[3]:
                winner = candidates[index]
    print winner

    """
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
