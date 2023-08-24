def validIPAddresses(string):
    output = set()

    for i1 in range(1, 4):
        for i2 in range(1, 4):
            for i3 in range(1, 4):
                firstNumber = string[0:i1]
                secondNumber = string[i1 : i1 + i2]
                thirdNumber = string[i1 + i2 : i1 + i2 + i3]
                forthNumber = string[i1 + i2 + i3 :]

                if len(firstNumber) >= 2 and firstNumber[0] == "0":
                    continue
                if len(secondNumber) >= 2 and secondNumber[0] == "0":
                    continue
                if len(thirdNumber) >= 2 and thirdNumber[0] == "0":
                    continue
                if len(forthNumber) >= 2 and forthNumber[0] == "0":
                    continue

                if firstNumber == "":
                    continue
                if secondNumber == "":
                    continue
                if thirdNumber == "":
                    continue
                if forthNumber == "":
                    continue

                if (
                    int(firstNumber) <= 255
                    and int(secondNumber) <= 255
                    and int(thirdNumber) <= 255
                    and int(forthNumber) <= 255
                ):
                    ip = f"{firstNumber}.{secondNumber}.{thirdNumber}.{forthNumber}"
                    output.add(ip)
    return output
