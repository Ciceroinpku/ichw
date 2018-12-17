"""tile.py  Description of ways of tiling

__author__ = "Jiangyufei"
__pkuid__ = "1800011734"
__email__ = "1800011734@pku.edu.cn"
"""

import turtle


"""Function 'built_wall' is used to built a list that include all the coordinates which a m*n wall would include."""


def built_wall(m, n):
    wall = []
    for i in range(m*n):
        wall.append(i)
    return wall


"""Function 'find_bricks' is used to figure out all the possible bricks that can be removed from a given wall.
This is the modified vision, solving the repeat problem."""


def find_bricks(wall, m, a, b):
    bricks = []
    i = wall[0]         # The found brick must be located at the smallest coordinate remained.
    for r in range(2):  # For every rectangle, there are two possible tropism.
        brick = []
        if r == 0:
            for y in range(b):
                for x in range(a):
                    brick.append(i+x+y*m)
            if conflict(brick, wall, m, a) is True:
                bricks.append(brick)
        elif r == 1 and not a == b:   # If the rectangle is a square, there is no need to discuss two tropism.
            for y in range(a):
                for x in range(b):
                    brick.append(i+x+y*m)
            if conflict(brick, wall, m, b) is True:
                bricks.append(brick)
    return bricks


"""This function is in propose of simplify the process of removing the brick from the given wall in function 'remove'"""


def rest_wall(wall, brick):
    for coordinate in brick:
        wall.remove(coordinate)
    return wall


"""Function 'list_in' is designed to simplify function 'conflict'."""


def list_in(a, b):
    for i in a:
        if i not in b:
            return False
        elif i == a[-1]:
            return True


"""Function 'conflict' is used to figure out whether the brick which is found by
function 'find_bricks' is available or not."""


def conflict(brick, wall, m, a):
    x = brick[0] % m+1
    if x == 0:
        x = m
    if x+a-1 <= m and list_in(brick, wall) is True:  # There are two judgement, whether the brick is continuous and
        return True                                  # whether all the coordinates of the brick are in the given wall.
    else:
        return False


"""The function 'remove' is designed to find out all the solutions for the given wall and brick."""


def remove(wall, m, n, a, b):
    if wall == []:              # Set the recursive end, returning a two-dimension empty list.
        return [[]]
    bricks = find_bricks(wall, m, a, b)
    way = []
    for brick in bricks:    # For each possible bricks and removed wall, discuss anew.
        awall = wall[:]
        rwall = rest_wall(awall, brick)
        parts = remove(rwall, m, n, a, b)
        for solution in parts:
            way.append([tuple(brick)]+solution)  # Add the brick just be found to the solutions list that 'remove' gave.
    return way


"""The function 'draw_wall' is used to draw the visual picture of one given solution."""


def draw_wall(solution, m, n):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('blank')
    pen.pensize(1)
    pen.color('sea green')
    for y in range(n+1):  # Draw the horizontal lines of the wall.
        pen.penup()
        pen.goto(0, 30*y)
        pen.pendown()
        pen.forward(30*m)
    pen.left(90)
    for x in range(m+1):  # Draw the vertical lines of the wall
        pen.penup()
        pen.goto(30*x, 0)
        pen.pendown()
        pen.forward(30*n)

    num = 0                # Write the coordinates of each 1*1 squares.
    while num < m*n:
        pen.penup()
        x = num % m+0.5
        y = num//m
        pen.goto(30*x, 30*y)
        pen.pendown
        pen.write(str(num), 'center')
        num = num+1

    pen.right(90)                   # Draw the bricks in the wall we had just drawn.
    pen.pensize(3)
    pen.color('black')
    for brick in solution:
        coordinate = list(brick)
        x1 = coordinate[0] % m      # Find out the coordinates of the brick in coordinate system.
        y1 = coordinate[0]//m
        x2 = coordinate[-1] % m
        y2 = coordinate[-1]//m
        pen.penup()
        pen.goto(30*x1, 30*y1)
        pen.pendown()
        for i in range(2):
            pen.forward(30*(x2-x1+1))
            pen.left(90)
            pen.forward(30*(y2-y1+1))
            pen.left(90)
    turtle.done()


"""The function 'tile' is the confluence function of the program, in which all the functions assemble together.
Also, finish some fragmentary works, such as print results."""


def tile(m, n, a, b):
    wall = built_wall(m, n)
    ways = remove(wall, m, n, a, b)
    solutions = []

    for i in ways:           # In the fear of remaining some repeat errors, the author add this three line sentences
        if i not in solutions:   # in order to exclude the repetition.
            solutions.append(i)

    if len(solutions) == 0:   # If result list has no ant solutions inside, print "no result"
        print("There are no solutions for the given wall and brick.")
    else:
        for solution in solutions:
            print(solution)

    print("The number of solutions is:", len(solutions))
    if not len(solutions) == 0:
        number = input("Please input the serial number of the solution you want to draw.")
        if int(number) <= len(solutions):
            draw_wall(solutions[int(number)-1], m, n)
        else:
            print("There is no such solution.")


"""Function 'main' is the main module of the whole program"""


def main():
    m, n, a, b = int(input("Input the length of the wall:")), int(input("Input the width of the wall:")), \
                 int(input("Input the length of the brick:")), int(input("Input the width of the brick:"))
    tile(m, n, a, b)


if __name__ == "__main__":
    main()

