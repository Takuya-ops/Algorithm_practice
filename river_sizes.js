function explore(i, j, size, matrix, visited) {
  if (visited[i][j]) return size;

  visited[i][j] = true;
  size++;

  if (matrix[i][j+1] === 1) size = explore(i, j+1, size, matrix, visited);
  if (matrix[i][j-1] === 1) size = explore(i, j-1, size, matrix, visited);
  if (matrix[i+1] && matrix[i+1][j] === 1) size = explore(i+1, j, size, matrix, visited);
  if (matrix[i-1] && matrix[i-1][j] === 1) size = explore(i-1, j, size, matrix, visited);

  return size;
}

function riverSizes(matrix) {
  const visited = []
  for (let i=0; i<matrix.length; i++) {
    const line = new Array(matrix[i].length).fill(null);
    visited.push(line);
  }

  const rivers = [];
  for (let i=0; i<matrix.length; i++) {
    for (let j= 0; j<matrix[i].length; j++) {
      if (visited[i][j]) continue;
      if (matrix[i][j] === 1) {
        const river = explore(i, j, 0, matrix, visited);
        rivers.push(river);
      } else visited[i][j] = true;
    }
  }
  return rivers;
}
exports.riverSizes = riverSizes;