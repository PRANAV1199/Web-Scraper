import ply.lex as lex
import ply.yacc as yacc




###DEFINING TOKENS###

tokens = ('OPENTIME', 'CLOSETIME','BEGINTABLE',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
t_ignore = '\t'


###############Tokenizer Rules################


i=1
j=1

def t_BEGINTABLE(t):

    '''<h3><span\sclass="mw-headline"\sid="Stadiums">Stadiums</span></h3>'''
   
    return t


def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t

def t_OPENTIME(t):
    '''<time[^>]*>'''
 


def t_CLOSETIME(t):
    '''</time[^>]*>'''
     


def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t

def t_OPENROW(t):
    '''<tr[^>]*>'''
    return t

def t_CLOSEROW(t):
    '''</tr[^>]*>'''
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
    '''<td[^>]*>'''
    return t

def t_CLOSEDATA(t):
    '''</td[^>]*>'''
    return t

def t_CONTENT(t):
    '''[A-Za-z0-9, ]+'''
    return t

''

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
##Fill with parsing rules
def p_start(p):
    '''start : table'''
    p[0] = p[1]



       


def p_name(p):
    '''name : CONTENT
            | CONTENT name
            | OPENTIME OPENTABLE OPENTABLE'''
    if len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | OPENTIME skiptag
               | CLOSETIME skiptag
               | '''


def p_hd(p):
    '''hd : CLOSEHREF'''

def p_handleData(p):
    '''handleData : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
                  | OPENHREF CLOSEDATA CLOSEDATA
                  | OPENDATA CONTENT skiptag CLOSEDATA handleData
                  | OPENDATA skiptag CLOSEDATA handleData
                  | OPENTIME CLOSEHREF OPENHREF OPENHREF
                  | '''
   
    if len(p) == 7:
        p_stadium_name.append(p[3])
        #print(p[3])
    if len(p) == 6:
        #print(p[2])
        p_stadium_capacity.append(p[2])


def p_hr(p):
    '''hr : CLOSEHEADER '''


def p_handlerow(p):
    '''handlerow : OPENROW OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER CLOSEROW handlerow
                 | OPENTIME OPENTIME CLOSETIME CLOSETIME CLOSEHREF
                 | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handleData CLOSEROW handlerow
                 | OPENROW handleData CLOSEROW handlerow
                 | OPENTIME OPENROW CLOSEROW CONTENT
                 | '''
   
def p_table(p):
    '''table : BEGINTABLE skiptag OPENTABLE handlerow
             | OPENTIME BEGINTABLE OPENTABLE table
             | '''

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

def p_error(p):
    pass

p_stadium_name=[]
p_stadium_capacity=[]

#########################################################################################
#########DRIVER FUNCTION#######

def venue_details():
    file_obj= open('Fifa_data.html','r',encoding="utf-8")

    try :
       
        if i==1:
            data=file_obj.read()
            lexer = lex.lex()
            lexer.input(data)
    #########Fill the blank here for parser and lexer
        if j==1:
            parser=yacc.yacc()
            parser.parse(data)
        file_obj.close()
    except :
        print("Unable to open")
    return p_stadium_name, p_stadium_capacity