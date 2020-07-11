import pygame
import numpy
import time

# Initialize the imported modules o pygame
pygame.init()

widthViewPort, heightViewPort = 600, 600

screen = pygame.display.set_mode((heightViewPort, widthViewPort))

backgroundColor = 25,25,25
screen.fill(backgroundColor)

cellsX, cellsY = 40, 40

dimensionCellsWidth = widthViewPort / cellsX
dimensionCellsHeight = heightViewPort / cellsY

gameState = numpy.zeros((cellsX, cellsY))

while True:
    pygame.event.pump()
    newGameState = numpy.copy(gameState)
    screen.fill(backgroundColor)

    time.sleep(0.1)
    for y in range(0, cellsX):
        for x in range(0, cellsY):
            # Search in a 3x3 square all the neighbour living cells 
            cellsNeighbour = gameState[(x - 1) % cellsX, (y - 1) % cellsY] + \
                            gameState[(x) % cellsX, (y - 1) % cellsY] + \
                            gameState[(x + 1) % cellsX, (y - 1) % cellsY] + \
                            gameState[(x - 1) % cellsX, (y) % cellsY] + \
                            gameState[(x + 1) % cellsX, (y) % cellsY] + \
                            gameState[(x - 1) % cellsX, (y + 1) % cellsY] + \
                            gameState[(x) % cellsX, (y + 1) % cellsY] + \
                            gameState[(x + 1) % cellsX, (y + 1) % cellsY]

            # Rule 1: If the cell is dead and have 3 neighbours, these cells reproduce and create a new cell
            if gameState[x, y] == 0 and cellsNeighbour == 3:
                newGameState[x, y] = 1

            # Rule 2: If the cell have less of 2 or more of 3 neighbours, the cell die of loneliness or overpopulation
            elif gameState[x, y] == 1 and (cellsNeighbour < 2 or cellsNeighbour > 3):
                newGameState[x, y] = 0

            polygon = [
                ((x) * dimensionCellsWidth, y * dimensionCellsHeight),
                ((x+1) * dimensionCellsWidth, y * dimensionCellsHeight),
                ((x+1) * dimensionCellsWidth, (y+1) * dimensionCellsHeight),
                ((x) * dimensionCellsWidth, (y+1) * dimensionCellsHeight)
            ]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128,128,128), polygon, 1)
            elif newGameState[x, y] == 1:
                pygame.draw.polygon(screen, (255,255,255), polygon, 0)
    gameState = numpy.copy(newGameState)
    pygame.display.flip()