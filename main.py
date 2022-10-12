from pickle import TRUE

from ply.lex import lex
from ply.yacc import yacc
from VarsTable import VarsTable
from SemanticCube import SemanticCube
from Function import Function
from FunctionsTable import FunctionsTable
from Parameter import Parameter
varsTable = VarsTable()
semanticCube = SemanticCube()
functionsTable= FunctionsTable()

reserved_words = {
    'classes':'CLASSES',
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
    'char': 'CHAR',
    'var':'VAR',
    'void':'VOID',
    'vars':'VARS',
    'functions':'FUNCTIONS',
    'cl':'CL',
    'new':'NEW',
    'do' : 'DO',
    'to' : 'TO'
}

tokens =  ['ID', 'CTEI', 'CTEF', 'SIGNBOARD', 'COLON',
           'PERIOD', 'COMMA', 'SEMICOLON', 'LEFTCURLYBRACE',
           'RIGHTCURLYBRACE', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS', 'LEFTBRACKET', 'RIGHTBRACKET',
           'GT', 'LT', 'GTOE', 'LTOE','NE', 'EQUALITY','EQUAL', 'PLUS' , 'MINUS',
           'MULTIPLICATION', 'DIVISION', 'AND', 'OR'] + list(reserved_words.values())



t_ignore = ' \t'
# ID'S MUST BE AT LEAST TWO CHARACTERS
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
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_GT = r'\>'
t_LT = r'\<'
t_GTOE = r'\>\='
t_LTOE = r'\<\='
t_NE = r'\<\>'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_AND = r'\&\&'
t_OR = r'\|\|'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]+'
    t.type = reserved_words.get(t.value,'ID')    # Check for reserved words
    return t

def t_CLASSES(t):
    r'classes'
    t.type = reserved_words.get(t.value,'classes')
    return t

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

def t_FUNCTIONS(t):
    r'functions'
    t.type = reserved_words.get(t.value,'functions')
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

def t_CHAR(t):
    r'char'
    t.type = reserved_words.get(t.value,'char')
    return t

def t_FLOAT(t):
    r'float'
    t.type = reserved_words.get(t.value,'float')
    return t

def t_VOID(t):
    r'void'
    t.type = reserved_words.get(t.value,'void')
    return t

def t_VARS(t):
    r'vars'
    t.type = reserved_words.get(t.value,'vars')
    return t

def t_VAR(t):
    r'var'
    t.type = reserved_words.get(t.value,'var')
    return t

def t_CL(t):
    r'cl'
    t.type = reserved_words.get(t.value,'cl')
    return t

def t_NEW(t):
    r'new'
    t.type = reserved_words.get(t.value,'new')
    return t

def t_DO(t):
    r'do'
    t.type = reserved_words.get(t.value,'do')
    return t

def t_TO(t):
    r'to'
    t.type = reserved_words.get(t.value,'to')
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EQUALITY(t):
    r'=='
    return t

def t_EQUAL(t):
    r'='
    return t

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

lexer = lex()

def p_main(p):
    '''
    main : CLASS MAIN LEFTCURLYBRACE CLASSES LEFTCURLYBRACE class_dec RIGHTCURLYBRACE VARS np_set_var_scope_global LEFTCURLYBRACE  var_dec  RIGHTCURLYBRACE FUNCTIONS LEFTCURLYBRACE func_dec RIGHTCURLYBRACE block RIGHTCURLYBRACE
    '''
    p[0] = ('rule main: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17])


def p_class_dec(p):
    '''
    class_dec : CLASS ID LEFTCURLYBRACE VARS np_set_var_scope_class LEFTCURLYBRACE var_dec RIGHTCURLYBRACE FUNCTIONS LEFTCURLYBRACE func_dec RIGHTCURLYBRACE RIGHTCURLYBRACE class_dec2
    '''
    p[0] = ('rule class_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13])

def p_class_dec2(p):
    '''
    class_dec2 : class_dec
               | empty
    '''
    p[0] = ('rule class_dec2: ', p[1])

def p_param(p):
    '''
    param : s_type ID param2
    '''
    p[0] = ('rule param: ', p[1], p[2], p[3])

def p_param2(p):
    '''
    param2 : COMMA param
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule param2: ', p[1], p[2])
    else:
        p[0] = ('rule param2: ', p[1])

def p_func_dec(p):
    '''
    func_dec : FUNC func_dec2 ID LEFTPARENTHESIS param RIGHTPARENTHESIS LEFTCURLYBRACE VARS np_set_var_scope_function LEFTCURLYBRACE var_dec RIGHTCURLYBRACE block RETURN h_exp RIGHTCURLYBRACE func_dec3
    '''
    p[0] = ('rule func_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15],p[16])

def p_func_dec2(p):
    '''
    func_dec2 : s_type
              | VOID
    '''
    p[0] = ('rule func_dec2: ', p[1])

def p_func_dec3(p):
    '''
    func_dec3 : func_dec
              | empty
    '''
    p[0] = ('rule func_dec3: ', p[1])

def p_var_dec(p):
    '''
    var_dec : VAR var_dec6 SEMICOLON np_save_var var_dec8
    '''
    p[0] = ('rule var_dec: ', p[1], p[2], p[3])

def p_var_dec2(p):
    '''
    var_dec2 : c_type var_dec4
    '''
    p[0] = ('rule var_dec2: ', p[1], p[2])

def p_var_dec3(p):
    '''
    var_dec3 : s_type var_dec4
    '''
    p[0] = ('rule var_dec3: ', p[1], p[2])

def p_var_dec4(p):
    '''
    var_dec4 : ID np_get_var_name COMMA np_save_var var_dec4
             | ID np_get_var_name var_dec5
    '''
    if (len(p) == 4):
        p[0] = ('rule var_dec4: ', p[1], p[2], p[3])
    elif(len(p) == 3):
        p[0] = ('rule var_dec4: ', p[1], p[2])
    else:
        p[0] = ('rule var_dec4: ', p[1])

def p_var_dec5(p):
    '''
    var_dec5 : LEFTBRACKET CTEI RIGHTBRACKET np_set_var_type_arr var_dec9
	         | LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET np_set_var_type_matrix var_dec9
             | empty
    '''
    if (len(p) == 7):
        p[0] = ('rule var_dec5: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    elif (len(p) == 4):
        p[0] = ('rule var_dec5: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule var_dec5: ', p[1])

def p_var_dec6(p):
    '''
    var_dec6 : var_dec2 var_dec7
             | var_dec3 var_dec7
    '''
    p[0] = ('rule var_dec6: ', p[1], p[2])

def p_var_dec7(p):
    '''
    var_dec7 : var_dec6
             | empty
    '''
    p[0] = ('rule var_dec7: ', p[1])

def p_var_dec8(p):
    '''
    var_dec8 : var_dec
             | empty
    '''
    p[0] = ('rule var_dec8: ', p[1])

def p_var_dec9(p):
    '''

    var_dec9 : COMMA np_save_var var_dec4
             | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule param2: ', p[1], p[2])
    else:
        p[0] = ('rule param2: ', p[1])

def p_factor(p):
    '''
    factor : LEFTPARENTHESIS h_exp RIGHTPARENTHESIS
           | CTEI
           | CTEF
           | variable
           | call
    '''
    if (len(p) == 4):
        p[0] = ('rule factor: ', p[1], p[2], p[3])
    elif(len(p) == 2):
        p[0] = ('rule factor: ', p[1])

def p_t(p):
    '''
    t : factor t2
    '''
    p[0] = ('rule term: ', p[1], p[2])

def p_t2(p):
    '''
    t2 : MULTIPLICATION t
       | DIVISION t
       | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule term2: ', p[1], p[2])
    else:
        p[0] = ('rule term2: ', p[1])

def p_exp(p):
    '''
    exp : t exp2
    '''
    p[0] = ('rule exp: ', p[1], p[2])

def p_exp2(p):
    '''
    exp2 : PLUS exp
         | MINUS exp
         | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule exp2: ', p[1], p[2])
    else:
        p[0] = ('rule exp2: ', p[1])

def p_s_exp(p):
    '''
    s_exp : exp s_exp2
    '''
    p[0] = ('rule s_exp2: ', p[1], p[2])

def p_s_exp2(p):
    '''
    s_exp2 : LT exp
           | GT exp
           | LTOE exp
           | GTOE exp
           | NE exp
           | EQUALITY exp
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule s_exp2: ', p[1], p[2])
    else:
        p[0] = ('rule s_exp2: ', p[1])

def p_h_exp(p):
    '''
    h_exp : s_exp h_exp2
    '''
    p[0] = ('rule h_exp: ', p[1],p[2])

def p_h_exp2(p):
    '''
    h_exp2 : AND s_exp h_exp2
           | OR s_exp h_exp2
           | empty
    '''
    if(len(p)  == 4):
        p[0] = ('rule h_exp2: ', p[1],p[2],p[3])
    else:
        p[0] = ('rule h_exp2: ', p[1])
def p_variable(p):
    '''
    variable : ID variable2
    '''
    p[0] = ('rule variable: ', p[1], p[2])

def p_variable2(p):
    '''
    variable2 : LEFTBRACKET CTEI RIGHTBRACKET variable3
              | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule variable2: ', p[1], p[2], p[3],p[4])
    elif(len(p) == 2):
        p[0] = ('rule variable2: ', p[1])

def p_variable3(p):
    '''
    variable3 : LEFTBRACKET CTEI RIGHTBRACKET
              | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule variable2: ', p[1], p[2], p[3])
    elif (len(p) == 2):
        p[0] = ('rule variable2: ', p[1])

def p_call_obj(p):
    '''
    call_obj : ID PERIOD ID LEFTPARENTHESIS call_obj2 RIGHTPARENTHESIS
    '''
    p[0] = ('rule call_obj: ', p[1], p[2], p[3],p[4],p[5],p[6])

def p_call_obj2(p):
    '''
    call_obj2 : call_obj3
              | empty
    '''
    p[0] = ('rule call_obj2: ', p[1])


def p_call_obj3(p):
    '''
    call_obj3 : h_exp call_obj4
              | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call_obj3: ', p[1], p[2])
    else:
        p[0] = ('rule call_obj3: ', p[1])

def p_call_obj4(p):
    '''
    call_obj4 : COMMA h_exp call_obj4
              | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule call_obj4: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call_obj4: ', p[1])


def p_call(p):
    '''
    call : ID LEFTPARENTHESIS call2 RIGHTPARENTHESIS
    '''
    p[0] = ('rule call: ', p[1], p[2], p[3],p[4])

def p_call2(p):
    '''
    call2 : h_exp call3
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call2:', p[1], p[2])
    else:
        p[0] = ('rule call2:', p[1])

def p_call3(p):
    '''
    call3 : COMMA h_exp call3
          | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule call3:', p[1], p[2], p[3])
    else:
        p[0] = ('rule call3:', p[1])

def p_c_type(p):
    '''
    c_type : CL COLON ID
    '''
    p[0] = ('rule c_type: ', p[1], p[2], p[3])

def p_s_type(p):
    '''
    s_type : INT np_get_var_type
	       | FLOAT np_get_var_type
	       | CHAR
    '''
    p[0] = ('rule s_type: ', p[1])

def p_assignment(p):
    '''
    assignment : variable EQUAL assignment2
    '''
    p[0] = ('rule assignment: ', p[1],p[2])

def p_assignment2(p):
    '''
    assignment2 : exp
                | NEW ID

    '''
    if(len(p) == 2):
        p[0] = ('rule assignment2 : ', p[1])
    else:
        p[0] = ('rule assignment2 : ', p[1],p[2])

def p_read(p):
    '''
    read : READ LEFTPARENTHESIS variable RIGHTPARENTHESIS

    '''
    p[0] = ('rule read : ', p[1],p[2])

def p_write(p):
    '''
    write : WRITE LEFTPARENTHESIS write2 RIGHTPARENTHESIS

    '''
    p[0] = ('rule write :',p[1],p[2],p[3],p[4])

def p_write2(p):
    '''
    write2 : h_exp write3
            | SIGNBOARD write3

    '''
    p[0] = ('rule write2 :',p[1],p[2])

def p_write3(p):
    '''
    write3 : COMMA h_exp
           | COMMA SIGNBOARD
           | empty

    '''
    if(len(p) == 3):
        p[0] = ('rule write3 :',p[1],p[2])
    else:
        p[0] = ('rule write3 :',p[1])

def p_condition(p):
    '''
    condition : IF LEFTPARENTHESIS h_exp RIGHTPARENTHESIS block condition2 SEMICOLON
    '''
    p[0] = ('rule condition: ', p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_condition2(p):
    '''
    condition2 : ELSE block
               | empty

    '''
    if(len(p) == 3):
        p[0] = ('rule condition2 : ', p[1],p[2])
    else:
        p[0] = ('rule condition2 : ', p[1])

def p_loop_w(p):
    '''
    loop_w : WHILE LEFTPARENTHESIS h_exp RIGHTPARENTHESIS DO block SEMICOLON

    '''
    p[0] = ('rule loopW : ', p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_loop_f(p):
    '''
    loop_f : FOR LEFTPARENTHESIS variable EQUAL h_exp TO h_exp RIGHTPARENTHESIS DO block

    '''

    p[0] = ('rule loopF : ', p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10])


def p_statement(p):
    '''
    statement : assignment
              | call
              | call_obj
              | read
              | write
              | condition
              | loop_w
              | loop_f

    '''
    p[0] = ('rule statement : ', p[1])

def p_block(p):
    '''
    block : LEFTCURLYBRACE statement block2 RIGHTCURLYBRACE

    '''
    p[0] = ('rule block : ', p[1],p[2],p[3],p[4])

def p_block2(p):
    '''
    block2 : statement block2
           | empty

    '''
    if(len(p) == 3):
        p[0] = ('rule block2 : ', p[1],p[2])
    else:
        p[0] = ('rule block2 : ', p[1])


def p_empty(p):
     'empty :'
     pass

def p_error(p):
    print(f'Syntax error at {p.value!r} on line {p.lineno} of type {p}')


##### NEURALGIC POINTS ######



def p_np_get_var_type(p):
    '''
    np_get_var_type : empty
    '''
    global current_var_type
    current_var_type = p[-1]

def p_np_set_var_type_arr(p):
    '''
    np_set_var_type_arr : empty
    '''
    global current_var_type
    current_var_type += '['+ str(p[-2])+']'

def p_np_set_var_type_matrix(p):
    '''
    np_set_var_type_matrix : empty
    '''
    global current_var_type

    current_var_type += '['+ str(p[-5])+']'+'['+ str(p[-2])+']'

def p_np_get_var_name(p):
    '''
    np_get_var_name : empty
    '''
    global current_var_name
    current_var_name = p[-1]

def p_np_set_var_scope_global(p):
    '''
    np_set_var_scope_global : empty
    '''
    global current_var_scope
    current_var_scope = 'global'

def p_np_set_var_scope_class(p):
    '''
    np_set_var_scope_class : empty
    '''
    global current_var_scope
    current_var_scope = 'class'

def p_np_set_var_scope_function(p):
    '''
    np_set_var_scope_function : empty
    '''
    global current_var_scope
    current_var_scope = 'function'

def p_np_save_var(p):
    '''
    np_save_var : empty
    '''
    global current_var_type
    varsTable.add(current_var_name, current_var_type, current_var_scope)
    current_var_type = current_var_type.translate(str.maketrans('','',' 1234567890[]'))


parser = yacc()
f = open('test_case4.c', 'r')
content = f.read()
case_correct_01 = parser.parse(content)
# print(case_correct_01)

# print("type", current_var_type)
# print("name", current_var_name)
# print("scope", current_var_scope)

# var1, err  = varsTable.search('hello')
# if err:
#     print(err.type)
# else:
#     print(var1.type, var1.scope)

print(varsTable.toString())

param1=Parameter('int','eggs')
#test_func= Function()
functionsTable.add("create","int",[param1],varsTable)
functionsTable.add("doingg","void",[{'lets':'int'},{'dog','float'}],varsTable)

func1,testbool=functionsTable.search("create")
if testbool:
    print(testbool.type)
else:
    print(func1.type,func1.parameters,varsTable.table)
# type, err = semanticCube.semantic('int', 'int', '+')
# if err:
#     print(err.type)
# else:
#     print(type)
