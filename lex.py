import ply.lex as lex

tokens = [
    'create',
    'use',
    'show',
    'insert',
    'select',
    'update',
    'delete',
    'drop',
    'exit',
    'databases',
    'database',
    'tables',
    'table',
    'into',
    'values',
    'from',
    'all',
    'where',
    'set',
    'compare',
    'logic',
    'char',
    'int',
    'id',
    'number',
    'string',
    'comma',
    'semicolon',
    'left_paren',
    'right_paren'
]


def t_create(t):
    r"""(C|c)(R|r)(E|e)(A|a)(T|t)(E|e)"""
    t.value = "CREATE"
    return t


def t_use(t):
    r"""(U|u)(S|s)(E|e)"""
    t.value = "USE"
    return t


def t_show(t):
    r"""(S|s)(H|h)(O|o)(W|w)"""
    t.value = "SHOW"
    return t


def t_insert(t):
    r"""(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)"""
    t.value = "INSERT"
    return t


def t_select(t):
    r"""(S|s)(E|e)(L|l)(E|e)(C|c)(T|t)"""
    t.value = "SELECT"
    return t


def t_update(t):
    r"""(U|u)(P|p)(D|d)(A|a)(T|t)(E|e)"""
    t.value = 'UPDATE'
    return t


def t_delete(t):
    r"""(D|d)(E|e)(L|l)(E|e)(T|t)(E|e)"""
    t.value = "DELETE"
    return t


def t_drop(t):
    r"""(D|d)(R|r)(O|o)(P|p)"""
    t.value = "DROP"
    return t


def t_exit(t):
    r"""(E|e)(X|x)(I|i)(T|t)"""
    t.value = "EXIT"
    return t


def t_databases(t):
    r"""(D|d)(A|a)(T|t)(A|a)(B|b)(A|a)(S|s)(E|e)(S|s)"""
    t.value = "DATABASES"
    return t


def t_database(t):
    r"""(D|d)(A|a)(T|t)(A|a)(B|b)(A|a)(S|s)(E|e)"""
    t.value = "DATABASE"
    return t


def t_tables(t):
    r"""(T|t)(A|a)(B|b)(L|l)(E|e)(S|s)"""
    t.value = "TABLES"
    return t


def t_table(t):
    r"""(T|t)(A|a)(B|b)(L|l)(E|e)"""
    t.value = "TABLE"
    return t


def t_into(t):
    r"""(I|i)(N|n)(T|t)(O|o)"""
    t.value = "INTO"
    return t


def t_values(t):
    r"""(V|v)(A|a)(L|l)(U|u)(E|e)(S|s)"""
    t.value = "VALUES"
    return t


def t_from(t):
    r"""(F|f)(R|r)(O|o)(M|m)"""
    t.value = "FROM"
    return t


def t_all(t):
    r"""\*"""
    return t


def t_where(t):
    r"""(W|w)(H|h)(E|e)(R|r)(E|e)"""
    t.value = "WHERE"
    return t


def t_set(t):
    r"""(S|s)(E|e)(T|t)"""
    t.value = "SET"
    return t


def t_compare(t):
    r"""(=)|(!=)|(>)|(<)|(>=)|(<=)"""
    return t


def t_logic(t):
    r"""((A|a)(N|n)(D|d))|((O|o)(R|r))"""
    return t


def t_char(t):
    r"""(C|c)(H|h)(A|a)(R|r)"""
    t.value = "CHAR"
    return t


def t_int(t):
    r"""(I|i)(N|n)(T|t)"""
    t.value = "INT"
    return t


def t_id(t):
    r"""[A-Za-z][A-Za-z0-9_]*"""
    return t


def t_number(t):
    r"""[0-9]+"""
    return t


def t_string(t):
    r"""\'[A-Za-z][A-Za-z0-9_]*\'"""
    return t


def t_comma(t):
    r""","""
    return t


def t_semicolon(t):
    r""";"""
    return t


def t_left_paren(t):
    r"""\("""
    return t


def t_right_paren(t):
    r"""\)"""
    return t


t_ignore = " \t\n"


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Illegal character '%s' in line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


lexer = lex.lex()

# with open('testData.txt', 'r') as f:
#     s = f.read()
#
# lexer.input(s)
#
# for token in lexer:
#     print(token)
