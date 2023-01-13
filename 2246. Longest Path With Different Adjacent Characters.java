class Solution {
  private int longestPath = 1;

  public int dfs(int currentNode, Map<Integer, List<Integer>> children, String s) {
    // ノードが唯一の子である場合、currentNodeに１を返す。
    if (!children.containsKey(currentNode)) {
      return 1;
    }
    // currentNodeから始まる最長および２番目に長いパス
    int longestChain = 0, secondLongestChain = 0;
    for (int child : children.get(currentNode)) {
      // 子から始まる最長チェーンのノード数を取得
      int longestChainStartingFromChild = dfs(child, children, s);
      // currentNodeと同じ文字を持つ子には移動しない
      if (s.charAt(currentNode) == s.charAt(child)) {
        continue;
      }
      // longestChainStartingFromChildの場合は、longestChainとsecondLongestChainを変更する
      if (longestChainStartingFromChild > longestChain) {
        secondLongestChain = longestChain;
        longestChain = longestChainStartingFromChild;
      } else if (longestChainStartingFromChild > secondLongestChain) {
        secondLongestChain = longestChainStartingFromChild;
      }
    }

    // node自体に１を追加する
    longestPath = Math.max(longestPath, longestChain + secondLongestChain + 1);
    return longestChain + 1;
  }

  public int longestPath(int[] parent, String s) {
    int n = parent.length;
    Map<Integer, List<Integer>> children = new HashMap<>();
    // ルートノード０には親がないので、ノード１から開始する。
    for (int i = 1; i < n; i++) {
      children.computeIfAbsent(parent[i], value -> new ArrayList<Integer>()).add(i);
    }

    dfs(0, children, s);

    return longestPath;
  }
}