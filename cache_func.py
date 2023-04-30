# キャッシュをするためのデコレーター
# from functools import lru_cache
import time

# 自作のキャッシュ用のデコレータ
# デコレータは関数やクラスの前後に特定の処理を追加できる機能

# キャッシュに使用するためのデコレータの作成（lru_cacheの中身）


def memoize(f):
    # 辞書型で格納しておく
    cache = {}

    def _wrapper(n):
        # cacheの中に含まれていない場合、辞書の中に追加する
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper

# 作成したデコレータ関数の使用


@memoize
# @lru_cache()
def long_func(num: int) -> int:
    r = 0
    for i in range(20000000):
        r += num * i
    return r


if __name__ == "__main__":
    for i in range(10):
        print(long_func(i))
    # 開始時刻の記録
    start = time.time()
    # 処理
    for i in range(10):
        print(long_func(i))
    # 処理にかかった時間を算出
    print(time.time() - start)
