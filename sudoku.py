#Universidad del Valle de Guatemala
#Inteligencia Artificial
#Integrantes:
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
# Oscar Saravia

# Operations

def createSudoku(size):
  allowedSizes = [4, 6, 9]
  matrix = []
  if size in allowedSizes:
    for i in range(size):
      tempArray = []
      for j in range(size):
        tempArray.append(0)
      matrix.append(tempArray)
    return matrix
  else:
    print('Únicamente se aceptan 4, 6 o 9 como tamaños')

def fillInitialPositions(sudoku, initialPositions):
  # print(sudoku)
  # print(initialPositions)
  # Setting coordinates
  for coord in initialPositions:
    row = coord[0] - 1
    column = coord[1] - 1
    value = coord[2]
    if value < 1 or value > 9:
      print('Los valores iniciales deben estar dentro de 1 y 9')
      return
    try:
      sudoku[row][column] = value
    except:
      print('La coordenada: ', row, ' ', column, ' es invalida')
      return
  return sudoku

# Variables
sudokuConfigLines = []
sudokuSize = 0
initialPositions = 0
isConfigValid = True
errorMsg = 'La configuración del sudoku no es válida, ingrese el tamaño del sudoku y la cantidad de posiciones iniciales.'

# Reading the txt file
sudokuFile = open('sudoku4.txt', 'r')
try:
  for line in sudokuFile:
    tempList = []
    for element in line.rstrip('\n').split(' '):
      tempList.append(int(element))
    sudokuConfigLines.append(tempList)
except:
  isConfigValid = False
  print(errorMsg)

# Close the txt file
sudokuFile.close()

# Validations
if isConfigValid and len(sudokuConfigLines) >= 2:
  sudokuSize = sudokuConfigLines[0][0]
  initialPositions = sudokuConfigLines[1][0]
  # Check if the number of initial positions matches the number of positions set on the file
  if (initialPositions + 2 != len(sudokuConfigLines)):
    print('Error, el numero de posiciones iniciales no coincide con las posiciones iniciales en el documento')
  else:
    # Remove first 2 config values, to make initial values list
    sudokuInitialValues = sudokuConfigLines
    for i in range(2):
      sudokuInitialValues.pop(0)
    emptySudoku = createSudoku(sudokuSize)
    filledSudoku = fillInitialPositions(emptySudoku, sudokuInitialValues)

board = filledSudoku

def print_board(bo):
    print(bo)

def solution(bo):
    find = find_empty_spaces(bo)
    if not find:
        return True
    else:
        row, col = find
    for m in range(1,sudokuSize + 1):
        if valid(bo, m, (row, col)):

            bo[row][col] = m

            if solution(bo):
                return True

            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    row, col = pos
    for m in range(sudokuSize):
        if bo[row][m] == num and col != m:
            return False
    for m in range(sudokuSize):
        if bo[m][col] == num and row != m:
            return False

    
    if sudokuSize == 6:
        squares_x = col // 3 * 3
        squares_y = row // 2 * 2
        y = 2
        x = 3
    elif sudokuSize == 9:
        squares_x = col // 3 * 3
        squares_y = row // 3 * 3
        y = 3
        x = 3
    else:
        squares_x = col // 2 * 2
        squares_y = row // 2 * 2
        y = 2
        x = 2
    

    for m in range(squares_y, squares_y + y):
        for c in range(squares_x, squares_x + x):
            if bo[m][c] == num and (m,c) != pos:
                return False

    return True

def find_empty_spaces(bo):
    for m in range(len(bo)):
        for c in range(len(bo[0])):
            if bo[m][c] == 0:
                return (m,c)

    return False


print('-------------Sin resolver--------------------')
print_board(board)
print('---------------------------------------------')
solution(board)
print('-----------------Resuelto--------------------')
print_board(board)
print('---------------------------------------------')
