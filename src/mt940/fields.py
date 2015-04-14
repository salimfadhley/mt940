"""
Status

M - mandatory,
O - optionalFormat

n - only digits
a - only letters
c - alphanumerical
x - any alphanumerical characters including commas, spaces, etc.
d - amount including a comma as a decimal separator

Example:

2n - up to 2 digits
3!a - always 3 letters
15*65x - up to 15 lines, 65 characters each
"""
import re

FIELDS = {
    "61": '6!n4!n2a1!a15dN3!a16x//16x34x'
}

FIELD_DEF = "(\\/*)((\d+)*)?(\d)(!)?([nacxd])"

TEXT_CLASSES = {
    'n':r'\d',
    'a':r'[A-Z]',
    'c':r'[A-Z\d]',
    'd':r'[\d,]',
    'x':r'[A-Z\d\s,]',
}

def get_regex_parts_from_spec(spec):
    parts = re.findall(FIELD_DEF, spec)
    for part in parts:
        slashes = part[0]
        length = int(part[3])
        min_length = length if part[4] == '!' else 0
        text_class = TEXT_CLASSES[part[5]]

        yield "%s(%s{%i,%i})" % (re.escape(slashes), text_class, min_length, length)

def get_regex_from_spec(spec):
    return "".join(get_regex_parts_from_spec(spec))


def get_field_regex(field_code):
    spec = FIELDS[field_code]
    return get_regex_from_spec(spec)



if __name__ == '__main__':
    print(get_regex_from_spec("2!n"))