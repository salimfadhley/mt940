from ply import lex, yacc

class ParserError(RuntimeError): pass

tokens = (

    "OPEN_BRACKET",
    "CLOSE_BRACKET",
    "NUMERIC",
    "ALPHANUMERIC",
    "COLON",
    "SLASH",
    "STATEMENT_NO_SEQ_NO",
)

t_OPEN_BRACKET = r"{"
t_CLOSE_BRACKET = r"}"
t_COLON = r":"
t_SLASH = r"/"
t_STATEMENT_NO_SEQ_NO = r"28C"

def t_NUMERIC(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_ALPHANUMERIC(t):
    r"[\w\d]+"
    t.value = str(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text %r" % t.value)

lex.lex()

def p_error(p):
    raise ParserError("Syntax error at '%s'" % p.value)

def p_swift_message(p):
    """
    swift_message : block
                  | empty_block
    """
    p[0] = p[1]

def p_empty_block(p):
    """
    empty_block : OPEN_BRACKET CLOSE_BRACKET
    """
    p[0] = {}

def p_block(p):
    """
    block : OPEN_BRACKET single_field CLOSE_BRACKET
    """
    p[0] = {}

def p_single_field(p):
    """
    single_field : statement_seq_field
    """
    p[0]=p[1]

def p_statement_seq_field(p):
    """
    statement_seq_field : COLON STATEMENT_NO_SEQ_NO COLON NUMERIC SLASH NUMERIC
    """
    p[0] = ("Statement Number/Sequence Number", p[4], p[6])

yacc.yacc()

def tokenize(message):
    output = []
    lex.input(message)
    for tok in iter(lex.token, None):
        output.append((tok.type, tok.value))
    return output

def parse(message):
    return yacc.parse(message)
