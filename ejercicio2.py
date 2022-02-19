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

def showSudoku(matrix, size):
  module = 0
  if (size == 9):
    module = 3
  elif (size == 6):
    module = 2
  elif (size == 4):
    module = 1
  for i in range(len(matrix)):
    if i % module == 0 and i != 0:
      print("- - - - - - - - - - - - - ")
    for j in range(len(matrix[0])):
      if j % module == 0 and j != 0:
        print(" | ", end="")
      if j == (size - 1):
        print(matrix[i][j])
      else:
        print(str(matrix[i][j]) + " ", end="")

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

def solveSudoku(matrix, size):
  find = getEmptySlots(matrix)
  if not find:
    return True
  else:
    row, col = find
  for i in range(1,size + 1):
    if valid(matrix, i, (row, col), size):
      matrix[row][col] = i
      if solveSudoku(matrix, size):
          return True
      matrix[row][col] = 0
  return False

def valid(bo, num, pos, size):
  module = 0
  if (size == 9):
    module = 3
  elif (size == 6):
    module = 2
  elif (size == 4):
    module = 1
  for i in range(len(bo[0])):
    if bo[pos[0]][i] == num and pos[1] != i:
      return False
  for i in range(len(bo)):
    if bo[i][pos[1]] == num and pos[0] != i:
      return False

  box_x = pos[1] // module
  box_y = pos[0] // module

  for i in range(box_y*module, box_y*module + module):
    for j in range(box_x * module, box_x*module + module):
      if bo[i][j] == num and (i,j) != pos:
        return False

  return True

def getEmptySlots(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        return (i, j)
  return None

# Variables
sudokuConfigLines = []
sudokuSize = 0
initialPositions = 0
isConfigValid = True
errorMsg = 'La configuración del sudoku no es válida, ingrese el tamaño del sudoku y la cantidad de posiciones iniciales.'

# Reading the txt file
sudokuFile = open('sudoku6.txt', 'r')
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
    if (filledSudoku):
      print('INITIAL SUDOKU')
      showSudoku(filledSudoku, sudokuSize)
      solveSudoku(filledSudoku, sudokuSize)
      print('FINAL SUDOKU')
      showSudoku(filledSudoku, sudokuSize)

