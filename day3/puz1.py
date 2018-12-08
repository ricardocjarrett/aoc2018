def main():

    with open("puz1.txt") as f:
        puz1file = f.readlines()

    rects = []
    for rect in puz1file:
        splitrect = rect.split(" ")
        num = splitrect[0][1:]
        x, y = splitrect[2].split(",")
        y = y[:-1]
        w, h = splitrect[3].split("x")
        h = h[:-1]
        rects.append((int(num), (int(x), int(y)), (int(w)+int(x), int(h)+int(y))))

    openx = []
    overlap = 0
    for x in range(0, 1000, 1):
        xolap = 0
        print ("Overlap: ", overlap)
        print ("X: ", x)
        openy = []
        for rect in rects:
            if rect[1][0] == x:
                openx.append(rect)
            if rect[2][0] == x:
                openx.remove(rect)
        print len(openx)
        for y in range(0, 1000, 1):
            for rect in openx:
                if rect[1][1] == y:
                    if not openy.count(rect):
                        openy.append(rect)
                if rect[2][1] == y:
                    openy.remove(rect)
            if len(openy) >= 2:
                xolap = xolap + 1
        overlap = overlap + xolap
