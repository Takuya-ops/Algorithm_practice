def tournamentWinner(competitions, results):
    dict = {}  # 勝利回数をカウントするための空の辞書を作成

    # 各競技の結果とその対戦を順番に処理
    for i, comp in enumerate(competitions):
        if results[i]:  # もしi番目の競技の結果がTrue（チーム1の勝利）なら
            dict[comp[0]] = dict.get(comp[0], 0) + 1  # チーム1の勝利回数を辞書に追加または1増やす
        else:  # もしi番目の競技の結果がFalse（チーム2の勝利）なら
            dict[comp[1]] = dict.get(comp[1], 0) + 1  # チーム2の勝利回数を辞書に追加または1増やす

    # 辞書の中で最も多く勝利したチーム名を返す
    return max(dict, key=dict.get)


if __name__ == "__main__":
    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"],
    ]
    results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
    print(tournamentWinner(competitions, results))
