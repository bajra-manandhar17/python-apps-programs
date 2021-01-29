# Convert integers to roman numbers from 1 to 1000

# 13 Numbers are including to include exceptions like '4'.
# The input number is divided with the equivalent roman number
# If the quotient is not 0, the program will loop for all the 13 roman numbers.

input = int(input("Enter number to convert: "))

dict = {1000: 'N',
        900: 'CM',
        600: 'DC',
        500: 'D',
        400: 'XD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}

order = [1000, 900, 500, 400, 100, 90, 40, 10, 9, 5, 4, 1]

for x in order:
    if input != 0:
        quotient = input // x

        # Displays output if quotient is not 0
        if quotient != 0:
            for y in range(quotient):
                print(dict[x], end="")

        # input is updated with remainder
        input = input % x
