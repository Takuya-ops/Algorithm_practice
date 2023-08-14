import math


# クラスの定義：式木のノードを表すための BinaryTree クラス
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value  # ノードに格納される値（数値または演算子）
        self.left = left  # 左側の子ノード
        self.right = right  # 右側の子ノード


# 式木を評価するための関数
def evaluateExpressionTree(tree):
    # 演算子と演算子関数の対応を定義したディクショナリ
    operators = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: math.trunc(x / y),  # 小数点以下を切り捨てた割り算
        -4: lambda x, y: x * y,
    }

    # ノードが数値の場合、その数値を返す（再帰のベースケース）
    if tree.value >= 0:
        return tree.value

    # 式木の左側と右側を再帰的に評価して、それぞれの値を取得
    left_val = evaluateExpressionTree(tree.left)
    right_val = evaluateExpressionTree(tree.right)

    # 演算子ノードの場合、対応する演算子関数を適用して計算結果を返す
    return operators[tree.value](left_val, right_val)
