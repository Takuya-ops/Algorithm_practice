def minimumCharactersForWords(words):
    mainMap = {}
    resultList = []

    for word in words:
        tempMap = {}

        # 単語ごとに文字の出現回数をカウントし、mainMapに追加します
        for letter in word:
            if letter not in mainMap:
                mainMap[letter] = mainMap.get(letter, 0) + 1
                resultList.append(letter)
            tempMap[letter] = tempMap.get(letter, 0) + 1

        # 単語内の文字の出現回数がmainMapより多い場合、不足している文字を追加します
        for letter, count in tempMap.items():
            while count > mainMap[letter]:
                resultList.append(letter)
                mainMap[letter] += 1

    return resultList


# テスト用の単語リスト
words = ["hello", "world"]
result = minimumCharactersForWords(words)
print(result)
