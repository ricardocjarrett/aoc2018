def main():

    with open("puz1_input.txt") as f:
        numbers = f.readlines()
    total = 0
    for number in numbers:
        if number[:1] == "-":
            total = total - int(number[1:])
        elif number[:1] == "+":
            total = total + int(number[1:])
        print total