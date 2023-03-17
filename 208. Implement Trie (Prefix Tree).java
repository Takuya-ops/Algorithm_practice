class Trie {
  boolean isEnd;
  Trie next[];

  public Trie() {
    isEnd = false;
    next = new Trie[26];
  }

  public void insert(String word) {
    Trie node = this;
    for (char ch : word.toCharArray()) {
      int idx = ch - 'a';
      if (node.next[idx] == null) {
        node.next[idx] = new Trie();
      }

      node = node.next[idx];
    }

    node.isEnd = true;
  }

  public boolean search(String word) {
    Trie node = searchPrefix(word);
    return node != null && node.isEnd;
  }

  public boolean startsWith(String prefix) {
    Trie node = searchPrefix(prefix);
    return node != null;
  }

  public Trie searchPrefix(String prefix) {
    Trie node = this;
    for (char ch : prefix.toCharArray()) {
      int idx = ch - 'a';
      if (node.next[idx] == null) {
        return null;
      }

      node = node.next[idx];
    }

    return node;
  }
}