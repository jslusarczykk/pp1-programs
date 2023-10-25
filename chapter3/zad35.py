for num in range(1, 31):
    output = ""
    if num % 3 == 0:
        output += "THREE"
    if num % 5 == 0:
        output += "FIVE"
    if num % 3 == 0 and num % 5 == 0:
        output += " BINGO"
    print(output, end=" ")

print()