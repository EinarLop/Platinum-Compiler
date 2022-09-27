from pickle import TRUE
from ply.lex import lex
from ply.yacc import yacc

reserved_words = {
    'class' : 'CLASS',
    'main' : 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'func':'FUNC',
    'return':'RETURN',
    'read':'READ',
    'write':'WRITE',
    'int':'INT',
    'float':'FLOAT',
    'var':'VAR',
    'void':'VOID',
    'classes':'CLASSES',
    'vars':'VARS',
    'functions':'FUNCTIONS',
    'cl':'CL',
    'new':'NEW',
}

tokens =  ['ID', 'CTEI', 'CTEF', 'SIGNBOARD', 'COLON',
           'PERIOD', 'COMMA', 'SEMICOLON', 'LEFTCURLYBRACE',
           'RIGHTCURLYBRACE', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS',
           'GT', 'LT', 'GTOE', 'LTOE','NE', 'EQUAL', 'PLUS' , 'MINUS', 
           'MULTIPLICATION', 'DIVISION', 'AND', 'OR'] + list(reserved_words.values())


t_ignore = ' \t'
t_CTEI = r'[0-9]+'
t_CTEF = r'[+-]?([0-9]*[.])?[0-9]+'
t_SIGNBOARD = r'["][a-zA-Z_][a-zA-Z0-9_]*["]'
t_COLON = r'\:'
t_PERIOD = r'\.'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LEFTCURLYBRACE = r'\{'
t_RIGHTCURLYBRACE = r'\}'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_GT = r'\>'
t_LT = r'\<'
t_GTOE = r'[>=]'
t_LTOE = r'[<=]'
t_NE = r'[<>]'
t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_AND = r'[&&]'
t_OR = r'[||]'

def t_CLASS(t):
    r'class'
    t.type = reserved_words.get(t.value,'class')   
    return t

def t_MAIN(t):
    r'main'
    t.type = reserved_words.get(t.value,'main')   
    return t

def t_IF(t):
    r'if'
    t.type = reserved_words.get(t.value,'if')   
    return t

def t_ELSE(t):
    r'else'
    t.type = reserved_words.get(t.value,'else')   
    return t

def t_FOR(t):
    r'for'
    t.type = reserved_words.get(t.value,'for')   
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved_words.get(t.value,'while')   
    return t

def t_FUNC(t):
    r'func'
    t.type = reserved_words.get(t.value,'func')   
    return t

def t_RETURN(t):
    r'return'
    t.type = reserved_words.get(t.value,'return')   
    return t

def t_READ(t):
    r'read'
    t.type = reserved_words.get(t.value,'read')   
    return t

def t_WRITE(t):
    r'write'
    t.type = reserved_words.get(t.value,'write')   
    return t

def t_INT(t):
    r'int'
    t.type = reserved_words.get(t.value,'int')   
    return t

def t_FLOAT(t):
    r'float'
    t.type = reserved_words.get(t.value,'float')   
    return t

def t_VAR(t):
    r'var'
    t.type = reserved_words.get(t.value,'var')   
    return t

def t_VOID(t):
    r'void'
    t.type = reserved_words.get(t.value,'void')   
    return t

def t_CLASSES(t):
    r'classes'
    t.type = reserved_words.get(t.value,'classes')   
    return t

def t_VARS(t):
    r'vars'
    t.type = reserved_words.get(t.value,'vars')   
    return t

def t_FUNCTION(t):
    r'function'
    t.type = reserved_words.get(t.value,'function')   
    return t

def t_CL(t):
    r'cl'
    t.type = reserved_words.get(t.value,'cl')   
    return t

def t_NEW(t):
    r'new'
    t.type = reserved_words.get(t.value,'new')   
    return t

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

lexer = lex()






