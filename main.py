
from ClassesTable import ClassesTable
from Program import Program
from ply.yacc import yacc
from VarsTable import VarsTable
from SemanticCube import SemanticCube
from Function import Function
from FunctionsTable import FunctionsTable
from QuadruplesList import QuadruplesList
from Parameter import Parameter
from Lexer import *
semanticCube = SemanticCube()
classesTable = ClassesTable()
varsTablesPile = []
functionsTablesPile = []
quadrupleList = QuadruplesList()


def p_main(p):
    '''
    main :  CLASS MAIN LEFTCURLYBRACE CLASSES LEFTCURLYBRACE class_dec RIGHTCURLYBRACE VARS np_create_varsTable np_set_var_scope_global LEFTCURLYBRACE  var_dec  RIGHTCURLYBRACE np_destroy_varsTable  FUNCTIONS np_create_functionsTable LEFTCURLYBRACE func_dec RIGHTCURLYBRACE np_destroy_functionsTable block RIGHTCURLYBRACE np_create_program
    '''
    p[0] = ('rule main: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17])

def p_class_dec(p):
    '''
    class_dec : CLASS ID np_get_class_name LEFTCURLYBRACE VARS np_create_varsTable np_set_var_scope_class  LEFTCURLYBRACE var_dec RIGHTCURLYBRACE np_destroy_varsTable FUNCTIONS np_create_functionsTable LEFTCURLYBRACE func_dec RIGHTCURLYBRACE np_destroy_functionsTable RIGHTCURLYBRACE np_save_class class_dec2
    '''
    p[0] = ('rule class_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13])

def p_class_dec2(p):
    '''
    class_dec2 : class_dec
               | empty
    '''
    p[0] = ('rule class_dec2: ', p[1])

#duda
def p_param(p):
    '''
    param : s_type ID np_get_func_parameter np_add_parameter_to_list param2
    '''
    p[0] = ('rule param: ', p[1], p[2], p[3])

#dudaa
def p_param2(p):
    '''
    param2 : COMMA np_add_parameter_to_list param
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule param2: ', p[1], p[2])
    else:
        p[0] = ('rule param2: ', p[1])

def p_func_dec(p):
    '''
    func_dec : FUNC func_dec2  ID np_get_func_name LEFTPARENTHESIS param RIGHTPARENTHESIS LEFTCURLYBRACE VARS np_create_varsTable np_set_var_scope_function LEFTCURLYBRACE var_dec RIGHTCURLYBRACE np_destroy_varsTable block RETURN h_exp RIGHTCURLYBRACE np_save_function func_dec3
    '''
    p[0] = ('rule func_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15],p[16])

def p_func_dec2(p):
    '''
    func_dec2 : s_type np_get_func_type
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
           | variable np_push_id_type
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
    t2 : MULTIPLICATION np_push_operand_times_divide t
       | DIVISION np_push_operand_times_divide t
       | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule term2: ', p[1], p[2])
    else:
        p[0] = ('rule term2: ', p[1])

def p_exp(p):
    '''
    exp : t np_solve_plus_minus_operand exp2
    '''
    p[0] = ('rule exp: ', p[1], p[2])

def p_exp2(p):
    '''
    exp2 : PLUS np_push_operand_plus_minus exp
         | MINUS np_push_operand_plus_minus exp
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

def p_np_create_program(p):
    '''
    np_create_program : empty
    '''
    global program
    program = Program(classesTable, varsTablesPile.pop(-1), functionsTablesPile.pop(-1))


def p_np_get_class_name(p):
    '''
    np_get_class_name : empty
    '''
    global current_class_name
    current_class_name = p[-1]

def p_np_save_class(p):
    '''
    np_save_class : empty
    '''
    classesTable.add(current_class_name, functionsTablesPile.pop(-1), varsTablesPile.pop(-1))

def p_np_create_functionsTable(p):
    '''
    np_create_functionsTable : empty
    '''
    global current_functionsTable
    current_functionsTable = FunctionsTable()

def p_np_destroy_functionsTable(p):
    '''
    np_destroy_functionsTable : empty
    '''
    functionsTablesPile.append(current_functionsTable)
    del globals()['current_functionsTable']

def p_np_create_varsTable(p):
    '''
    np_create_varsTable : empty
    '''
    global current_varsTable
    current_varsTable = VarsTable()

def p_np_destroy_varsTable(p):
    '''
    np_destroy_varsTable : empty
    '''
    varsTablesPile.append(current_varsTable)
    del globals()['current_varsTable']

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
    current_varsTable.add(current_var_name, current_var_type, current_var_scope)
    current_var_type = current_var_type.translate(str.maketrans('','',' 1234567890[]'))

def p_np_get_func_name(p):
    '''
    np_get_func_name : empty
    '''

    global current_func_name
    current_func_name = str(p[-1])

def p_np_get_func_type(p):
    '''
    np_get_func_type : empty
    '''

    global current_func_type
    current_func_type = str(p[-1][1])

def p_np_get_func_parameter(p):
    '''
    np_get_func_parameter : empty
    '''

    global current_parameter
    current_parameter=Parameter(str(p[-2][1]),str(p[-1]))

def p_np_add_parameter_to_list(p):
    '''
    np_add_parameter_to_list : empty
    '''

    global current_parameters_list
    current_parameters_list = []
    current_parameters_list.append(current_parameter)

#tabla de variables limpiar?


def p_np_save_function(p):
    '''
    np_save_function : empty
    '''
    global current_functionsTable
    current_functionsTable.add(current_func_name,current_func_type,current_parameters_list,varsTablesPile.pop(-1))


##########Quadruples##########

#first rules from fact,term,exp
def p_np_push_id_type(p):
    '''
    np_push_id_type : empty
    '''
    global idPush
    idPush = p[-1]
    quadrupleList.operatorsStack.append(idPush)

def p_np_push_operand_times_divide(p):
    '''
    np_push_operand_times_divide : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operandsStack.append(operPush)

def p_np_push_operand_plus_minus(p):
    '''
    np_push_operand_plus_minus : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operandsStack.append(operPush)

def p_np_solve_plus_minus_operand(p):
    '''
    np_solve_plus_minus_operand : empty
    '''
    #quadrupleList.checkOperandPlusMinus()
###########################################################################################3
parser = yacc()
f = open('test_case5.c', 'r')
content = f.read()
case_correct_01 = parser.parse(content)

for quad in quadrupleList.operatorsStack:
    print(quad)


#program.toString()

# functionsTable = FunctionsTable()
# functionsTable.add("test", "int", [Parameter("int", "param"), Parameter("float", "param2")], varsTable)

# varsTable2 = VarsTable()
# varsTable2.add("ClassVar", "int", "class")

# classTable = ClassesTable()
# classTable.add("ClassTest", functionsTable, varsTable2)

# classTable.toString()
