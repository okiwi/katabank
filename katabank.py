DIGIT_MAP = {
    "   \n  |\n  |\n   ":1,
    " _ \n _|\n|_ \n   ":2,
    " _ \n _|\n _|\n   ":3,
    "   \n|_|\n  |\n   ":4,
    " _ \n|_ \n _|\n   ":5,
    " _ \n|_ \n|_|\n   ":6,
    " _ \n  |\n  |\n   ":7,
    " _ \n|_|\n|_|\n   ":8,
    " _ \n|_|\n _|\n   ":9,
}

def ocrMachine(pDigit):
    splitedDigit = splitDigits(pDigit)
    result = ""
    for digit in splitedDigit:
        result += str(DIGIT_MAP[digit])
    return int(result)

def splitDigits(pDigits):
    lines = pDigits.split("\n")
    digit = []
    for line in lines:
        digit.append([line[i:i+3] for i in range(0, len(line), 3)])
    digits = []
    for n in range(len(digit[0])):
        digits.append("\n".join([e[n] for e in digit]))
    return digits

