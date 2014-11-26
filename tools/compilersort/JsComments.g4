grammar JsComments;

program
    : body+;

body
    : '/**' comment '*/' | (IDENTIFIER | '}');

comment
    : (IDENTIFIER | '}')*? (minterface | constructor | mnamespace) (IDENTIFIER | '}')*?
    | (IDENTIFIER | '}')*?;

mnamespace
    : '@namespace';

minterface
    : '@interface' (mextends)*;

constructor
    : '@constructor' (mextends)* (mimplements)* | (mextends)* (mimplements)* '@constructor';

mextends
    : '@extends {' IDENTIFIER '}';

mimplements
    : '@implements {' IDENTIFIER '}';

IDENTIFIER    : ('a'..'z' | 'A'..'Z' | '_')
                ('.' | 'a'..'z' | 'A'..'Z' | '_' | '0'..'9')*;

WHITESPACE
    : [ \t\r\n]+ -> skip;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip;

FILTER
    : . -> skip;
