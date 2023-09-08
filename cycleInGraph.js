function cycleInGraph(nodeList) {
  for (let i=0; i<nodeList.length; i++) {
    const hasCycle = getHasCycle(nodeList, i)
    if (hasCycle) {
        return hasCycle;
      }
    }
    return false;
  }
  
  function getHasCycle(nodeList, targetNode) {
    const queue = [targetNode]
    const visitedNodes = {}
    while (queue.length > 0) {
      const currentNode = queue.shift();
      if (nodeList[currentNode].includes(targetNode)) {
        return true;
      }
      visitedNodes[currentNode] = true
      nodeList[currentNode].forEach(edge => {
        if (!(edge in visitedNodes)) {
          queue.push(edge)
        }
      })
    }
    return false;
  }
  exports.cycleInGraph = cycleInGraph;