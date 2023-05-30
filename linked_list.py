# class名を使いたいときに使用
from __future__ import annotations
# dataに入れるデータ型は何でも良い
from typing import Any

# python2の場合は、Node(object)：と記述する
class Node:
  def __init__(self, data: Any, next_node: Node = None):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self, head=None) -> None:
    self.head = head