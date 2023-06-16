<program> -> <main_block>

<main_block> -> 'int' 'main' '(' ')' '{' <statements> '}'

<type> -> 'int' | 'float' | 'char'

<declaration> -> <type> <identifier> <assign> <declaration_list>

<assign> -> '=' <constant> | ε

<assignment> -> <identifier> '=' <constant> ';'

<declaration_list> = ',' <identifier> <assign> <declaration_list> | ';' 

<identifier> -> <LETTER> (<LETTER> | <DIGIT>)*

<constant> -> <DIGIT>+ 
            | '"' <LETTER> '"'

<statements> -> <statement>*

<statement> -> <declaration>
           | <read_statement>
           | <write_statement>
           | <selection_statement>
           | <loop_statement>
           | <until_statement>
           | <if_statement>

<read_statement> -> 'read' '(' <type> ',' <identifier> ')' ';'

<write_statement> -> 'write' '(' <string> ',' <identifier> ')' ';'

<string> -> '"' (CHARACTER | ESCAPE_SEQUENCE)* '"'

<if_statement> -> 'if' '(' <condition> ')' 'so' '{' <statements> '}'

<loop_statement> -> 'loop' '(' condition ')' '{' statements '}'

<condition> -> <expression> <multi_expression> <CONDITIONAL> <expression> <multi_expression> ('++')?

<multi_expression> -> <AND_OR> <expression> <multi_expression> | ε

<selection_statement> -> 'selector' ':' <identifier> '{' <selector_cases> '}'

<selector_cases> -> <selector_case>+

<selector_case> -> 'select' <constant> ':' <statements> | 'other' ':' <statements>

<until_statement> -> 'until' '(' <condition> ')' '{' statements '}'

<expression> -> term (('+'|'-') term)*

term -> factor (('*'|'/') factor)*

factor -> identifier
        | constant
        | '(' expression ')'

LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k'
           | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 'w' | 'x' | 'y' | 'z'
           | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K'
           | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'W' | 'X' | 'Y' | 'Z'
           | '_'

DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

CHARACTER -> any printable ASCII character except '"' or '\'

ESCAPE_SEQUENCE -> '\' '"' | '\' '\'

CONDITIONAL = '<' | '>' | '>=' | '<=' | '==' | '!='

AND_OR = '&' | '|'
