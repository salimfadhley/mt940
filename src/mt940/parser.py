from ply import lex, yacc

class ParserError(RuntimeError): pass

tokens = (
    "NUMERIC",
    "ALPHANUMERIC",
    "NEWLINE",
    "FIELD_DATA"
)

literals = "{}:-"
t_ignore = '\r'


# t_STATEMENT_NO_SEQ_NO_TAG = ":28C:"
# t_REFERENCE_NO_TAG = ":20:"

def t_NEWLINE(t):
    r"\n+"
    t.value = "NEWLINE"
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
    r"(?<=:)([[0-9A-Z\s\/:,\(\) ]+)(?=\}|\n[\-:])"
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
    header_block : "{" NUMERIC ":" FIELD_DATA "}"
                 | "{" NUMERIC ":" ALPHANUMERIC "}"
                 | "{" NUMERIC ":" fields "}"
    """
    p[0] = (p[2], p[4])


def p_fields0(p):
    """
    fields : terminal_field
    """
    p[0] = {}

def p_fields1(p):
    """
    fields : value_fields terminal_field
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
    value_field : NEWLINE ":" ALPHANUMERIC ":" FIELD_DATA
                | NEWLINE ":" ALPHANUMERIC ":" ALPHANUMERIC
                | NEWLINE ":" NUMERIC ":" ALPHANUMERIC
    """
    p[0] = (str(p[3]), p[5])

def p_terminal_field(p):
    """
    terminal_field : NEWLINE "-"
    """
    pass


yacc.yacc()

def tokenize(message):
    output = []
    lex.input(message)
    for tok in iter(lex.token, None):
        output.append((tok.type, tok.value))
    return output

def parse(message):
    return yacc.parse(message, debug=False)
