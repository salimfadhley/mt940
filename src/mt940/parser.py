from ply import lex

tokens = (
    "OPEN_BRACKET",
    "CLOSE_BRACKET"
)

t_OPEN_BRACKET = "{"
t_CLOSE_BRACKET = "}"


def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


lex.lex()


def parse(message):
    lex.input(message)
    for tok in iter(lex.token, None):
        print(repr(tok.type), repr(tok.value))

if __name__ == '__main__':
    print ("dfdd" "dfdfdfs" "gghhh")
    #parse("{")
    parse("{{{{}{{")