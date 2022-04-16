import turtle
import random
import argparse

colors = ["black", "red", "green", "blue", "yellow", "magenta", "cyan", "orange", "brown", "pink"]

turt = turtle.Turtle()
turt.hideturtle()
turt.speed(0)
turt.left(90)

def execCode(code):
    pointer = 0
    pen = True
    mult = 10
    if type(code) == str:
        code = code.strip().replace("\n", "").replace(" ", "").replace("\t", "")
        code = "".join(filter(str.isdigit, code))
        code = list(map(int, list(code)))
    while pointer < len(code):
        if code[pointer] == 1:
            turt.forward(mult * code[pointer+1])
            pointer += 1
        elif code[pointer] == 2:
            turt.left(180)
            turt.forward(mult * code[pointer+1])
            turt.right(180)
            pointer += 1
        elif code[pointer] == 3:
            turt.left(90)
            turt.forward(mult * code[pointer+1])
            turt.right(90)
            pointer += 1
        elif code[pointer] == 4:
            turt.right(90)
            turt.forward(mult * code[pointer+1])
            turt.left(90)
            pointer += 1
        elif code[pointer] == 5:
            turt.right(code[pointer+1])
            pointer += 1
        elif code[pointer] == 6:
            if pen:
                turt.penup()
                pen = False
            else:
                turt.pendown()
                pen = True
        elif code[pointer] == 7:
            turt.color(colors[code[pointer+1]])
            pointer += 1
        elif code[pointer] == 8:
            start = pointer + 2
            end = start + code[pointer+1]
            for i in range(start, end - 1):
                j = random.randint(start, end)
                code[i - 1], code[j - 1] = code[j - 1], code[i - 1]
            pointer += 1
        elif code[pointer] == 9:
            for i in range(code[pointer+2]):
                execCode(code[pointer - code[pointer+1]:pointer])
            pointer += 2
        pointer += 1	

argparser = argparse.ArgumentParser(description="TurtleDigits code interpreter")
argparser.add_argument("filename", help="File containing the code to be interpreted")
args = argparser.parse_args()

with open(args.filename, "r") as f:
    execCode(f.read())

turtle.done()
