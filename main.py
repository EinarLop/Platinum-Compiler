
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
from Error import Error
semanticCube = SemanticCube()
classesTable = ClassesTable()
varsTablesPile = []
functionsTablesPile = []
quadrupleList = QuadruplesList()

#duda con memoria
#la memoria con las direcciones virtuales entonces tendriamos que restarle el numero base por asi decirlo cuando queramos accedar a ella?
#cuando hacemos como el push o append de cada cosa en las "direcciones virtuales" o en los arreglos o como esta eso?


#duda
#tenemos entonces 2 tablas de funciones? una como de globales y una que se va creando en cada clase con sus respectivas funciones?
def p_main(p):
    '''
    main :  CLASS MAIN LEFTCURLYBRACE GLOBAL VARS np_create_varsTable np_set_var_scope_global LEFTCURLYBRACE  var_dec  RIGHTCURLYBRACE np_destroy_varsTable  CLASSES LEFTCURLYBRACE class_dec RIGHTCURLYBRACE FUNCTIONS np_create_functionsTable LEFTCURLYBRACE func_dec RIGHTCURLYBRACE np_destroy_functionsTable block RIGHTCURLYBRACE np_create_program
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


def p_param(p):
    '''
    param : s_type ID np_get_func_parameter np_add_parameter_to_list param2
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
    func_dec : FUNC func_dec2  ID np_get_func_name LEFTPARENTHESIS np_create_param_list param RIGHTPARENTHESIS LEFTCURLYBRACE VARS np_create_varsTable np_set_var_scope_function LEFTCURLYBRACE var_dec RIGHTCURLYBRACE np_destroy_varsTable  block RETURN h_exp RIGHTCURLYBRACE  np_save_function np_generate_endfunc_quad func_dec3
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
#call? añadir call como cuadruplo?
def p_factor(p):
    '''
    factor : LEFTPARENTHESIS np_create_fake_void h_exp RIGHTPARENTHESIS np_eliminate_fake_void
           | CTEI np_push_ctei
           | CTEF np_push_ctef
           | variable np_push_id_type
           | call
    '''
    if (len(p) == 4):
        p[0] = ('rule factor: ', p[1], p[2], p[3])
    elif(len(p) == 2):
        p[0] = ('rule factor: ', p[1])

def p_t(p):
    '''
    t : factor np_solve_times_divide_operator t2
    '''
    p[0] = ('rule term: ', p[1], p[2])

def p_t2(p):
    '''
    t2 : MULTIPLICATION np_push_operator_times_divide t
       | DIVISION np_push_operator_times_divide t
       | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule term2: ', p[1], p[2])
    else:
        p[0] = ('rule term2: ', p[1])

def p_exp(p):
    '''
    exp : t np_solve_plus_minus_operator exp2
    '''
    p[0] = ('rule exp: ', p[1], p[2])

def p_exp2(p):
    '''
    exp2 : PLUS np_push_operator_plus_minus exp
         | MINUS np_push_operator_plus_minus exp
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
    s_exp2 : LT np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
           | GT np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
           | LTOE np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
           | GTOE np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
           | NE np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
           | EQUALITY np_push_operator_sexp np_define_LOperand_sexp exp np_define_ROperand_sexp
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
    h_exp2 : AND np_push_operator_hexp np_define_LOperand_hexp s_exp np_define_ROperand_hexp h_exp2
           | OR np_push_operator_hexp np_define_LOperand_hexp s_exp np_define_ROperand_hexp h_exp2
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
    call : ID np_verify_ID_call_module LEFTPARENTHESIS np_generate_ERA_quad_func_call call2 RIGHTPARENTHESIS np_generate_goSub_function_call
    '''
    p[0] = ('rule call: ', p[1], p[2], p[3],p[4])

####duda
###deberiamos cambiar h_exp a exp?
def p_call2(p):
    '''
    call2 : exp np_append_param_function_call_parameters  call3
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call2:', p[1], p[2])
    else:
        p[0] = ('rule call2:', p[1])

def p_call3(p):
    '''
    call3 : COMMA exp np_append_param_function_call_parameters call3
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
	       | CHAR  np_get_var_type
    '''
    p[0] = ('rule s_type: ', p[1])

def p_assignment(p):
    '''
    assignment : variable np_push_id_type  EQUAL np_push_assignation_operator assignment2
    '''
    p[0] = ('rule assignment: ', p[1],p[2])
#cambio de gramatica p_assignment2
def p_assignment2(p):
    '''
    assignment2 : exp np_result_assignation
                | NEW ID

    '''
    if(len(p) == 2):
        p[0] = ('rule assignment2 : ', p[1])
    else:
        p[0] = ('rule assignment2 : ', p[1],p[2])

def p_read(p):
    '''
    read : READ LEFTPARENTHESIS variable np_generate_read_quadruple RIGHTPARENTHESIS

    '''
    p[0] = ('rule read : ', p[1],p[2])

def p_write(p):
    '''
    write : WRITE LEFTPARENTHESIS write2 RIGHTPARENTHESIS

    '''
    p[0] = ('rule write :',p[1],p[2],p[3],p[4])

def p_write2(p):
    '''
    write2 : h_exp np_generate_write_quadruple write3
           | SIGNBOARD np_push_signboard np_generate_write_quadruple write3

    '''
    p[0] = ('rule write2 :',p[1],p[2])

def p_write3(p):
    '''
    write3 : COMMA h_exp write3 np_generate_write_quadruple
           | COMMA SIGNBOARD np_push_signboard write3 np_generate_write_quadruple
           | empty

    '''
    if(len(p) == 3):
        p[0] = ('rule write3 :',p[1],p[2])
    else:
        p[0] = ('rule write3 :',p[1])

def p_condition(p):
    '''
    condition : IF LEFTPARENTHESIS h_exp RIGHTPARENTHESIS np_generate_gotoF_condition block condition2 SEMICOLON np_fill_gotoF_condition_if
    '''
    p[0] = ('rule condition: ', p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_condition2(p):
    '''
    condition2 : ELSE np_generate_goto_condition block
               | empty

    '''
    if(len(p) == 3):
        p[0] = ('rule condition2 : ', p[1],p[2])
    else:
        p[0] = ('rule condition2 : ', p[1])

def p_loop_w(p):
    '''
    loop_w : WHILE LEFTPARENTHESIS np_while_push_jumpStack h_exp np_while_generate_gotoF RIGHTPARENTHESIS DO block np_while_generate_goto SEMICOLON

    '''
    p[0] = ('rule loopW : ', p[1],p[2],p[3],p[4],p[5],p[6],p[7])

#cambios de momento
def p_loop_f(p):
    '''
    loop_f : FOR LEFTPARENTHESIS ID np_for_push_id EQUAL exp np_for_FIRSTexp TO exp np_for_SECONDexp  RIGHTPARENTHESIS DO block SEMICOLON np_for_changesVC

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
    # del globals()['current_functionsTable']

def p_np_create_varsTable(p):
    '''
    np_create_varsTable : empty
    '''
    global current_varsTable
    current_varsTable = VarsTable()
#duda
#esto como tal no se destruye o si? o como funciona esta parte
def p_np_destroy_varsTable(p):
    '''
    np_destroy_varsTable : empty
    '''
    varsTablesPile.append(current_varsTable)
    # del globals()['current_varsTable']

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
    #current_var_type = current_var_type.translate(str.maketrans('','',' 1234567890[]'))

def p_np_get_func_name(p):
    '''
    np_get_func_name : empty
    '''

    global current_func_name
    global initialQuadruple
    initialQuadruple = quadrupleList.cont
    current_func_name = str(p[-1])

def p_np_get_func_type(p):
    '''
    np_get_func_type : empty
    '''

    global current_func_type
    current_func_type = str(p[-1][1])

def p_np_create_param_list(p):
    '''
    np_create_param_list : empty
    '''
    global current_parameters_list
    current_parameters_list = []


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

    current_parameters_list.append(current_parameter)

def p_np_save_function(p):
    '''
    np_save_function : empty
    '''
    global current_functionsTable
    current_functionsTable.add(current_func_name,current_func_type,current_parameters_list,varsTablesPile.pop(-1),initialQuadruple)


##########Quadruples##########

#first rules from fact,term,exp
def p_np_push_id_type(p):
    '''
    np_push_id_type : empty
    '''
    global idPush
    test = False
    idPush = p[-1][1]
    quadrupleList.operandsStack.append(idPush)

    '''
    for vt in reversed(varsTablesPile):
        if idPush in vt.table:
            test= True
            break

    if test:
        #print(idPush, vt.table[idPush].type)
        quadrupleList.operandsStack.append(idPush)
        quadrupleList.typesStack.append(vt.table[idPush].type)
    else:
        error= Error.notDeclaredError(idPush)
    '''

def p_np_push_ctei(p):
    '''
    np_push_ctei : empty
    '''

    global cteiPush
    cteiPush = p[-1]
    quadrupleList.operandsStack.append(cteiPush)

def p_np_push_ctef(p):
    '''
    np_push_ctef : empty
    '''

    global ctefPush
    ctefPush = p[-1]
    quadrupleList.operandsStack.append(ctefPush)

def p_np_push_operator_times_divide(p):
    '''
    np_push_operator_times_divide : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)

def p_np_push_operator_plus_minus(p):
    '''
    np_push_operator_plus_minus : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)

def p_np_solve_plus_minus_operator(p):
    '''
    np_solve_plus_minus_operator : empty
    '''
    quadrupleList.checkOperatorPlusMinus()

def p_np_solve_times_divide_operator(p):
    '''
    np_solve_times_divide_operator : empty
    '''

    quadrupleList.checkOperatorTimesDivide()

def p_np_push_assignation_operator(p):
    '''
    np_push_assignation_operator : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)

def p_np_result_assignation(p):
    '''
    np_result_assignation : empty
    '''

    quadrupleList.makeAssignationResult()

def p_np_create_fake_void(p):
    '''
    np_create_fake_void : empty
    '''

    global fakeVoid
    fakeVoid= p[-1]
    quadrupleList.operatorsStack.append(fakeVoid)

def p_np_eliminate_fake_void(p):
    '''
    np_eliminate_fake_void : empty
    '''
    quadrupleList.eliminateFakeVoid()

def p_np_push_operator_sexp(p):
    '''
    np_push_operator_sexp : empty
    '''
    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)


def p_np_push_operator_hexp(p):
    '''
    np_push_operator_hexp : empty
    '''
    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)

def p_np_define_LOperand_sexp(p):
    '''
    np_define_LOperand_sexp : empty
    '''
    global LOperandSexp
    LOperandSexp = quadrupleList.operandsStack.pop()
def p_np_define_ROperand_sexp(p):
    '''
    np_define_ROperand_sexp : empty
    '''
    quadrupleList.generate_sExp_quad(LOperandSexp)

def p_np_define_LOperand_hexp(p):
    '''
    np_define_LOperand_hexp : empty
    '''
    global LOperandHexp
    LOperandHexp = quadrupleList.operandsStack.pop()
def p_np_define_ROperand_hexp(p):
    '''
    np_define_ROperand_hexp : empty
    '''
    quadrupleList.generate_hExp_quad(LOperandHexp)

def p_np_generate_gotoF_condition(p):
    '''
    np_generate_gotoF_condition : empty
    '''

    quadrupleList.generateGoToFCondition()

#fill de condicion if sola
def p_np_fill_gotoF_condition_if(p):
    '''
    np_fill_gotoF_condition_if : empty
    '''
    quadrupleList.fillgotoF_IF()

#else
def p_np_generate_goto_condition(p):
    '''
    np_generate_goto_condition : empty
    '''

    quadrupleList.generateGoToCondition()

######nuevos####


def p_np_push_signboard(p):
    '''
    np_push_signboard : empty
    '''
    global oper
    oper=p[-1]
    quadrupleList.operandsStack.append(oper)


def p_np_generate_write_quadruple(p):
    '''
    np_generate_write_quadruple : empty
    '''

    quadrupleList.addQuadrupleReadWrite("WRITE",quadrupleList.operandsStack.pop(),'','')

def p_np_generate_read_quadruple(p):
    '''
    np_generate_read_quadruple : empty
    '''

    global operand
    operand=p[-1][1]
    quadrupleList.addQuadrupleReadWrite("READ",operand,'','')

def p_np_while_push_jumpStack(p):
    '''
    np_while_push_jumpStack : empty
    '''
    quadrupleList.jumpsStack.append(quadrupleList.cont)

def p_np_while_generate_gotoF(p):
    #faltaria aqui los tipos lo estoy haciendo sin tipos de momento
    '''
    np_while_generate_gotoF : empty
    '''

    quadrupleList.generateGoToFWhile()

def p_np_while_generate_goto(p):
    '''
    np_while_generate_goto : empty
    '''
    quadrupleList.generateGoToWhile()

################################for################################
def p_np_for_push_id(p):
    '''
    np_for_push_id : empty
    '''
    #pushear id y tipo pero aun no tiene tipos
    global pushIDFor
    pushIDFor= p[-1]
    #si el tipo del id no es un numero entonces typemismatch
    #if
    #else
    quadrupleList.operandsStack.append(pushIDFor)

def p_np_for_FIRSTexp(p):
    '''
    np_for_FIRSTexp : empty
    '''
    quadrupleList.generateVControlQuadruple(pushIDFor)

def p_np_for_SECONDexp(p):
    '''
    np_for_SECONDexp : empty
    '''
    quadrupleList.generateVFinalQuadruple()

def p_np_for_changesVC(p):
    '''
    np_for_changesVC : empty
    '''

    quadrupleList.forChangeVC()

################################for################################

def p_np_generate_endfunc_quad(p):
    '''
    np_generate_endfunc_quad : empty
    '''
    quadrupleList.generateEndFuncModule()



#######functions#######
def p_np_verify_ID_call_module(p):
    '''
    np_verify_ID_call_module : empty
    '''
    global idVerify
    idVerify =p[-1]
    #anotaciones
    #significa que el id si existe en la tabla de funciones actual paso 1 check
    current_functionsTable.search(idVerify)

def p_np_generate_ERA_quad_func_call(p):
    '''
    np_generate_ERA_quad_func_call : empty
    '''
    #anotaciones
    #se necesitan contar los tipos locales: int float y char y temporales: int float y char para despues usar el era bien en la maquina virtual
    #genero quad ERA pero aun no hacemos nada exactamente con el creo que eso ya viene en la maquina virtual no?
    global paramCounter
    paramCounter = 0

    '''
    for param in current_functionsTable.table[idVerify].parameters:
        print("param:",param.id)
    '''
    #duda ##arreglado
    #hay algo mal con los parametros, solo se puede poner uno o solo aparece uno


    #checar tipos de parametros y si coincide el numero de parametros hacer el gosub
    quadrupleList.generateERAFuncCall(idVerify)

def p_np_append_param_function_call_parameters(p):
    '''
    np_append_param_function_call_parameters : empty
    '''

    #param= quadrupleList.operandsStack.pop()
    #anotaciones
    #faltaria hacer pop en pila de tipos para comparar

    #paramCounter +=1
    #if pop de pila de tipos == en current_functionsTable.table[idVerify].parameters[paramCounter-1]

def p_np_generate_goSub_function_call(p):
    '''
    np_generate_goSub_function_call : empty
    '''
    #print(paramCounter)
    quadrupleList.generateGoSubFuncCall(idVerify,current_functionsTable.table[idVerify].quadrupleStart)
###########################################################################################
parser = yacc()
f = open('test_case7.c', 'r')
content = f.read()
case_correct_01 = parser.parse(content)



#program.toString()

#print("###############QuadrupleTests###############")
#quadrupleList.operatorsStackToString()
#quadrupleList.operandsStackToString()
quadrupleList.quadrupleListToString()
# quadrupleList.typeStackToString()
# quadrupleList.jumpsStackToString()




#classesTable.toString()
