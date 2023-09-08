function removeIslands(matrix) {
  for (let i=0; i<matrix[0].length; i++) {
    traverseNeighbors(0, i, matrix)
    traverseNeighbors(matrix.length-1, i, matrix)
  }
  for (let j=0; j<matrix.length; j++) {
    traverseNeighbors(j, 0, matrix)
    traverseNeighbors(j, matrix[0].length-1, matrix)
  }

  for (let j=0; j<matrix.length; j++) {
    for (let i=0; i<matrix[0].length; i++) {
      const value = matrix[j][i]

      if (value == 1) {
        matrix[j][i] = 0
      } else if (value == 2) {
        matrix[j][i] = 1
      }
    }
  }
  return matrix;
}

function traverseNeighbors(j, i, matrix) {
  const current = matrix[j][i]

  if (current == 1) {
    matrix[j][i] = 2

    if (j + 1 < matrix.length) {
      traverseNeighbors(j+1, i, matrix)
    }
    if (j-1 >= 0) {
      traverseNeighbors(j-1, i, matrix)
    }
    if (i+1 < matrix[0].length) {
      traverseNeighbors(j, i+1, matrix)
    }
    if (i - 1 >= 0) {
      traverseNeighbors(j, i-1, matrix)
    }
  }
}
exports.removeIslands = removeIslands;