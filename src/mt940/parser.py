from ply import lex, yacc


class ParserError(RuntimeError): pass


tokens = (
    "FIELD_SEPARATOR",
    "NEWLINE",
    "TERMINAL_FIELD",
    "COLON",
    "NUMERIC",
    "ALPHANUMERIC"
)

literals = "{}/,"


def t_FIELD_SEPARATOR(t):
    r"(?m)\n:"
    t.value = None
    return t


def t_TERMINAL_FIELD(t):
    r"(?m)\n-"
    t.value = None
    return t


def t_NEWLINE(t):
    r"(?m)\n"
    t.value = "\n"
    return t


def t_COLON(t):
    r":"
    t.value = ":"
    return t


def t_NUMERIC(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_ALPHANUMERIC(t):
    r"[A-Z0-9 \(\)]+"
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


def p_data_chunk0(p):
    """
    data_chunk : NUMERIC
               | ALPHANUMERIC
    """
    p[0] = str(p[1])


def p_data_chunk1(p):
    """
    data_chunk : data_chunk data_chunk
    """
    p[0] = p[1] + p[2]


def p_header_block(p):
    """
    header_block : "{" data_chunk COLON data_chunk "}"
                 | "{" data_chunk COLON fields "}"
                 | "{" data_chunk COLON swift_message "}"
    """
    p[0] = (p[2], p[4])


def p_fields0(p):
    """
    fields : TERMINAL_FIELD
    """
    p[0] = []


def p_fields1(p):
    """
    fields : value_fields TERMINAL_FIELD
    """
    p[0] = p[1]


def p_value_fields0(p):
    """
    value_fields : value_field
    """
    p[0] = [p[1]]


def p_value_fields1(p):
    """
    value_fields : value_fields value_field
    """
    p[0] = p[1] + [p[2]]


def p_value_field(p):
    """
    value_field : FIELD_SEPARATOR data_chunk COLON field_data
    """
    p[0] = (str(p[2]), p[4])


def p_field_data0(p):
    """
    field_data : data_chunk
    """
    p[0] = p[1]


def p_subfield_separator(p):
    """
    subfield_separator : COLON
                       | NEWLINE
                       | "/"
                       | ","
    """
    p[0] = p[1]


def p_field_data1(p):
    """
    field_data : field_data subfield_separator data_chunk
    """
    p[0] = p[1] + p[2] + p[3]


yacc.yacc()


def tokenize(message):
    output = []
    lex.input(message)
    for tok in iter(lex.token, None):
        output.append((tok.type, tok.value))
    return output


def parse(message, debug=False):
    return yacc.parse(message, debug=debug)
