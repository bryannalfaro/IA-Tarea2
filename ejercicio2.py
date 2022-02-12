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
    print('Únicamente se aceptan 4, 6 o 0 como tamaños')

def showSudoku(matrix):
  for row in matrix:
    print(row)

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
sudokuFile = open('sudoku.txt', 'r')
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
      showSudoku(filledSudoku)

