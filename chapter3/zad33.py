decimal = int(input("Enter decimal number: "))
binary = ""

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print(decimal, "(10) =", binary, "(2)")