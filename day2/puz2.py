def main():

    with open("puz1.txt") as f:
        puz1file = f.readlines()

    lines = []
    for line in puz1file:
        lines.append(line)

    """Loop through all lines of the puzzle, except the first"""

    winners = []
    for i_line, line in enumerate(lines, 1):
        """Loop through all lines BEFORE this line"""
        for compLine in lines[:i_line]:
            fails = []
            """Loop through all characters in this line"""
            for i_cha, cha in enumerate(line, 0):
                if cha != compLine[i_cha]:
                    fails.append(i_cha)
                if len(fails) == 2:
                    break
            if len(fails) == 1:
                winners.append((line, compLine, i_cha))

    for w in winners:
        print w
