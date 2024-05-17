def int_to_roman_(num):
    dict_storage = {
    1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9  : "IX",
    5  : "V",
    4  : "IV",
    1  : "I"
    }
    result = ''
    for value , symbol in dict_storage.items():
        while num >= value:
            result += symbol
            num -= value
    return result

number = int(input("Enter any number: "))
roman_representation = int_to_roman_(number)
print(f"The Roman numeral representation of {number} is: {roman_representation}")