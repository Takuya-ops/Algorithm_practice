import string

# 大文字での実装
ALPHABET = string.ascii_uppercase

# 元の文字列と同じ長さの文字列を作成する関数


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        key += key[i]
    return key


# 暗号化用の関数
def encrypt(message: str, key: str) -> str:
    result = ""
    # インデックス番号と中身（char）を分けて取得
    for i, char in enumerate(message):
        # 大文字のアルファベット以外のものがある場合、暗号化せずそのまま返す。
        if char not in ALPHABET:
            result += char
            continue

        # 暗号化((元の文字列のインデックス番号 + 鍵の文字列のインデックス番号) % アルファベットの長さ))
        index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        result += ALPHABET[index]

        # unicodeのコードポイントを使って実装する場合
        # result += chr((ord(message[i]) + ord(key[i])) %
        #               len(ALPHABET) + ord("A"))

    return result

# 復号化用の関数


def decrypt(cipher_text: str, key: str) -> str:
    result = ""
    for i, char in enumerate(cipher_text):
        # スペース等はスキップする
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) -
                 ALPHABET.index(key[i]) + len(ALPHABET)) % len(ALPHABET)
        # 復号化したアルファベットをresultに追加していく
        result += ALPHABET[index]

        # unicodeのコードポイントを使って実装する場合
        # result += chr((ord(cipher_text[i]) - ord(key[i]) +
        #               len(ALPHABET)) % len(ALPHABET) + ord("A"))

    return result


# テスト
if __name__ == "__main__":
    # 元の文字列
    t = "OPERATION STRIX"
    # 元の文字列と同じ長さのキー（文字列）を作成
    k = generate_key(t, "BECKY")
    # print(generate_key("OPERATION STRIX", "BECKY"))
    # print(encrypt("ABCDXYZ", "MORNING"))
    # 作成したキーを使って暗号化する
    e = encrypt(t, k)
    print("暗号化した文字列：" + e)
    # 復号化する
    d = decrypt(e, k)
    print("復号化した文字列：" + d)
