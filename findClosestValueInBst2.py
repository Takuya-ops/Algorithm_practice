from typing import List

# 引数（二分木のノード値、目標値）　目標値に近い値を返す。


def findClosestValueBst(tree, target):
    print("Target:", target)

    def find_recursively(tree, closest):
        if tree is None:
            return closest
