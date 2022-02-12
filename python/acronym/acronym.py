import re


def abbreviate(words):
    pattern_to_del = re.compile(r'[!"#$%&()*+,-./:;<=>?@[\]^_{|}~]')
    lst = pattern_to_del.sub(' ', words).title().split()
    return ''.join([word[0] for word in lst])
