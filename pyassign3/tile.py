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
    i = wall[0]
    for r in range(2):
        brick = []
        if r == 0:
            for y in range(b):
                for x in range(a):
                    brick.append(i+x+y*m)
            if conflict(brick, wall, m, a) is True:
                bricks.append(brick)
        if r == 1:
            for y in range(a):
                for x in range(b):
                    brick.append(i+x+y*m)
            if conflict(brick, wall, m, b) is True:
                bricks.append(brick)
    return bricks


"""This function is in propose of simplify the process of removing the brick from the given wall"""


def rest_wall(wall, brick):
    for coordinate in brick:
        wall.remove(coordinate)
    return wall


"""Function 'list_in' is designed to complete function 'conflict'."""


def list_in(a, b):
    for i in a:
        if i not in b:
            return False
        elif i == a[-1]:
            return True


"""Function 'conflict' is used to figure out whether the brick which is found by
function 'find_bricks' is available or not."""


def conflict(brick, wall, m, a):
    x = brick[0]%m +1
    if x+a-1 <= m and list_in(brick, wall) is True:
        return True
    else:
        return False


"""The function 'tile' is designed to find out all the solutions for the given wall and brick."""


def tile(wall, m, n, a, b):
    if wall == []:
        return [[]]
    bricks = find_bricks(wall, m, a, b)
    way = []
    for brick in bricks:
        awall = wall[:]
        rwall = rest_wall(awall, brick)
        parts = tile(rwall, m, n, a, b)
        for solution in parts:
            way.append(solution+[tuple(brick)])
    return way


"""The function 'main' is the main module."""


def main(m, n, a, b):
    wall = built_wall(m, n)
    ways = tile(wall, m, n, a, b)
    aways = []
    for i in ways:
        if i not in aways:
            aways.append(i)
    solutions = []
    for way in aways:
        solutions.append(sorted(way))
    if len(solutions) == 0:
        print("There are no solutions for the given wall and brick.")
    else:
        for solution in solutions:
            print(solution)
        print("The number of solutions is:", len(solutions))
    if not len(solutions) == 0:
        number = input("Please input the serial number of the solution you want to draw.\n"
                       "(The number must not bigger than the number of solutions):")
        while number.isdigit() is False or int(number) > len(solutions):
            number = input("Please input the serial number of the solution you want to draw.\n"
                           "(The number must not bigger than the number of solutions):")
        draw_wall(solutions[int(number)-1], m)


"""The function draw_wall is used to draw the visual picture of one given solution."""


def draw_wall(solution, m):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('blank')
    pen.pensize(3)
    for brick in solution:
        coordinate = list(brick)
        x1 = coordinate[0]%m+1      # Find out the coordinates of the brick in coordinate system.
        y1 = coordinate[0]//m
        x2 = coordinate[-1]%m+1
        y2 = coordinate[-1]//m
        pen.penup()
        pen.goto(20*x1, 20*y1)
        pen.pendown()
        for i in range(2):
            pen.forward(20*(x2-x1+1))
            pen.left(90)
            pen.forward(20*(y2-y1+1))
            pen.left(90)
    turtle.done()


if __name__ == "__main__":
    m, n, a, b = int(input("Input the length of the wall:")), int(input("Input the width of the wall:")),\
                 int(input("Input the length of the brick:")), int(input("Input the width of the brick:"))
    main(m, n, a, b)

