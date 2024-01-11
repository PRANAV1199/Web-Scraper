import ply.lex as lex
import ply.yacc as yacc



team_list = []


###DEFINING TOKENS###

tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW','OPENCOLUMN', 'CLOSECOLUMN',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
t_ignore = '\t'


###############Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<h3><span\sclass="mw-headline"\sid="Draw">Draw</span></h3>'''
    return t


def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t

def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t

def t_OPENROW(t):
    '''<tr[^>]*>'''
    return t

def t_CLOSEROW(t):
    '''</tr[^>]*>'''
    return t

def t_OPENCOLUMN(t):
    '''<td[^>]*>'''
    return t

def t_CLOSECOLUMN(t):
    '''</td[^>]*>'''
    return t

def t_OPENHEADER(t):
    '''<th[^>]*>'''
    return t

def t_CLOSEHEADER(t):
    '''</th[^>]*>'''
    return t

def t_OPENHREF(t):
    '''<a[^>]*>'''
    return t

def t_CLOSEHREF(t):
    '''</a[^>]*>'''
    return t

def t_OPENDATA(t):
    '''<span[^>]*>'''
    return t

def t_CLOSEDATA(t):
    '''</span[^>]*>'''
    return t

def t_CONTENT(t):
    '''[A-Za-z0-9, ]+'''
    return t

def t_OPENDIV(t):
    '''<div[^>]*>'''

def t_CLOSEDIV(t):
    '''</div[^>]*>'''

def t_OPENSTYLE(t):
    '''<style[^>]*>'''

def t_CLOSESTYLE(t):
    '''</style[^>]*>'''

def t_OPENSPAN(t):
    '''<span[^>]*>'''
    return t

def t_CLOSESPAN(t):
    '''</span[^>]*>'''
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
#Fill with parsing rules

def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | '''

def p_handleData(p):
    '''handleData : OPENDATA OPENDATA CONTENT CLOSEDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA skiptag handleData
                  | OPENHREF CONTENT CLOSEHREF CLOSEDATA skiptag handleData OPENDATA OPENDATA CONTENT CLOSEDATA 
                  | '''
    if(len(p) == 11):
        team_list.append(p[6])


def p_handlecolumn(p):
    '''handlecolumn : OPENCOLUMN handleData CLOSECOLUMN handlecolumn
                    | OPENHEADER CONTENT skiptag CONTENT CONTENT CLOSEHEADER OPENROW CLOSEROW
                    | '''

def p_handlerow(p):
    '''handlerow : OPENROW OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW handlerow
                 | OPENROW handlecolumn CLOSEROW
                 | OPENCOLUMN handleData CLOSECOLUMN handlecolumn OPENROW OPENHEADER CLOSEROW CLOSEHEADER
                 | '''
    
def p_table(p):
    '''table : BEGINTABLE skiptag OPENTABLE handlerow'''

def p_error(p):
    pass







#########################################################################################
#########DRIVER FUNCTION#######

def team():
    file_obj= open('Fifa_data.html','r',encoding="utf-8")
    try : 
        data=file_obj.read()
    except :
        print("Unable to open file")
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    return team_list