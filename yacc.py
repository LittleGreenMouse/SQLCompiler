import ply.yacc as yacc
import pymysql
import sys

from lex import tokens


def p_start(p):
    """start : statement"""
    sql = p[1]
    sql = sql.split('\n')
    for ret in sql:
        if ret != '':
            print(ret)
            if ret != 'EXIT;':
                execute_sql(ret)
            else:
                close()


def p_statement(p):
    """
    statement :
              | create_db statement
              | show_db statement
              | drop_db statement
              | use_db statement
              | create_tb statement
              | show_tb statement
              | drop_tb statement
              | insert_tb statement
              | delete_tb statement
              | update_tb statement
              | select_tb statement
              | exit_db statement
    """
    try:
        p[0] = p[1] + '\n' + p[2]
    except IndexError:
        p[0] = ''
    return p


def p_create_db(p):
    """create_db : create database id semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4]
    return p


def p_show_db(p):
    """show_db : show databases semicolon"""
    p[0] = p[1] + ' ' + p[2] + p[3]
    return p


def p_drop_db(p):
    """drop_db : drop database id semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4]
    return p


def p_use_db(p):
    """use_db : use id semicolon"""
    p[0] = p[1] + ' ' + p[2] + p[3]
    return p


def p_create_tb(p):
    """create_tb : create table id left_paren cols right_paren semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + p[5] + p[6] + p[7]


def p_cols(p):
    """cols : id type col"""
    p[0] = p[1] + ' ' + p[2] + p[3]
    return p


def p_type(p):
    """
    type : int
         | char left_paren number right_paren
    """
    if p[1] == 'INT':
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2] + p[3] + p[4]
    return p


def p_col(p):
    """
    col :
        | comma id type col
    """
    try:
        p[0] = p[1]
        p[0] += ' ' + p[2] + ' ' + p[3]
        try:
            p[0] += p[4]
        except IndexError:
            print('right')
    except IndexError:
        p[0] = ''
    return p


def p_show_tb(p):
    """show_tb : show tables semicolon"""
    p[0] = p[1] + ' ' + p[2] + p[3]
    return p


def p_drop_tb(p):
    """drop_tb : drop table id semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4]
    return p


def p_insert_tb(p):
    """insert_tb : insert into tb_name values left_paren value_cols right_paren semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + p[6] + p[7] + p[8]
    return p


def p_tb_name(p):
    """
    tb_name : id
            | id left_paren id_cols right_paren
    """
    p[0] = p[1]
    try:
        p[0] += p[2] + p[3] + p[4]
    except IndexError:
        p[0] += ''
    return p


def p_id_cols(p):
    """id_cols : id id_col"""
    p[0] = p[1] + p[2]
    return p


def p_id_col(p):
    """
    id_col :
           | comma id id_col
    """
    try:
        p[0] = p[1] + ' ' + p[2] + p[3]
    except IndexError:
        p[0] = ''
    return p


def p_value_cols(p):
    """
    value_cols : string value_col
               | number value_col
    """
    p[0] = p[1] + p[2]
    return p


def p_value_col(p):
    """
    value_col :
              | comma string value_col
              | comma number value_col
    """
    try:
        p[0] = p[1] + ' ' + p[2] + p[3]
    except IndexError:
        p[0] = ''
    return p


def p_delete_tb(p):
    """delete_tb : delete from id where conditions semicolon"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + p[6]
    return p


def p_conditions(p):
    """
    conditions : condition_col
               | left_paren conditions right_paren condition
    """
    p[0] = p[1]
    try:
        p[0] += p[2] + p[3] + p[4]
    except IndexError:
        p[0] += ''
    return p


def p_condition_col(p):
    """
    condition_col : id compare id
                  | id compare number
                  | id compare string
                  | number compare id
                  | number compare string
                  | string compare id
                  | string compare string
    """
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
    return p


def p_condition(p):
    """
    condition :
              | logic left_paren condition_col right_paren condition
    """
    try:
        p[0] = ' ' + p[1] + ' ' + p[2] + p[3] + p[4] + p[5]
    except IndexError:
        p[0] = ''
    return p


def p_update_tb(p):
    """
    update_tb : update id set update_cols semicolon
              | update id set update_cols where conditions semicolon
    """
    try:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + ' ' + p[6] + p[7]
    except IndexError:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + p[5]
    return p


def p_update_cols(p):
    """
    update_cols : id compare number update_col
                | id compare string update_col
    """
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4]
    if p[2] != '=':
        p_error(p)
        sys.exit()  
    return p


def p_update_col(p):
    """
    update_col :
               | comma id compare number update_col
               | comma id compare string update_col
    """
    try:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + p[5]
        if p[3] != '=':
            p_error(p)
            sys.exit()
    except IndexError:
        p[0] = ''
    return p


def p_select_tb(p):
    """
    select_tb : select all from id_cols semicolon
              | select id_cols from id_cols semicolon
              | select all from id_cols where conditions semicolon
              | select id_cols from id_cols where conditions semicolon
    """
    try:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + ' ' + p[6] + p[7]
    except IndexError:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + p[5]
    return p


def p_exit_db(p):
    """exit_db : exit semicolon"""
    p[0] = p[1] + p[2]
    return p


def p_error(p):
    if isinstance(p, yacc.YaccProduction):
        print("Wrong assignment symbol in '%s'" % p[0])
    elif p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def connect_db():
    global conn
    global cur
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='mysql', db='mysql')
    cur = conn.cursor()


def execute_sql(sql):
    cur.execute(sql)
    for ret in cur:
        print(ret)


def close():
    cur.close()
    conn.close()
    sys.exit()


if __name__ == '__main__':
    parser = yacc.yacc()

    connect_db()

    in_type = input("choose where date is from:\n1. file\n2. terminal\ninput: ")
    if in_type == '1':
        with open("testData.txt", "r") as f:
            s = f.read()
        parser.parse(s)
    elif in_type == '2':
        while True:
            try:
                s = input('SQL > ')
            except EOFError:
                break
            if not s:
                continue
            parser.parse(s)
