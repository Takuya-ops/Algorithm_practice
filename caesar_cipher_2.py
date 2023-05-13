# stringモジュールを使わない場合
from typing import Generator, Tuple


def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    len_alphabet = ord("Z") - ord("A") + 1
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - ord("A")) %
                          len_alphabet + ord("A"))
        elif char.islower():
            result += chr((ord(char) + shift - ord("a")) %
                          len_alphabet + ord("a"))
        else:
            result += char
    return result

# 解読用のファンクション(すべてのシフトしたパターンを表示させる)


def caesar_cipher_hack(text: str) -> Generator[Tuple[int: str], None, None]:
    # アルファベットの長さを取得する（stringモジュールが使えない場合）
    len_alphabet = ord("Z") - ord("A") + 1
    # アルファベットの長さを取得する（stringモジュールが使える場合）
    # len_alphabet = len(string.ascii_uppercase
    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            if char.isupper():
                index = ord(char) - candidate_shift
                if index < ord("A"):
                    index += len_alphabet
                reverted += chr(index)
            elif char.islower():
                index = ord(char) - candidate_shift
                if index < ord("a"):
                    index += len_alphabet
                reverted += chr(index)
            else:
                reverted += char
        yield candidate_shift, reverted


if __name__ == "__main__":
    print("暗号化したもの：" + caesar_cipher("Programming practice", 3))
    # デクリプト(復号化)
    e = caesar_cipher("Programming practice", 3)
    print("復号化したもの：" + caesar_cipher(e, -3))

    # 総当たりでパターンを表示させ見つける
    for shift_num, decrypted in caesar_cipher_hack(e):
        print(f"{shift_num:2d}", decrypted)
