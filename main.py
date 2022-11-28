#Clase main en la cual se tiene toda la parte de gramatica y fase de compilacion

#importacion de todas las clases necesarias para
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
from VirtualMemory import VirtualMemory

#inicializacion de dichos objetos para su uso
#creacion de pila de tablas de variables y funciones
semanticCube = SemanticCube()
classesTable = ClassesTable()
varsTablesPile = []
functionsTablesPile = []
quadrupleList = QuadruplesList()

#rangos de memoria global ademas de constantes
GI = [1000, 1999]
GF = [2000, 2999]
GC = [3000, 3999]
GB = [4000, 4999]

CI = [18000, 18999]
CF = [19000, 19999]
CC = [20000, 20999]
CB = [21000, 21999]


#contadores para saber cuanta memoria usa cada funcion y clase
global ci_counter
ci_counter = 0

cf_counter = 0
cc_counter = 0
cb_counter = 0

#creacion de tabla de constantes vacia
constantsTable = {}

LI = [10000, 10999]
LF = [11000, 11999]
LC = [12000, 12999]
LB = [13000, 13999]


#gramaticas con sus puntos neuralgicos
def p_main(p):
    '''
    main : CLASS MAIN np_generate_goto_main LEFTCURLYBRACE np_start_global_memory_counter GLOBAL VARS np_create_varsTable np_set_var_scope_global LEFTCURLYBRACE  var_dec  RIGHTCURLYBRACE np_destroy_varsTable np_stop_global_memory_counter  CLASSES LEFTCURLYBRACE class_dec RIGHTCURLYBRACE FUNCTIONS np_create_functionsTable  LEFTCURLYBRACE func_dec RIGHTCURLYBRACE np_destroy_functionsTable np_fill_goto_main_quad np_reset_temp_counter np_set_temp_global_flag block RIGHTCURLYBRACE np_create_program
    '''

    p[0] = ('rule main: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17])

def p_class_dec(p):
    '''
    class_dec : CLASS ID np_get_class_name np_check_class_exists LEFTCURLYBRACE VARS np_create_varsTable np_set_var_scope_class  LEFTCURLYBRACE var_dec RIGHTCURLYBRACE np_destroy_varsTable FUNCTIONS np_create_functionsTable LEFTCURLYBRACE func_dec RIGHTCURLYBRACE np_destroy_functionsTable RIGHTCURLYBRACE np_save_class class_dec2
              | empty
    '''
    # p[0] = ('rule class_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13])

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
    func_dec : FUNC np_reset_temp_counter func_dec2 ID np_get_func_name np_start_local_memory_counter np_push_func_id_globals LEFTPARENTHESIS np_create_varsTable param RIGHTPARENTHESIS LEFTCURLYBRACE  VARS  np_set_var_scope_function LEFTCURLYBRACE var_dec RIGHTCURLYBRACE np_destroy_varsTable np_init_func_tempTable np_save_function block RETURN h_exp  RIGHTCURLYBRACE np_generate_return_func np_pop_varsTable np_generate_endfunc_quad func_dec3
             | empty
    '''
    # p[0] = ('rule func_dec: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15],p[16])

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
    var_dec5 : LEFTBRACKET CTEI RIGHTBRACKET np_set_DIM_array var_dec9
	         | LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET np_set_DIM_matrix var_dec9
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
    factor : LEFTPARENTHESIS np_create_fake_void h_exp RIGHTPARENTHESIS np_eliminate_fake_void
           | CTEI np_saveConstantI np_push_ctei
           | CTEF np_saveConstantF np_push_ctef
           | variable
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
    variable : ID np_push_id_type variable2
    '''
    p[0] = ('rule variable: ', p[1], p[2])

def p_variable2(p):
    '''
    variable2 : LEFTBRACKET exp np_create_dimensional_quads RIGHTBRACKET  variable3 np_sum_baseA_array
              | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule variable2: ', p[1], p[2], p[3],p[4])
    elif(len(p) == 2):
        p[0] = ('rule variable2: ', p[1])

def p_variable3(p):
    '''
    variable3 : LEFTBRACKET np_DIM_plus exp np_create_dimensional_quads RIGHTBRACKET
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
    call : ID np_check_func_exists LEFTPARENTHESIS np_generate_ERA_quad_func_call call2 RIGHTPARENTHESIS np_check_func_params np_generate_goSub_function_call np_assign_global_to_temporal_func_call
    '''
    p[0] = ('rule call: ', p[1], p[2], p[3],p[4])



def p_call2(p):
    '''
    call2 : exp np_generate_quad_parameter np_check_func_params_counter call3
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call2:', p[1], p[2])
    else:
        p[0] = ('rule call2:', p[1])

def p_call3(p):
    '''
    call3 : COMMA exp np_generate_quad_parameter np_check_func_params_counter call3
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
	       | CHAR np_get_var_type
           | BOOL np_get_var_type
    '''
    p[0] = ('rule s_type: ', p[1])

def p_assignment(p):
    '''
    assignment : variable EQUAL np_push_assignation_operator assignment2
    '''
    p[0] = ('rule assignment: ', p[1],p[2])

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
    read : READ LEFTPARENTHESIS ID np_generate_read_quadruple RIGHTPARENTHESIS

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
    exit()


##### NEURALGIC POINTS ######

#funcion para añadir constantes a la tabla de constantes
def addConstantsTable(constantAdd):
    global ci_counter
    if constantAdd not in constantsTable:
        constantsTable[constantAdd] = CI[0] + ci_counter
        ci_counter += 1
    else:
        pass
#generar cuadruplo para ir a main, se genera vacio
def p_np_generate_goto_main(p):
    '''
    np_generate_goto_main : empty
    '''
    quadrupleList.generateGoToMainQuad()

#crear programa haciendo pop de la pila de las tablas
def p_np_create_program(p):
    '''
        np_create_program : empty
    '''
    global program
    program = Program(classesTable, varsTablesPile.pop(-1), functionsTablesPile.pop(-1))

#obtener el nombre de la clase
def p_np_get_class_name(p):
    '''
    np_get_class_name : empty
    '''
    global current_class_name
    current_class_name = p[-1]
#guardar clase en tabla de clases
def p_np_save_class(p):
    '''
    np_save_class : empty
    '''
    classesTable.add(current_class_name, functionsTablesPile.pop(-1), varsTablesPile.pop(-1))


#creación de la tabla de funciones
def p_np_create_functionsTable(p):
    '''
    np_create_functionsTable : empty
    '''
    global current_functionsTable
    current_functionsTable = FunctionsTable()

#se saca la actual tabla de funciones y se mete en la pila de tablas de funciones
def p_np_destroy_functionsTable(p):
    '''
    np_destroy_functionsTable : empty
    '''

    functionsTablesPile.append(current_functionsTable)


#se crea una nueva tabla de variables
def p_np_create_varsTable(p):
    '''
    np_create_varsTable : empty
    '''
    global current_varsTable
    current_varsTable = VarsTable()

#se mete la actual tabla de variables en la pila de tablas de variables
def p_np_destroy_varsTable(p):
    '''
    np_destroy_varsTable : empty
    '''
    global current_varsTable

    varsTablesPile.append(current_varsTable)
    current_varsTable=VarsTable()

#obtener el tipo de variable
def p_np_get_var_type(p):
    '''
    np_get_var_type : empty
    '''
    global current_var_type
    current_var_type = p[-1]

#si es arreglo llega aqui y marca que al menos es un arrego con un bool
def p_np_set_DIM_array(p):
    '''
    np_set_DIM_array : empty
    '''
    global isArray
    isArray=True

    global current_dimension_size
    current_dimension_size = p[-2]

# si llega a ser una matriz se marca con un booleano y se sacan ambas dimensiones de los indices ctei
def p_np_set_DIM_matrix(p):
    '''
    np_set_DIM_matrix : empty
    '''
    global isMatrix
    global sizesMatrix
    sizesMatrix=[]
    isMatrix = True
    #size1 size2 sizetotal d2
    global current_dimension_size
    current_dimension_size = p[-5] * p[-2]
    sizesMatrix=[p[-5],p[-2]]

#obtener el nombre de variable
def p_np_get_var_name(p):
    '''
    np_get_var_name : empty
    '''
    global isArray
    isArray = False

    global isMatrix
    isMatrix = False


    global current_var_name
    current_var_name = p[-1]
# si esta en variables globales el scope se vuelve global
def p_np_set_var_scope_global(p):
    '''
    np_set_var_scope_global : empty
    '''
    global current_var_scope
    current_var_scope = 'global'

#el scope se vuelve de tipo clase si esta en una clase la variable
def p_np_set_var_scope_class(p):
    '''
    np_set_var_scope_class : empty
    '''
    global current_var_scope
    current_var_scope = 'class'

#el scope se vuelve de tipo funcion si esta dentro de una funcion
def p_np_set_var_scope_function(p):
    '''
    np_set_var_scope_function : empty
    '''
    global current_var_scope
    current_var_scope = 'function'

# se guarda la variable en la tabla de variables actual
def p_np_save_var(p):
    '''
    np_save_var : empty
    '''
    global DIM
    global varAddDimensionalArray
    global sizesMatrix
    DIM=[]

    #checar si es un arreglo o una matriz para darle valores a DIM para la tabla de variables
    if not isArray and not isMatrix:
        DIM = None
        varAddDimensional=0
    else:
        if isArray: #si es un arreglo darle valor a su campo DIM
            DIM.append(current_dimension_size)
            varAddDimensional= current_dimension_size-1
        if isMatrix: #si es una matriz darle valor a su campo DIM
            for i in sizesMatrix:
                DIM.append(i)
            varAddDimensional= (DIM[0]*DIM[1])-1

    if global_memory_counter_flag: #si es global con esta bandera se verifica

        #variables para los contadores de memoria global
        global current_var_type
        global global_memory_counter_int
        global global_memory_counter_float
        global global_memory_counter_char
        global global_memory_counter_bool
        global global_memory_counter_array
        global global_memory_counter_matrix

        #dependiendo del tipo de variable se le suma la dirección base y se aumenta el contador global de ese tipo de variable
        if current_var_type  == "int":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, GI[0] + global_memory_counter_int,DIM)
            global_memory_counter_int += 1 + varAddDimensional
        elif current_var_type  == "float":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, GF[0] + global_memory_counter_float,DIM)
            global_memory_counter_float += 1 + varAddDimensional
        elif current_var_type  == "char":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, GC[0] + global_memory_counter_char,DIM)
            global_memory_counter_char += 1 + varAddDimensional
        elif current_var_type  == "bool":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, GB[0] + global_memory_counter_bool,DIM)
            global_memory_counter_bool += 1 + varAddDimensional

    else: #de lo contrario se hace lo mismo pero con contadores y direcciones base locales
        #variables para los contadores de memoria local
        global local_memory_counter_int
        global local_memory_counter_float
        global local_memory_counter_char
        global local_memory_counter_bool

        #dependiendo del tipo de variable se le suma la dirección base y se aumenta el contador local de ese tipo de variable
        if current_var_type  == "int":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, LI[0] + local_memory_counter_int,DIM)
            local_memory_counter_int += 1
        elif current_var_type  == "float":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, LF[0] + local_memory_counter_float,DIM)
            local_memory_counter_float += 1
        elif current_var_type  == "char":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, LC[0] + local_memory_counter_char,DIM)
            local_memory_counter_char += 1
        elif current_var_type  == "bool":
            current_varsTable.add(current_var_name, current_var_type, current_var_scope, LB[0] + local_memory_counter_bool,DIM)
            local_memory_counter_bool += 1

    current_var_type = current_var_type.translate(str.maketrans('','',' 1234567890[]'))

#obtener el nombre de la funcion
def p_np_get_func_name(p):
    '''
    np_get_func_name : empty
    '''

    global current_func_name
    global initialQuadruple
    initialQuadruple = quadrupleList.cont
    current_func_name = str(p[-1])

#obtener el tipo de la funcion
def p_np_get_func_type(p):
    '''
    np_get_func_type : empty
    '''

    global current_func_type
    current_func_type = str(p[-1][1])

#el id de la funcion se pushea a la tabla de variables globales ya que todas tienen return asi que se mete en la tabla de variables global con su tipo
def p_np_push_func_id_globals(p):
    '''
    np_push_func_id_globals : empty
    '''

    global current_var_type
    global global_memory_counter_int
    global global_memory_counter_float
    global global_memory_counter_char
    global global_memory_counter_bool
    global global_memory_counter_array
    global global_memory_counter_matrix

    if current_var_type  == "int":
        varsTablesPile[0].add(current_func_name, current_func_type,  "globalFunction", GI[0] + global_memory_counter_int,None)
        global_memory_counter_int += 1
    elif current_var_type  == "float":
        varsTablesPile[0].add(current_func_name, current_func_type,  "globalFunction", GF[0] + global_memory_counter_float,None)
        global_memory_counter_float += 1
    elif current_var_type  == "char":
        varsTablesPile[0].add(current_func_name, current_func_type,  "globalFunction", GC[0] + global_memory_counter_char,None)
        global_memory_counter_char += 1
    elif current_var_type  == "bool":
        varsTablesPile[0].add(current_func_name, current_func_type,  "globalFunction", GB[0] + global_memory_counter_bool,None)
        global_memory_counter_bool += 1


#se obtienen los campos de los parametros de una funcion para convertrlo enun objeto parameter
def p_np_get_func_parameter(p):
    '''
    np_get_func_parameter : empty
    '''

    global current_parameter

    current_parameter=Parameter(str(p[-2][1]),str(p[-1]))

#añadir parametros a la tabla de variables para poder usarlos
def p_np_add_parameter_to_list(p):
    '''
    np_add_parameter_to_list : empty
    '''

    global current_parameters_list
    global local_memory_counter_int
    global local_memory_counter_float
    global local_memory_counter_char
    global local_memory_counter_bool


    temp = "current_parameters_list" in globals()
    if (temp):
        current_parameters_list.append(current_parameter)
        if current_parameter.type  == "int":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LI[0] + local_memory_counter_int,None)
            local_memory_counter_int += 1
        elif current_parameter.type  == "float":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LF[0] + local_memory_counter_float,None)
            local_memory_counter_float += 1
        elif current_parameter.type  == "char":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LC[0] + local_memory_counter_char,None)
            local_memory_counter_char += 1
        elif current_parameter.type  == "bool":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LB[0] + local_memory_counter_bool,None)
            local_memory_counter_bool += 1
    else:
        current_parameters_list = []
        current_parameters_list.append(current_parameter)
        if current_parameter.type  == "int":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LI[0] + local_memory_counter_int,None)
            local_memory_counter_int += 1
        elif current_parameter.type  == "float":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LF[0] + local_memory_counter_float,None)
            local_memory_counter_float += 1
        elif current_parameter.type  == "char":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LC[0] + local_memory_counter_char,None)
            local_memory_counter_char += 1
        elif current_parameter.type  == "bool":
            current_varsTable.add(current_parameter.id,current_parameter.type, current_var_scope, LB[0] + local_memory_counter_bool,None)
            local_memory_counter_bool += 1

#guardar funcion en tabla de funciones
def p_np_save_function(p):
    '''
    np_save_function : empty
    '''

    current_functionsTable.add(current_func_name,current_func_type, current_parameters_list,varsTablesPile[-1],initialQuadruple, [0,0,0,0])
    del globals()["current_parameters_list"]






##############################Quadruples###############################


#############################aritmetic_exp#############################
#pushear id con la condicion de si existe o no, y si tiene dimensiones se pushea a pila de dimensionadas junto con su tipo
def p_np_push_id_type(p):
    '''
    np_push_id_type : empty
    '''
    global idPush
    test = False
    idPush = p[-1]

    ## Si este esta antes de siguiente da prioridad a variables
    for vt in reversed(varsTablesPile):
        if idPush in vt.table:
            if vt.table[idPush].dim != None:
                global DIMid
                DIMid=1
                quadrupleList.dimensionalOperandsStack.append(idPush)
                quadrupleList.typesStack.append(vt.table[idPush].type)
                quadrupleList.operatorsStack.append('(')
            elif vt.table[idPush].dim == None:
                quadrupleList.operandsStack.append(vt.table[idPush].address)
                quadrupleList.typesStack.append(vt.table[idPush].type)


            return


    print(f"Variable {idPush} not declared")
    exit()

#pushear a pilaOper ctei
def p_np_push_ctei(p):
    '''
    np_push_ctei : empty
    '''

    global cteiPush
    cteiPush = p[-2]

    if cteiPush in constantsTable:
        quadrupleList.operandsStack.append(constantsTable[cteiPush])
    quadrupleList.typesStack.append("int")

#pushear a pilaOper cteF
def p_np_push_ctef(p):
    '''
    np_push_ctef : empty
    '''

    global ctefPush
    ctefPush = p[-2]
    if ctefPush in constantsTable:
        quadrupleList.operandsStack.append(constantsTable[ctefPush])
    quadrupleList.typesStack.append("float")

#pushear operador / a pilaOperadores
def p_np_push_operator_times_divide(p):
    '''
    np_push_operator_times_divide : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)
#pushear operador +´o -a pilaOperadores
def p_np_push_operator_plus_minus(p):
    '''
    np_push_operator_plus_minus : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)
#resolver si hay un + o - en top de pilaOperadores
def p_np_solve_plus_minus_operator(p):
    '''
    np_solve_plus_minus_operator : empty
    '''
    temporalType = quadrupleList.checkOperatorPlusMinus()
    registerTempVariable(temporalType)
#resolver si hay un * o / en top de pilaOperadores
def p_np_solve_times_divide_operator(p):
    '''
    np_solve_times_divide_operator : empty
    '''

    temporalType = quadrupleList.checkOperatorTimesDivide()
    registerTempVariable(temporalType)
#############################aritmetic_exp#############################


#############################assignation fakevoid bool_operators#############################
#se pushea = a pila de operadores
def p_np_push_assignation_operator(p):
    '''
    np_push_assignation_operator : empty
    '''

    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)
#resolver la asignacion, sacar de pilaOperadores con su tipo para hacer comparacion de tipos
def p_np_result_assignation(p):
    '''
    np_result_assignation : empty
    '''

    temporalType = quadrupleList.makeAssignationResult()
    registerTempVariable(temporalType)

#pushear ( a pilaOperadores que es el fondo falso
def p_np_create_fake_void(p):
    '''
    np_create_fake_void : empty
    '''

    global fakeVoid
    fakeVoid= p[-1]
    quadrupleList.operatorsStack.append(fakeVoid)

#eliminar fondo falso con pop
def p_np_eliminate_fake_void(p):
    '''
    np_eliminate_fake_void : empty
    '''
    quadrupleList.eliminateFakeVoid()
#pushear operadores de s_exp
def p_np_push_operator_sexp(p):
    '''
    np_push_operator_sexp : empty
    '''
    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)

#pushear AND o OR a pilaOperadores
def p_np_push_operator_hexp(p):
    '''
    np_push_operator_hexp : empty
    '''
    global operPush
    operPush = p[-1]
    quadrupleList.operatorsStack.append(operPush)
#definir operando izquierdo de s_exp es decir Loperand < ROperand como ejemplo
def p_np_define_LOperand_sexp(p):
    '''
    np_define_LOperand_sexp : empty
    '''
    global LOperandSexp
    LOperandSexp = quadrupleList.operandsStack.pop()

#definir operando derecho de s_exp es decir Loperand < ROperand como ejemplo
def p_np_define_ROperand_sexp(p):
    '''
    np_define_ROperand_sexp : empty
    '''
    temporalType = quadrupleList.generate_sExp_quad(LOperandSexp)
    registerTempVariable(temporalType)

#definir operando izquierdo de h_exp es decir Loperand && ROperand como ejemplo
def p_np_define_LOperand_hexp(p):
    '''
    np_define_LOperand_hexp : empty
    '''
    global LOperandHexp
    LOperandHexp = quadrupleList.operandsStack.pop()

#definir operando derecho de h_exp es decir Loperand && ROperand como ejemplo
def p_np_define_ROperand_hexp(p):
    '''
    np_define_ROperand_hexp : empty
    '''
    temporalType = quadrupleList.generate_hExp_quad(LOperandHexp)
    registerTempVariable(temporalType)
#############################assignation# #fakevoid# #bool_operators#############################


#############################if#############################

#Crear cuadruplo sinn saber aun a donde ir de gotoF para despues de evaluar exp del parentesis de if
def p_np_generate_gotoF_condition(p):
    '''
    np_generate_gotoF_condition : empty
    '''

    quadrupleList.generateGoToFCondition()

#fill de gotoF de condicion if
def p_np_fill_gotoF_condition_if(p):
    '''
    np_fill_gotoF_condition_if : empty
    '''
    quadrupleList.fillgotoF_IF()

#generar goto despues de encontrar un else
def p_np_generate_goto_condition(p):
    '''
    np_generate_goto_condition : empty
    '''

    quadrupleList.generateGoToCondition()
#############################if#############################


#############################write#############################
#pushear letrero a pila de operadores
def p_np_push_signboard(p):
    '''
    np_push_signboard : empty
    '''
    global oper
    oper=p[-1]
    quadrupleList.operandsStack.append(oper)

#generar cuadruplo write con el pop de pilaOperadores
def p_np_generate_write_quadruple(p):
    '''
    np_generate_write_quadruple : empty
    '''

    quadrupleList.addQuadrupleReadWrite("WRITE",quadrupleList.operandsStack.pop(),'','')

#############################write#############################

#############################read#############################
#generar cuadruplo read con operando que viene antes
def p_np_generate_read_quadruple(p):
    '''
    np_generate_read_quadruple : empty
    '''

    global operand
    operand=p[-1]
    for vt in reversed(varsTablesPile):
        if operand in vt.table:
            if vt.table[idPush].dim == None:
                quadrupleList.addQuadrupleReadWrite("READ",vt.table[operand].address,'','')


            return

    print(f"Variable {idPush} not declared")
    exit()


#############################read#############################

#############################while#############################
#pushear actual cuadruplo a la pila de saltos para regresar despues para llenarlo
def p_np_while_push_jumpStack(p):
    '''
    np_while_push_jumpStack : empty
    '''
    quadrupleList.jumpsStack.append(quadrupleList.cont)

#generar gotoF despues de while
def p_np_while_generate_gotoF(p):

    '''
    np_while_generate_gotoF : empty
    '''

    quadrupleList.generateGoToFWhile()

#generar goto para regresar a inicio de evaluacion de exp de while
def p_np_while_generate_goto(p):
    '''
    np_while_generate_goto : empty
    '''
    quadrupleList.generateGoToWhile()
#############################while#############################



#############################for#############################
#pushear la variable a la que se le va  asignar una exp para saber si ya esta declarada
def p_np_for_push_id(p):
    '''
    np_for_push_id : empty
    '''


    global pushID
    pushID= p[-1]

    for vt in reversed(varsTablesPile):
        if pushID in vt.table:
            if vt.table[pushID].dim != None:
                global DIMid
                DIMid=1
                quadrupleList.dimensionalOperandsStack.append(pushID)
                quadrupleList.typesStack.append(vt.table[pushID].type)
                quadrupleList.operatorsStack.append('(')
            elif vt.table[pushID].dim == None:
                quadrupleList.operandsStack.append(vt.table[pushID].address)
                quadrupleList.typesStack.append(vt.table[pushID].type)
                if vt.table[pushID].type != "int" and vt.table[pushID].type != "float":
                    print(f"Variable {idPush} not numeric type")
                    exit()


            return



    print(f"Variable {idPush} not declared")
    exit()

#resolver la primera exp a la cual vamos a asignar al id anterior y asignarlo como la VC
def p_np_for_FIRSTexp(p):
    '''
    np_for_FIRSTexp : empty
    '''
    quadrupleList.generateVControlQuadruple()

#resolver la exp que va despues de TO para saber hasta donde se tiene que llegar
def p_np_for_SECONDexp(p):
    '''
    np_for_SECONDexp : empty
    '''
    quadrupleList.generateVFinalQuadruple()

#hacer el cambio en la variable de control del for
def p_np_for_changesVC(p):
    '''
    np_for_changesVC : empty
    '''
    addConstantsTable(1)
    quadrupleList.forChangeVC(constantsTable[1])
#############################for#############################

#############################functions call#############################
#checar que el id antes de () exista para saber si la funcion existe en la tabla de funciones
def p_np_check_func_exists(p):
    '''
    np_check_func_exists : empty
    '''
    global idVerify
    idVerify =p[-1]

    functionId = p[-1]
    if not functionId in current_functionsTable.table:
          print(f"Function {functionId} not declared")
          exit()
    else:
        quadrupleList.typesStack.append(current_functionsTable.table[functionId].type)

    global parameter_counter
    parameter_counter = 0

#checar la cantidad de parametros respecto a los que tenemos en lista para saber si coincide el numero
def p_np_check_func_params(p):
    '''
    np_check_func_params : empty
    '''
    functionId = p[-6]
    paramsInDirectory = [param.type for param in current_functionsTable.table[functionId].parameters]
    currentCallParams = [quadrupleList.typesStack.pop(-1) for x in range(parameter_counter)]
    currentCallParams = currentCallParams[::-1]

    if not len(paramsInDirectory)==len(currentCallParams):
        print(f"Wrong number of arguments in {functionId} expected {len(paramsInDirectory)}, given {len(currentCallParams)}")
        exit()


    if not paramsInDirectory == currentCallParams:
       print(f"At least one type mismatch in parameters in {functionId} call")
       exit()

    del globals()["parameter_counter"]

#aumentar el numero de parametros que se llevan en la llamada es decir cada que encuentre un parametro en la llamada aumenta el contador
def p_np_check_func_params_counter(p):
    '''
    np_check_func_params_counter : empty
    '''
    global parameter_counter
    parameter_counter +=1

#despues de declarar una clase se verifica que no este duplicada
def p_np_check_class_exists(p):
    '''
    np_check_class_exists : empty
    '''
    className = p[-2]
    if className in classesTable.table:
        print(f"Class {className} already exists")
        exit()

#se crea el arreglo con la cantidad de temporales de una funcion para llevar su conteo
def p_np_init_func_tempTable(p):
    '''
    np_init_func_tempTable : empty
    '''
    global current_funcTempTable
    current_funcTempTable = [0,0,0,0]

#hacer pop de la pila de tabla de variables para destruirla despues de su uso
def p_np_pop_varsTable(p):
    '''
    np_pop_varsTable : empty
    '''
    varsTablesPile.pop(-1)
############ Helper Functions ############
#aumentar el contador de cada tipo de temporal para irlo registrando en la lista de cantidad de temporales que ocupa una funcion
def registerTempVariable(tempType):


    temp = "current_funcTempTable" in globals()
    if not temp:
        return

    if tempType == "int":
        current_funcTempTable[0]+=1
    elif tempType == "float":
        current_funcTempTable[1]+=1
    elif tempType == "char":
        current_funcTempTable[2]+=1
    elif tempType == "bool":
        current_funcTempTable[3]+=1

######################Quadruples function call Amauri################
#generar cuadruplo de ENDFUNC despues del final de una funcion
def p_np_generate_endfunc_quad(p):
    '''
    np_generate_endfunc_quad : empty
    '''
    quadrupleList.generateEndFuncModule()

#generar cuadruplo ERA de la llamada
def p_np_generate_ERA_quad_func_call(p):
    '''
    np_generate_ERA_quad_func_call : empty
    '''
    quadrupleList.generateERAFuncCall(idVerify)

#generar cuadruplo de goSub del id de llamada y con su cuadruplo de inicio
def p_np_generate_goSub_function_call(p):
    '''
    np_generate_goSub_function_call : empty
    '''

    quadrupleList.generateGoSubFuncCall(idVerify,current_functionsTable.table[idVerify].quadrupleStart)
#generar cuadruplo RET ya que en todas nuestras funciones tienen RET
def p_np_generate_return_func(p):
    '''
    np_generate_return_func : empty
    '''

    quadrupleList.generateFuncReturnQuad(current_func_name)

#despues de pasar por una función si es que se llama se asigna el valor de la variable que se encuentra en variables globales, asignar su valor nuevo en un temporal para futuras operacioes
def p_np_assign_global_to_temporal_func_call(p):
    '''
    np_assign_global_to_temporal_func_call : empty
    '''
    type= varsTablesPile[0].table[idVerify].type

    quadrupleList.assignGlobalFuncCall(varsTablesPile[0].table[idVerify].address,type)
######################Quadruples function call Amauri################


#########################################Memory##################################################
#iniciar los contadores de memoria global para al contador al declarar una variable sumarle su direccion base correspondientes
def p_np_start_global_memory_counter(p):
    '''
    np_start_global_memory_counter : empty
    '''
    global global_memory_counter_int
    global_memory_counter_int = 0

    global global_memory_counter_float
    global_memory_counter_float = 0

    global global_memory_counter_char
    global_memory_counter_char = 0

    global global_memory_counter_bool
    global_memory_counter_bool = 0

    global global_memory_counter_array
    global_memory_counter_array = 0

    global global_memory_counter_matrix
    global_memory_counter_matrix = 0

    global global_memory_counter_flag
    global_memory_counter_flag = True

    quadrupleList.resetTemporalsCounter()

#iniciar los contadores de memoria local para al contador al declarar una variable sumarle su direccion base correspondientes
def p_np_start_local_memory_counter(p):
    '''
    np_start_local_memory_counter : empty
    '''
    global local_memory_counter_int
    local_memory_counter_int = 0

    global local_memory_counter_float
    local_memory_counter_float = 0

    global local_memory_counter_char
    local_memory_counter_char = 0

    global local_memory_counter_bool
    local_memory_counter_bool = 0

#despues de acabar con las variables globales se detiene el contador de globales para usar ahora los contadores de locales
def p_np_stop_global_memory_counter(p):
    '''
    np_stop_global_memory_counter : empty
    '''
    global global_memory_counter_flag
    global_memory_counter_flag = False
#generar cuadruplo por cada parametro en llamada a funcion
def p_np_generate_quad_parameter(p):
    '''
    np_generate_quad_parameter : empty
    '''
    global paramPop
    paramPop = quadrupleList.operandsStack.pop()
    quadrupleList.addQuadrupleParamFuncCall(paramPop,parameter_counter)
###########################################################################################
#rellenar cuadruplo de goto a main
def p_np_fill_goto_main_quad(p):
    '''
    np_fill_goto_main_quad : empty
    '''
    quadrupleList.fillGoToMainQuad()

############Constants############
#guardar constante
def p_np_saveConstantI(p):
    '''
    np_saveConstantI : empty
    '''
    global ci_counter

    constant = p[-1]
    if constant not in constantsTable:
        constantsTable[constant] = CI[0] + ci_counter
        ci_counter += 1
#guardar constante flotante
def p_np_saveConstantF(p):
    '''
    np_saveConstantF : empty
    '''
    global cf_counter

    constant = p[-1]
    if constant not in constantsTable:
        constantsTable[constant] = CF[0] + cf_counter
        cf_counter += 1




###########################arrays###########################
# en esta parte se crean los cuadruplos para variables dimensionadas
def p_np_create_dimensional_quads(p):
    '''
    np_create_dimensional_quads : empty
    '''
    #bool para saber si es una variable global para saber si buscar en tabla actual o en la primer tabla de variables
    global isGlobalDimensional
    isGlobalDimensional =False
    #bool para saber si es un arreglo si es falso, significa que es una matriz
    global isArrayCall
    isArrayCall = True

    addConstantsTable(0)



    ## sacar el limite superior de variable
    global idArray
    idArray = quadrupleList.dimensionalOperandsStack[-1]
    # se saca el limite superior para las operaciones y se checa si es un arreglo o matriz y si es global o no la variable para saber donde buscar exactamente
    if idArray in current_varsTable.table:
        Lsuperior= current_varsTable.table[idArray].dim[DIMid-1]

        if len(current_varsTable.table[idArray].dim) > 1:
            isArrayCall = False

    elif idArray in varsTablesPile[0].table:
        Lsuperior= varsTablesPile[0].table[quadrupleList.dimensionalOperandsStack[-1]].dim[DIMid-1]
        isGlobalDimensional = True

        if len(varsTablesPile[0].table[idArray].dim) > 1:
            isArrayCall = False

    #si el limite superior no esta en la tabla de constantes se mete

    addConstantsTable(Lsuperior)


    #generarr cuadruplo de verify para saber si esta dentro del limite del arreglo
    quadrupleList.addQuadrupleVerifyArray(quadrupleList.operandsStack[-1],constantsTable[0],constantsTable[Lsuperior])

    #si la dimension es 1 y no es un arreglo, significa que primero se debe multiplicar por d2 porque es una matriz
    if DIMid == 1 and not isArrayCall:

        aux= quadrupleList.operandsStack.pop()
        type= quadrupleList.typesStack.pop()
        #y se checa si es una variable global o local y dependiendo de eso es donde se busca
        if isGlobalDimensional:
            addConstantsTable(varsTablesPile[0].table[quadrupleList.dimensionalOperandsStack[-1]].dim[DIMid-1]+1)
            quadrupleList.addQuadruple("*",aux,constantsTable[varsTablesPile[0].table[quadrupleList.dimensionalOperandsStack[-1]].dim[DIMid-1]+1],0,type)
        else:
            addConstantsTable(current_varsTable.table[quadrupleList.dimensionalOperandsStack[-1]].dim[DIMid-1]+1)
            quadrupleList.addQuadruple("*",aux,constantsTable[current_varsTable.table[quadrupleList.dimensionalOperandsStack[-1]].dim[DIMid-1]+1],0,type)

    #despues de eso se debe sumar s2 con el temporal anterior que es s1*d2
    if DIMid>1:
        aux2= quadrupleList.operandsStack.pop()
        type2= quadrupleList.typesStack.pop()
        aux1=quadrupleList.operandsStack.pop()
        type1= quadrupleList.typesStack.pop()
        typeSC, err = semanticCube.semantic(type1, type2, "+")
        quadrupleList.addQuadruple("+",aux1,aux2,0,typeSC)

#se aumenta la dimension despues de encontrarse que hay un indice extra es decir, que es matriz
def p_np_DIM_plus(p):
    '''
    np_DIM_plus : empty
    '''
    global DIMid
    DIMid=DIMid+1

#suma la dirección base que es la operacion final y se busca la dirección base de la variable en la tabla de variables
def p_np_sum_baseA_array(p):
    '''
    np_sum_baseA_array : empty
    '''
    global idArray
    global isGlobalDimensional

    #si es falso esta en la current si no esta en globals
    if not isGlobalDimensional:
        baseAdd =current_varsTable.table[idArray].address
    else:
        baseAdd =varsTablesPile[0].table[idArray].address

    addConstantsTable(baseAdd)

    # se crea el cuadruplo de suma de direccion base y se almacena en un temporal pointer
    quadrupleList.addQuadruple("+",quadrupleList.operandsStack.pop(),constantsTable[baseAdd],0,"pointer")
    quadrupleList.typesStack.pop()
    quadrupleList.eliminateFakeVoid()
###########################arrays###########################

############################################################
# se resetea el contador de temporales despues de cada funcion
def p_np_reset_temp_counter(p):
    '''
    np_reset_temp_counter : empty
    '''
    quadrupleList.resetTemporalsCounter()

# se cambia el scope de las variables para saber si es global o local
def p_np_set_temp_global_flag(p):
    '''
    np_set_temp_global_flag : empty
    '''
    quadrupleList.changeScope()
############################################################
#se parsea con yacc
parser = yacc()

#archivo en donde esta todo nuestro codigo
f = open('test.c', 'r')

# se lee el archivo y se hace parse
content = f.read()
case_correct_01 = parser.parse(content)

#en esta sección se mete al ovejota: constantes y sus direcciones, cuadruplos y todas las funciones
f = open("ovejota.txt","w+")
for key in constantsTable:
    f.write(f"{key}|{constantsTable[key]},")
f.write("\n")


for func in program.functionsTable.table:
    varCount = program.functionsTable.table[func].variablesCount
    varCount = '%'.join(str(v) for v in varCount)

    params = ""
    for param in program.functionsTable.table[func].parameters:
        params += str(param.id) + "/" + str(param.type) + ";"

    f.write(f"{func}|{program.functionsTable.table[func].quadrupleStart}|{varCount}|{params},")
f.write("\n")

for key in program.varsTable.table:
    if program.varsTable.table[key].scope == "globalFunction":

        f.write(f"{key}|{program.varsTable.table[key].address},")
f.write("\n")

print(program.variablesCount)

program.variablesCount[4] =  quadrupleList.counter_tInt
program.variablesCount[5] =  quadrupleList.counter_tFloat
program.variablesCount[6] = quadrupleList.counter_tChar
program.variablesCount[7] = quadrupleList.counter_tBool

programVarCount = ','.join(str(v) for v in program.variablesCount)




f.write(programVarCount)
f.write("\n")


f.close()

print(constantsTable)
quadrupleList.quadrupleListToString()




program.toString()
