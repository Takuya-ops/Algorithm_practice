def reverseWordsInString(string):
    word_list = []
    start_word_index = 0

    if string == "":
        return ""

    for idx, char in enumerate(string):
        if char == " ":
            word_list.append(string[start_word_index:idx])
            start_word_index = idx + 1

    # 最後の単語をリストに追加
    word_list.append(string[start_word_index:])

    return " ".join(word_list[::-1])


# テスト用例
input_string = "Hello World"
result = reverseWordsInString(input_string)
print(result)  # 出力: "World Hello"
