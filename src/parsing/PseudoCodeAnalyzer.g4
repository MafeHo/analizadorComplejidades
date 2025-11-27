grammar PseudoCodeAnalyzer; 

// Regla de inicio (start rule): el programa completo
program: (class_declaration | subroutine_declaration)+ EOF; 

// -----------------------------------------------------------
// ---------- SECCIÓN 1: REGLAS LÉXICAS (TOKENS) -------------
// -----------------------------------------------------------

// Símbolos y Palabras Clave de Estructura
BEGIN: 'begin';
END: 'end';
CLASS: 'Clase';
NULL: 'NULL';

// Símbolos y Palabras Clave de Control de Flujo
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

// Asignación y Comentarios
ASSIGN: '<-'; // Cambiado de '🡨'
COMMENT: '//' ~[\r\n]* -> skip; // Cambiado de '►'

// Operadores Matemáticos
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV_REAL: '/';
OP_MOD: 'mod';
OP_DIV_ENTERA: 'div';
CEIL: '┌';
FLOOR: '└';
DOT: '.';

// Operadores Relacionales
OP_LT: '<';
OP_GT: '>';
OP_LE: '≤';
OP_GE: '≥';
OP_EQ: '=';
OP_NE: '≠';

// Operadores Booleanos
OP_AND: 'and';
OP_OR: 'or';
OP_NOT: 'not';
TRUE: 'T';
FALSE: 'F';

// Símbolos varios
COLON: ',';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
RANGE: '..';

// Identificadores y Literales
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+;

// Espacios en blanco e ignorados
WS: [ \t\r\n]+ -> skip;

// -----------------------------------------------------------
// ---------- SECCIÓN 2: REGLAS SINTÁCTICAS (PARSER) ---------
// -----------------------------------------------------------

// ----------------- CLASES Y OBJETOS -----------------

// Clase {Atributo1 Atributo2...}
class_declaration: CLASS ID '{' ID (ID)* '}'; 

// Declaración de variables locales
local_vars_declaration: (CLASS ID ID) | 
                        (ID (LBRACKET expression? RBRACKET)? (COLON ID (LBRACKET expression? RBRACKET)?)*) 
                        ;

// ----------------- SUBRUTINAS -----------------

subroutine_declaration: ID LPAREN (parameter_declaration (COLON parameter_declaration)*)? RPAREN
                      BEGIN 
                      (local_vars_declaration ';')*
                      statement_list
                      END;

// Parámetros
parameter_declaration: (CLASS ID ID) | 
                       (ID (LBRACKET expression? RBRACKET)+) | 
                       ID;

// ----------------- LISTA DE SENTENCIAS -----------------

statement_list: (statement ';')*;

statement: assignment | for_loop | while_loop | repeat_loop | if_statement | call_statement;

// ----------------- ASIGNACIÓN -----------------

assignment: variable ASSIGN expression;

// variable: A[i] o x.f
variable: ID (LBRACKET expression RBRACKET)* | ID DOT ID; 

// ----------------- CONTROL DE FLUJO -----------------

// for var 🡨 inicio to limite do begin ... end
for_loop: FOR ID ASSIGN expression TO expression DO BEGIN statement_list END;

// while (condicion) do begin ... end
while_loop: WHILE LPAREN expression RPAREN DO BEGIN statement_list END;

// repeat ... until (condicion)
repeat_loop: REPEAT statement_list UNTIL LPAREN expression RPAREN;

// If (condicion) then begin ... end else begin ... end
if_statement: IF LPAREN expression RPAREN THEN BEGIN statement_list END 
            (ELSE BEGIN statement_list END)?;

// ----------------- LLAMADA -----------------

// CALL nombre_subrutina(parámetros)
call_statement: CALL ID LPAREN (expression (COLON expression)*)? RPAREN;

// ----------------- EXPRESIONES Y CONDICIONES -----------------

expression: 
          // Nivel 1: Unario/Función/Terminales
          (CEIL expression FLOOR) 
          | (LPAREN expression RPAREN) 
          | (OP_NOT expression)
          | (ID LPAREN (expression (COLON expression)*)? RPAREN)
          | variable
          | NUMBER
          | TRUE
          | FALSE
          | NULL
          
          // Nivel 2: Multiplicación, División, Mod
          | expression OP_MUL expression
          | expression OP_DIV_REAL expression
          | expression OP_MOD expression
          | expression OP_DIV_ENTERA expression

          // Nivel 3: Suma y Resta
          | expression OP_ADD expression
          | expression OP_SUB expression

          // Nivel 4: Relacionales
          | expression (OP_LE | OP_GE | OP_EQ | OP_NE | OP_LT | OP_GT) expression

          // Nivel 5: Booleanos (AND, OR)
          | expression OP_AND expression
          | expression OP_OR expression
          ;