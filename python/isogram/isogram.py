def is_isogram(s):
    chars = [char.lower() for char in s if char.isalpha()]
    return (len(chars) == len(set(chars)))
