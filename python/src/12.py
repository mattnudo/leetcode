


def intToRoman(number:int) -> str:
    intToRomanMap = {1:'|', 5:"V", 10:'X', 50:"L", 100:"C", 500:"D", 1000:"M"}
    if( not number):
        return ""
    numerals = list(intToRomanMap.keys())
    numerals.sort(reverse=True)
    print(numerals)
    result=""
    for numeral in numerals:
        tuple = divmod(number, numeral)
        result+=intToRomanMap[numeral]*tuple[0]
        number -= tuple[0]*numeral
    return result


#formulate a map of roman numerals to ints
#mod the number by each key in the map, adding the number corresponding roman numeral to the string, 
# #decrement number by what is captured until the number is reduced to 0

print(intToRoman(6959))

help(map)