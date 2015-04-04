from ply import lex, yacc

class ParserError(RuntimeError): pass

tokens = (

    "OPEN_BRACKET",
    "CLOSE_BRACKET",
    "NUMERIC",
    "ALPHANUMERIC",
    "SLASH",

    "STATEMENT_NO_SEQ_NO_TAG",
    "REFERENCE_NO_TAG",
)

t_OPEN_BRACKET = r"{"
t_CLOSE_BRACKET = r"}"
t_SLASH = "/"
t_ignore = "\n"

t_STATEMENT_NO_SEQ_NO_TAG = ":28C:"
t_REFERENCE_NO_TAG = ":20:"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

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
    block : OPEN_BRACKET fields CLOSE_BRACKET
    """
    p[0] = {k:v for (k,v) in p[2]}

def p_fields_list(p):
    """
    fields : fields single_field
    """
    p[0] = p[1] + [p[2], ]


def p_field(p):
    """
    fields : single_field
    """
    result = list()
    result.append(p[1])
    p[0] = result


def p_single_field(p):
    """
    single_field : statement_no_sequence_no_field
                 | reference_no_field
    """
    p[0]=p[1]

def p_statement_no_sequence_no_field(p):
    """
    statement_no_sequence_no_field : STATEMENT_NO_SEQ_NO_TAG NUMERIC SLASH NUMERIC
    """
    p[0] = ("Statement Number/Sequence Number", (p[2],p[4]))

def p_reference_no_field(p):
    """
    reference_no_field : REFERENCE_NO_TAG NUMERIC
    """
    p[0] = ("Reference Number", p[2])


yacc.yacc()

def tokenize(message):
    output = []
    lex.input(message)
    for tok in iter(lex.token, None):
        output.append((tok.type, tok.value))
    return output

def parse(message):
    return yacc.parse(message)
