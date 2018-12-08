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
        rects.append((int(num), (int(x), int(y)), (int(w)+int(x), int(h)+int(y)), (int(w), int(h))))
        """0:num, 1:start, 2:end, 3:w,h"""

    intList = []
    for iter in range(0, len(rects), 1):
        intList.append(0)
    """Loop all rectangles"""
    for i_rect, rect in enumerate(rects, 0):
        """Loop against all rectangles after this one"""
        for i_comp, comp in enumerate(rects[i_rect+1:], i_rect+1):
            cxs, cys = comp[1]
            cxe, cye = comp[2]
            cw, ch = comp[3]
            rxs, rys = rect[1]
            rxe, rye = rect[2]
            rw, rh = rect[3]
            if cxs >= (rxs-cw) and cxs <= rxe and cys >= (rys-ch) and cys <= rye:
                """C:comparison, R:rect, x,y, S:start, E:end"""
                intList[rect[0]-1] = 1
                intList[comp[0]-1] = 1
            else:
                pass
    for ii, i in enumerate(intList, 0):
        if i == 0:
            print rects[ii]