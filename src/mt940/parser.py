from ply import lex, yacc

class ParserError(RuntimeError): pass

tokens = (
    "FIELD_SEPARATOR",
    "TERMINAL_FIELD",
    "COLON",
    "NUMERIC",
    "ALPHANUMERIC",
    "FIELD_DATA"
)

literals = "{}"


def t_FIELD_SEPARATOR(t):
    r"\n:"
    t.value = None
    return t


def t_TERMINAL_FIELD(t):
    r"\n-"
    t.value = None
    return t


def t_COLON(t):
    r":"
    t.value = None
    return t

def t_NUMERIC(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_ALPHANUMERIC(t):
    r"[A-Z0-9]+"
    t.value = str(t.value)
    return t

def t_FIELD_DATA(t):
    r"(?<=:)([[0-9A-Z\s\/:,\(\) \.]+)(?=\}|\n[\-:])"
    t.value = str(t.value)
    return t

def t_error(t):
    raise ValueError("Cannot parse text %r" % t.value)

lex.lex()

def p_error(p):
    raise ParserError("Syntax error at '%s (%s)'" % (p.value, p.type))


def p_swift_message(p):
    """
    swift_message : blocks
    """
    p[0] = dict(production for production in p[1])

def p_blocks0(p):
    """
    blocks : blocks header_block
    """
    p[0] = p[1] + [p[2]]

def p_blocks1(p):
    """
    blocks : header_block
    """
    p[0] = [p[1]]

def p_header_block(p):
    """
    header_block : "{" NUMERIC COLON FIELD_DATA "}"
                 | "{" NUMERIC COLON ALPHANUMERIC "}"
                 | "{" NUMERIC COLON fields "}"
    """
    p[0] = (p[2], p[4])


def p_fields0(p):
    """
    fields : TERMINAL_FIELD
    """
    p[0] = {}

def p_fields1(p):
    """
    fields : value_fields TERMINAL_FIELD
    """
    p[0] = dict(p[1])

def p_value_fields0(p):
    """
    value_fields : value_fields value_field
    """
    p[0] = p[1] + [p[2]]

def p_value_fields1(p):
    """
    value_fields : value_field
    """
    p[0] = [p[1]]

def p_value_field(p):
    """
    value_field : FIELD_SEPARATOR ALPHANUMERIC COLON FIELD_DATA
                | FIELD_SEPARATOR ALPHANUMERIC COLON ALPHANUMERIC
                | FIELD_SEPARATOR NUMERIC COLON ALPHANUMERIC
    """
    p[0] = (str(p[2]), p[4])


yacc.yacc()

def tokenize(message):
    output = []
    lex.input(message)
    for tok in iter(lex.token, None):
        output.append((tok.type, tok.value))
    return output

def parse(message):
    return yacc.parse(message, debug=False)
