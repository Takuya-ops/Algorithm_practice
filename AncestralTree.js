class AncestralTree {
  constructor(name) {
    this.name = name;
    this.ancestor = null;
  }
}

function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
  const ancestorsOne = new Set();
  
  // 1つ目の子孫のすべての祖先をセットに追加
  let current = descendantOne;
  while (current) {
    ancestorsOne.add(current);
    current = current.ancestor;
  }
  
  // 2つ目の子孫からルートに向かって祖先を辿り、最初に出現する共通の祖先を見つける
  current = descendantTwo;
  while (current) {
    if (ancestorsOne.has(current)) {
      return current;
    }
    current = current.ancestor;
  }
  
  return null; // 共通の祖先が見つからない場合は null を返す
}

exports.AncestralTree = AncestralTree;
exports.getYoungestCommonAncestor = getYoungestCommonAncestor;
