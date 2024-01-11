

import ply.lex as lex
import ply.yacc as yacc


player = []
young_player = []
awards = []
fair_play = []

###DEFINING TOKENS###

tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW','OPENCOLUMN', 'CLOSECOLUMN',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' , 'OPENDATAHEAD', 'CLOSEDATAHEAD' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
t_ignore = '\t'


###############Tokenizer Rules################

def t_BEGINTABLE(t):

    '''<h2><span\sclass="mw-headline"\sid="Awards">Awards</span></h2>'''
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

# def t_OPENCOLUMN(t):
#     '''<td[^>]*>'''
#     return t

# def t_CLOSECOLUMN(t):
#     '''</td[^>]*>'''
#     return t

# def t_OPENHEADER(t):
#     '''<td[^>]*>'''
#     return t

# def t_CLOSEHEADER(t):
#     '''</th[^>]*>'''
#     return t

def t_OPENHREF(t):
    '''<a[^>]*>'''
    return t

def t_CLOSEHREF(t):
    '''</a[^>]*>'''
    return t

def t_CLOSEDATA(t):
    '''</td[^>]*>'''
    return t

def t_CONTENT(t):
    '''[A-Za-z0-9,àâçéèêëîïôûùüÿñæœ ]+'''
    return t

def t_OPENDIV(t):
    '''<div[^>]*>'''

def t_CLOSEDIV(t):
    '''</div[^>]*>'''

def t_OPENDATAHEAD(t):
    '''<th[^>]*>'''
    return t

def t_CLOSEDATAHEAD(t):
    '''</th[^>]*>'''
    return t

def t_OPENSTYLE(t):
    '''<style[^>]*>'''

def t_CLOSESTYLE(t):
    '''</style[^>]*>'''


def t_OPENDATA(t):
    '''<td[^>]*>'''
    return t

def t_OPENSPAN(t):
    '''<span[^>]*>'''

def t_CLOSESPAN(t):
    '''</span[^>]*>'''

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

def p_handledata(p):
    '''handledata : OPENDATA OPENHREF CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handledata
                  | OPENDATA OPENHREF CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CLOSEHREF CLOSEDATA handledata
                  | OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handledata
                  | OPENCOLUMN CLOSECOLUMN OPENDATA OPENCOLUMN CONTENT skiptag CONTENT handledata CLOSECOLUMN handlecolumn CLOSEDATA
                  | '''
    if(len(p) == 10):
        #print(p[6]+"10")
        player.append(p[6])
    
    if(len(p) == 11):
        #print(p[6] + "" + p[7]+"11")
        young_player.append(p[6] + "" + p[7])

    if(len(p) == 8):
        #print(p[4]+"8")
        fair_play.append(p[4])


# def p_handledata1(p):
#     '''handledata1 : OPENDATA OPENHREF CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CLOSEHREF CLOSEDATA handledata1
#                    | '''
#     if(len(p) == 11):
#         print(p[6])


def p_handlecolumn(p):
    '''handlecolumn : OPENCOLUMN handledata CLOSECOLUMN handlecolumn
                    | '''

def p_handlerow(p):
    '''handlerow : OPENROW handledata CLOSEROW
                 | OPENCOLUMN CONTENT skiptag CONTENT handledata CLOSECOLUMN handlecolumn
                 | OPENCOLUMN CLOSECOLUMN OPENDATA OPENCOLUMN CONTENT skiptag CONTENT handledata CLOSECOLUMN handlecolumn CLOSEDATA
                 | '''

# def p_handlerow1(p):
#     '''handlerow1 : OPENROW handledata1 CLOSEROW
#                   | '''                 

def p_handleheaddata(p):
    '''handleheaddata : OPENDATAHEAD OPENHREF CONTENT CLOSEHREF CLOSEDATAHEAD handleheaddata
                      | OPENDATAHEAD CONTENT CLOSEDATAHEAD handleheaddata
                      | OPENDATA OPENCOLUMN CONTENT skiptag CONTENT handledata CLOSECOLUMN handlecolumn CLOSEDATA
                      | '''
    if(len(p) == 7):
        #print(p[3]+" handledata 7")
        awards.append(p[3])
    
    if(len(p) == 5):
        #print(p[2]+" handledata 3")
        awards.append(p[2])

def p_handleheadrow(p):
    '''handleheadrow : OPENROW handleheaddata CLOSEROW
                     | OPENDATA OPENCOLUMN CONTENT skiptag CONTENT handledata CLOSECOLUMN handlecolumn CLOSEDATA OPENDATA CLOSEDATA
                     | '''

def p_random(p):
    '''random : OPENROW OPENDATA CONTENT CONTENT CLOSEDATA OPENDATA CONTENT CONTENT CLOSEDATA OPENDATA CONTENT CONTENT CLOSEDATA CLOSEROW'''

def p_table(p):
    '''table : BEGINTABLE skiptag OPENTABLE handleheadrow handlerow handleheadrow handlerow random handleheadrow handlerow handleheadrow handlerow handleheadrow handlerow'''

def p_error(p):
    pass







#########################################################################################
#########DRIVER FUNCTION#######

def award():
    file_obj= open('Fifa_data.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    return awards, fair_play, young_player, player

###############################################################################

# if __name__ == '__main__':
#     main()