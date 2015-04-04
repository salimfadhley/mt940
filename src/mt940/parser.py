from ply import lex

tokens = (
    "OPEN_BRACKET",
    "CLOSE_BRACKET",
    "NUMERIC",
    "ALPHANUMERIC",
    "COLON"
)

t_OPEN_BRACKET = r"{"
t_CLOSE_BRACKET = r"}"
t_COLON = r":"

def t_ALPHANUMERIC(t):
    r"[\w\d]+"
    t.value = str(t.value)
    return t

def t_NUMERIC(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


lex.lex()


def parse(message):
    lex.input(message)
    for tok in iter(lex.token, None):
        print(repr(tok.type), repr(tok.value))


if __name__ == '__main__':
    #parse("{")
    parse("{23:ABC123}")