import random, time, copy

width = 5
height = 5

# Initialize the grid with random cells
nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append("#")  # Living cell
        else:
            column.append(" ")  # Dead cell
    nextCells.append(column)

while True:
    print("\n" * 5)  # Print new lines to separate generations
    currentCells = copy.deepcopy(nextCells)  # Make a deep copy of nextCells to currentCells

    # Print current cells with borders
    for y in range(height):
        for x in range(width):
            print(f"+---", end="")
        print("+")  # Print the top border of the row

        for x in range(width):
            print(f"| {currentCells[x][y]} ", end="")
        print("|")  # Print the cell content and the right border

    for x in range(width):
        print(f"+---", end="")
    print("+")  # Print the bottom border of the last row

    # Calculate the next state
    for x in range(width):
        for y in range(height):
            # Get neighboring coordinates
            leftCord = (x - 1) % width
            rightCord = (x + 1) % width
            aboveCord = (y - 1) % height
            belowCord = (y + 1) % height

            # Count the number of living neighbors
            numNeighbours = 0
            if currentCells[leftCord][aboveCord] == "#":
                numNeighbours += 1
            if currentCells[leftCord][y] == "#":
                numNeighbours += 1
            if currentCells[leftCord][belowCord] == "#":
                numNeighbours += 1
            if currentCells[x][aboveCord] == "#":
                numNeighbours += 1
            if currentCells[x][belowCord] == "#":
                numNeighbours += 1
            if currentCells[rightCord][aboveCord] == "#":
                numNeighbours += 1
            if currentCells[rightCord][y] == "#":
                numNeighbours += 1
            if currentCells[rightCord][belowCord] == "#":
                numNeighbours += 1

            # Apply Conway's Game of Life rules
            if currentCells[x][y] == "#" and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = "#"  # Cell stays alive
            elif currentCells[x][y] == " " and numNeighbours == 3:
                nextCells[x][y] = "#"  # Cell becomes alive
            else:
                nextCells[x][y] = " "  # Cell dies or remains dead

    # Pause to view the current state
    time.sleep(1)
