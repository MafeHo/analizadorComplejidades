grammar PseudoCodeAnalyzer;

// -----------------------------------------------------------
// 1. ESTRUCTURA PRINCIPAL DEL PROGRAMA
// -----------------------------------------------------------
program: (structure_definition)* algorithm_definition EOF;

structure_definition: 
    class_definition 
    | array_definition 
    ;

// Definición de Clases: Clase Nombre { Atributos... }
class_definition: CLASS ID '{' ID (ID)* '}';

// Definición de Arreglos Globales: Nombre[Tamaño]
array_definition: ID LBRACKET expression RBRACKET;

// -----------------------------------------------------------
// 2. DEFINICIÓN DEL ALGORITMO
// -----------------------------------------------------------
algorithm_definition: 
    ID LPAREN (param_list)? RPAREN 
    BEGIN 
    (local_var_decl ';')* statement_list 
    END;

// Parámetros: nombre, nombre[..], Clase nombre
param_list: parameter (COLON parameter)*;
parameter: 
    CLASS ID ID                     # ParamObject
    | ID LBRACKET (RANGE)? RBRACKET # ParamArray
    | ID                            # ParamSimple
    ;

// Variables locales: x, y, z
local_var_decl: ID (COLON ID)*; 

// -----------------------------------------------------------
// 3. SENTENCIAS (STATEMENTS)
// -----------------------------------------------------------
// Permite sentencias terminadas opcionalmente en punto y coma
statement_list: (statement ';'?)*; 

statement: 
    assignment 
    | for_loop 
    | while_loop 
    | repeat_loop 
    | if_statement 
    | call_statement
    | return_statement
    ;

// Asignación: variable <- expresión
assignment: target_var ASSIGN expression;

// Variables objetivo (x, A[i], objeto.campo)
target_var: 
    ID (LBRACKET expression RBRACKET)+  # VarArray
    | ID DOT ID                         # VarField
    | ID                                # VarSimple
    ;

// --- Estructuras de Control ---

// For: for i <- 1 to n do begin ... end
for_loop: FOR ID ASSIGN expression TO expression DO BEGIN statement_list END;

// While: while (cond) do begin ... end
while_loop: WHILE LPAREN expression RPAREN DO BEGIN statement_list END;

// Repeat: repeat ... until (cond)
repeat_loop: REPEAT statement_list UNTIL LPAREN expression RPAREN;

// If: If (cond) then begin ... end else begin ... end
if_statement: IF LPAREN expression RPAREN THEN BEGIN statement_list END 
              (ELSE BEGIN statement_list END)?;

// Llamada: CALL nombre(args)
call_statement: CALL ID LPAREN (expression (COLON expression)*)? RPAREN;

// Retorno: return valor (CRUCIAL PARA RECURSIÓN)
return_statement: RETURN expression;

// -----------------------------------------------------------
// 4. EXPRESIONES MATEMÁTICAS Y LÓGICAS
// -----------------------------------------------------------
// El orden define la precedencia de operaciones
expression: 
    LPAREN expression RPAREN                                                # ExprParen
    | CEIL expression CEIL_CLOSE                                            # ExprCeil  // ┌ x ┐
    | FLOOR expression FLOOR_CLOSE                                          # ExprFloor // └ x ┘
    | OP_NOT expression                                                     # ExprNot
    | expression (OP_MUL | OP_DIV_REAL | OP_MOD | OP_DIV_INT) expression    # ExprMulDiv
    | expression (OP_ADD | OP_SUB) expression                               # ExprAddSub
    | expression (OP_LE | OP_GE | OP_EQ | OP_NE | OP_LT | OP_GT) expression # ExprRelational
    | expression OP_AND expression                                          # ExprAnd
    | expression OP_OR expression                                           # ExprOr
    | atom                                                                  # ExprAtom
    ;

// Átomos: Números, Variables, Booleanos, Llamadas a Función
atom: 
    NUMBER 
    | TRUE | FALSE | NULL
    | ID LPAREN (expression (COLON expression)*)? RPAREN // Detecta: Fibonacci(n-1)
    | target_var
    ;

// -----------------------------------------------------------
// 5. REGLAS LÉXICAS (TOKENS)
// -----------------------------------------------------------

// Palabras Clave
BEGIN: 'begin';
END: 'end';
CLASS: 'Clase';
NULL: 'NULL';
FOR: 'for';
TO: 'to';
WHILE: 'while';
REPEAT: 'repeat';
UNTIL: 'until';
IF: 'If';
THEN: 'then';
ELSE: 'else';
DO: 'do';
CALL: 'CALL';
RETURN: 'return' | 'Return'; // Soporta mayúscula/minúscula

// Operadores
ASSIGN: '<-';
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV_REAL: '/';
OP_MOD: 'mod';
OP_DIV_INT: 'div';

// Caracteres Especiales Matemáticos (Unicode)
CEIL: '\u250C';       // ┌
CEIL_CLOSE: '\u2510'; // ┐ 
FLOOR: '\u2514';      // └
FLOOR_CLOSE: '\u2518';// ┘

// Relacionales
OP_LT: '<';
OP_GT: '>';
OP_LE: '≤' | '<=';
OP_GE: '≥' | '>=';
OP_EQ: '=';
OP_NE: '≠' | '<>' | '!=';

// Lógicos
OP_AND: 'and';
OP_OR: 'or';
OP_NOT: 'not';
TRUE: 'T';
FALSE: 'F';

// Puntuación
COLON: ',';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
DOT: '.';
RANGE: '..';

// Identificadores y Números
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+;

// Ignorar espacios y comentarios
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;