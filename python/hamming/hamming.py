def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("Strings are differen or zero lenght")
    return sum(key != value for key, value in zip(strand_a, strand_b))
