# シーザー暗号：アルファベット標記を３つシフトさせたものを送る。
# 例）art → duw

# asciiの文字を使えるようにする
import string


def caesar_cipher(text: str, shift: int) -> str:
    # シフト後の文字を入れる変数
    result = ""
    # 一つ一つの文字を取ってくる
    for char in text:
        # 大文字の場合
        if char.isupper():
            # 大文字のアルファベット２６文字を表示
            alphabet = string.ascii_uppercase
        # 小文字の場合
        elif char.islower():
            # 小文字のアルファベット２６文字を表示
            alphabet = string.ascii_lowercase
        # アルファベットでない場合
        else:
            # 取り出した１文字をresultに加える
            result += char
            # 次のループに行く
            continue

        # 取り出したアルファベットを3つ分シフトした時の文字のインデックスを取得(x,y,zの時にエラーにならないように、全体のアルファベット数（２６）で割った時の余りをインデックスとする)
        index = (alphabet.index(char) + shift) % len(alphabet)
        # 取得したインデックスに対応するアルファベットをresultに追加
        result += alphabet[index]
    # 結果を返す
    return result


if __name__ == "__main__":
    print(caesar_cipher("animal", 3))
