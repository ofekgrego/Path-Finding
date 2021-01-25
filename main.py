import random
from tkinter import *
import tkinter
import math

running = False

sizeOfWindowX = 1000
sizeOfWindowY = 1000
linesEachSide = 600

firstCube = []
lastCube = []
currentCount = 0
lastMovedCubes = []
grid = []
walls = []

noSol = False
foundIt = False
pathPlaces = []

window = Tk()
window.title("Graph Generator")
window.resizable(False, False)
mainCanvas = Canvas(window, width=sizeOfWindowX, height=sizeOfWindowY, background="gray")
mainCanvas.pack()
fInfo = Frame(window, width=200, height=sizeOfWindowY)
fInfo.pack()

creditLabel = Label(fInfo, text="Made By Ofek Grego").pack(side=tkinter.BOTTOM)


def drawFirst():
    global firstCube, lastCube, lastMovedCubes, grid, walls
    mainCanvas.delete("all")

    for n in range(linesEachSide):
        mainCanvas.create_line(0, n * sizeOfWindowY / linesEachSide, sizeOfWindowX, n * sizeOfWindowY / linesEachSide)
        grid.append([-1] * linesEachSide)

    for n in range(linesEachSide):
        mainCanvas.create_line(n * sizeOfWindowX / linesEachSide, 0, n * sizeOfWindowX / linesEachSide, sizeOfWindowY)

    while firstCube == lastCube:
        firstCube = [random.randint(0, linesEachSide - 1), random.randint(0, linesEachSide - 1)]
        lastCube = [random.randint(0, linesEachSide - 1), random.randint(0, linesEachSide - 1)]

    for n in range(round((linesEachSide * linesEachSide) / 3)):
        xAxe = random.randint(0, linesEachSide - 1)
        yAxe = random.randint(0, linesEachSide - 1)
        walls.append([xAxe, yAxe])
        grid[xAxe][yAxe] = -5

    lastMovedCubes = [firstCube]

    grid[firstCube[0]][firstCube[1]] = 0
    grid[lastCube[0]][lastCube[1]] = -2

    for n in walls:
        mainCanvas.create_rectangle(n[0] * sizeOfWindowX / linesEachSide,
                                    n[1] * sizeOfWindowY / linesEachSide,
                                    (n[0] + 1) * sizeOfWindowX / linesEachSide,
                                    (n[1] + 1) * sizeOfWindowY / linesEachSide, fill="#FFF")

    mainCanvas.create_rectangle(firstCube[0] * sizeOfWindowX / linesEachSide,
                                firstCube[1] * sizeOfWindowY / linesEachSide,
                                (firstCube[0] + 1) * sizeOfWindowX / linesEachSide,
                                (firstCube[1] + 1) * sizeOfWindowY / linesEachSide, fill="#00FF00")

    mainCanvas.create_rectangle(lastCube[0] * sizeOfWindowX / linesEachSide,
                                lastCube[1] * sizeOfWindowY / linesEachSide,
                                (lastCube[0] + 1) * sizeOfWindowX / linesEachSide,
                                (lastCube[1] + 1) * sizeOfWindowY / linesEachSide, fill="#FF0000")


def drawUpdate():
    for n in lastMovedCubes:
        mainCanvas.create_rectangle(n[0] * sizeOfWindowX / linesEachSide,
                                    n[1] * sizeOfWindowY / linesEachSide,
                                    (n[0] + 1) * sizeOfWindowX / linesEachSide,
                                    (n[1] + 1) * sizeOfWindowY / linesEachSide, fill="#444")

    if pathPlaces != []:
        for n in range(len(pathPlaces)):
            mainCanvas.create_rectangle(pathPlaces[n][0] * sizeOfWindowX / linesEachSide,
                                        pathPlaces[n][1] * sizeOfWindowY / linesEachSide,
                                        (pathPlaces[n][0] + 1) * sizeOfWindowX / linesEachSide,
                                        (pathPlaces[n][1] + 1) * sizeOfWindowY / linesEachSide, fill="#0000FF")


def foundPath(xAxe, yAxe):
    global foundIt, pathPlaces
    foundIt = True

    currentWay = currentCount
    pathPlaces = [[xAxe, yAxe]]
    while (currentWay != 0):
        # X+
        next = False
        if ((grid[pathPlaces[len(pathPlaces) - 1][0] - 1][pathPlaces[len(pathPlaces) - 1][1]] != -1)
                & (grid[pathPlaces[len(pathPlaces) - 1][0] - 1][pathPlaces[len(pathPlaces) - 1][1]] != -2)
                & (grid[pathPlaces[len(pathPlaces) - 1][0] - 1][pathPlaces[len(pathPlaces) - 1][1]] != -5)
                & (grid[pathPlaces[len(pathPlaces) - 1][0] - 1][pathPlaces[len(pathPlaces) - 1][1]] < currentWay)
                & (next == False)):
            pathPlaces.append([pathPlaces[len(pathPlaces) - 1][0] - 1, pathPlaces[len(pathPlaces) - 1][1]])
            next = True
            # X-
        if (pathPlaces[len(pathPlaces) - 1][0] + 1 < linesEachSide):
            if (((grid[pathPlaces[len(pathPlaces) - 1][0] + 1][pathPlaces[len(pathPlaces) - 1][1]] != -1))
                    & (grid[pathPlaces[len(pathPlaces) - 1][0] + 1][pathPlaces[len(pathPlaces) - 1][1]] != -2)
                    & (grid[pathPlaces[len(pathPlaces) - 1][0] + 1][pathPlaces[len(pathPlaces) - 1][1]] != -5)
                    & (grid[pathPlaces[len(pathPlaces) - 1][0] + 1][pathPlaces[len(pathPlaces) - 1][1]] < currentWay)
                    & (next == False)):
                pathPlaces.append([pathPlaces[len(pathPlaces) - 1][0] + 1, pathPlaces[len(pathPlaces) - 1][1]])
                next = True
            # Y-
        if ((grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] - 1] != -1)
                & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] - 1] != -2)
                & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] - 1] != -5)
                & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] - 1] < currentWay)
                & (next == False)):
            pathPlaces.append([pathPlaces[len(pathPlaces) - 1][0], pathPlaces[len(pathPlaces) - 1][1] - 1])
            next = True
            # Y+
        if (pathPlaces[len(pathPlaces) - 1][1] + 1 < linesEachSide):
            if ((grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] + 1] != -1)
                    & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] + 1] != -2)
                    & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] + 1] != -5)
                    & (grid[pathPlaces[len(pathPlaces) - 1][0]][pathPlaces[len(pathPlaces) - 1][1] + 1] < currentWay)
                    & (next == False)):
                pathPlaces.append([pathPlaces[len(pathPlaces) - 1][0], pathPlaces[len(pathPlaces) - 1][1] + 1])
                next = True
        currentWay -= 1

    print(pathPlaces)
    drawUpdate()


def findLine():
    global lastMovedCubes, currentCount, grid, noSol
    currentCount += 1
    newLastMovedCubes = []
    hasSoultion = False
    for n in range(len(lastMovedCubes)):
        # X-
        if (lastMovedCubes[n][0] != 0):
            if (grid[lastMovedCubes[n][0] - 1][lastMovedCubes[n][1]] == -5):
                do = False
            elif (grid[lastMovedCubes[n][0] - 1][lastMovedCubes[n][1]] == -2):
                foundPath(lastMovedCubes[n][0], lastMovedCubes[n][1])
                hasSoultion = True
                break
            elif (grid[lastMovedCubes[n][0] - 1][lastMovedCubes[n][1]] == -1):
                grid[lastMovedCubes[n][0] - 1][lastMovedCubes[n][1]] = currentCount
                newLastMovedCubes.append([lastMovedCubes[n][0] - 1, lastMovedCubes[n][1]])
                hasSoultion = True
        # X+
        if (lastMovedCubes[n][0] != linesEachSide - 1):
            if (grid[lastMovedCubes[n][0] + 1][lastMovedCubes[n][1]] == -5):
                do = False
            elif (grid[lastMovedCubes[n][0] + 1][lastMovedCubes[n][1]] == -2):
                foundPath(lastMovedCubes[n][0], lastMovedCubes[n][1])
                hasSoultion = True
                break
            elif (grid[lastMovedCubes[n][0] + 1][lastMovedCubes[n][1]] == -1):
                grid[lastMovedCubes[n][0] + 1][lastMovedCubes[n][1]] = currentCount
                newLastMovedCubes.append([lastMovedCubes[n][0] + 1, lastMovedCubes[n][1]])
                hasSoultion = True
        # Y-
        if (lastMovedCubes[n][1] != 0):
            if (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] - 1] == -5):
                do = False
            elif (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] - 1] == -2):
                foundPath(lastMovedCubes[n][0], lastMovedCubes[n][1])
                hasSoultion = True
                break
            elif (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] - 1] == -1):
                grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] - 1] = currentCount
                newLastMovedCubes.append([lastMovedCubes[n][0], lastMovedCubes[n][1] - 1])
                hasSoultion = True
        # Y+
        if (lastMovedCubes[n][1] != linesEachSide - 1):
            if (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] + 1] == -5):
                do = False
            elif (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] + 1] == -2):
                foundPath(lastMovedCubes[n][0], lastMovedCubes[n][1])
                hasSoultion = True
                break
            elif (grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] + 1] == -1):
                grid[lastMovedCubes[n][0]][lastMovedCubes[n][1] + 1] = currentCount
                newLastMovedCubes.append([lastMovedCubes[n][0], lastMovedCubes[n][1] + 1])
                hasSoultion = True

    lastMovedCubes = newLastMovedCubes

    if (hasSoultion == False):
        noSol = True

    drawUpdate()


def untilFind():
    global running
    if (noSol == False):
        running = True
        findLine()
        if (foundIt == False):
            print(" - " + str(currentCount))
            print(str(len(lastMovedCubes)) + " Cubes")
            window.after(1, untilFind)
    else:
        print("No Sol..")


drawFirst()


def clickAction(event):
    global grid, walls
    if (running == False):
        if ((grid[math.floor(event.x / (sizeOfWindowX / linesEachSide))][
                 math.floor(event.y / (sizeOfWindowY / linesEachSide))] != -5)):
            if (grid[math.floor(event.x / (sizeOfWindowX / linesEachSide))][
                math.floor(event.y / (sizeOfWindowY / linesEachSide))] != -2):
                if (grid[math.floor(event.x / (sizeOfWindowX / linesEachSide))][
                    math.floor(event.y / (sizeOfWindowY / linesEachSide))] != 0):
                    grid[math.floor(event.x / (sizeOfWindowX / linesEachSide))][
                        math.floor(event.y / (sizeOfWindowY / linesEachSide))] = -5
                    walls.append([math.floor(event.x / (sizeOfWindowX / linesEachSide)),
                                  math.floor(event.y / (sizeOfWindowY / linesEachSide))])
                    mainCanvas.create_rectangle(
                        math.floor(event.x / (sizeOfWindowX / linesEachSide)) * sizeOfWindowX / linesEachSide,
                        math.floor(event.y / (sizeOfWindowY / linesEachSide)) * sizeOfWindowY / linesEachSide,
                        (math.floor(event.x / (sizeOfWindowX / linesEachSide)) + 1) * sizeOfWindowX / linesEachSide,
                        (math.floor(event.y / (sizeOfWindowY / linesEachSide)) + 1) * sizeOfWindowY / linesEachSide,
                        fill="#FFF")
        else:
            grid[math.floor(event.x / (sizeOfWindowX / linesEachSide))][
                math.floor(event.y / (sizeOfWindowY / linesEachSide))] = -1
            mainCanvas.create_rectangle(
                math.floor(event.x / (sizeOfWindowX / linesEachSide)) * sizeOfWindowX / linesEachSide,
                math.floor(event.y / (sizeOfWindowY / linesEachSide)) * sizeOfWindowY / linesEachSide,
                (math.floor(event.x / (sizeOfWindowX / linesEachSide)) + 1) * sizeOfWindowX / linesEachSide,
                (math.floor(event.y / (sizeOfWindowY / linesEachSide)) + 1) * sizeOfWindowY / linesEachSide,
                fill="#888")


mainCanvas.bind("<Button-1>", clickAction)
runButton = Button(fInfo, text="Run!", command=untilFind).pack(side=tkinter.TOP)

window.mainloop()
