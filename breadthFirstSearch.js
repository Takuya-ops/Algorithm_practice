class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }
  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  breadthFirstSearch(array = []) {
    const nodes = [this]

    while (nodes.length) {
      const currentNode = nodes.shift()
      array.push(currentNode.name)
      nodes.push(...currentNode.children)
    }
    return array
  }
}

exports.Node = Node;