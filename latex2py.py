import ply.lex as lex

tokens = (
    'floatnumber',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'NAME',
 )
 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK  = r'{'
t_RBRACK  = r'}'
t_ignore  = ' \t' # A string containing ignored characters (spaces and tabs)

digit     = r'([0-9])'
digitpart     =  r'({digit}[_]{digit})*'.format(digit=digit)
fraction      =  '\.{digitpart}'.format(digitpart=digitpart)
exponent      =  '(e|E)[+|-]{digitpart}'.format(digitpart=digitpart)
pointfloat    =  '[{digitpart}]{fraction}|{digitpart}\.'.format(digitpart=digitpart, fraction=fraction)
exponentfloat =  '({digitpart}|{pointfloat}){exponent}'.format(digitpart=digitpart, pointfloat=pointfloat, exponent=exponent)
floatnumber =  '{pointfloat}|{exponentfloat}'.format(pointfloat=pointfloat, exponentfloat=exponentfloat)
print(floatnumber)
# A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)    
#     return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

