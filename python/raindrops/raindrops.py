def convert(number):
    pairs = [[3, "Pling"], [5, "Plang"], [7, "Plong"]]
    s = ''.join([value for num, value in pairs if number % num == 0])
    return s or str(number)
