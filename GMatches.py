import ply.lex as lex
import ply.yacc as yacc




home_team = []
away_team = []
score = []
ref_name = []
stad_name = []
attendance = []
goal_scorer = []
scorer = []
temp_list = []


###DEFINING TOKENS###

tokens = ('BEGINTABLE', 
'OPENTABLE',  'OPENROW', 'OPENLINK','CLOSESPAN','CLOSECOLUMN','CLOSETABLE',
'OPENHEADER', 'OPENSPAN','CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENCOLUMN','OPENDATA', 'CLOSEDATA' , 'CLOSEROW', 'TIME',
 'CLOSELINK','OPENDIV',
'CLOSELINKUL',  'OPENLINKINDEX', 'CLOSELINKINDEX',
 'CLOSEDIV', 'OPENLINKUL','OPENSTYLE', 'CLOSESTYLE', 'GARBAGE')
t_ignore = '\t'


###############Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<style\sdata-mw-deduplicate="TemplateStyles:r997937747">'''
    return t

def t_CLOSELINK(t):
    '''</link[^>]*>'''


def t_OPENLINK(t):
    '''<link[^>]*>'''

def t_CLOSEDATA(t):
    '''</a[^>]*>'''

def t_OPENDATA(t):
    '''<a[^>]*>'''

def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t

def t_OPENROW(t):
    '''<tr[^>]*>'''

def t_OPENCOLUMN(t):
    '''<td[^>]*>'''
    return t

def t_CLOSECOLUMN(t):
    '''</td[^>]*>'''
    return t

def t_OPENHEADER(t):
    '''<th[^>]*>'''
    return t

def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t

def t_CLOSEHEADER(t):
    '''</th[^>]*>'''
    return t
def t_CLOSEROW(t):
    '''</tr[^>]*>'''


def t_OPENLINKINDEX(t):
    '''<li[^>]*>'''
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

def t_CLOSELINKUL(t):
    '''</ul[^>]*>'''
    return t

def t_OPENLINKUL(t):
    '''<ul[^>]*>'''
    return t



def t_TIME(t):
    '''<time[^>]*>'''
    return t

def t_CLOSELINKINDEX(t):
    '''</li[^>]*>'''
    return t


def t_CONTENT(t):
    '''[A-Za-z0-9,àâçéèêëîïôûùüÿñæœÀÁÂÃÃĂAÄÀAĂÂÂĄAĄ ]+'''
    return t

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

def p_groupchange(p):
    '''groupchange : CONTENT groupchange
                   | OPENTABLE groupchange
                   | OPENHEADER groupchange
                   | CLOSEHEADER groupchange
                   | OPENLINKUL groupchange
                   | CLOSELINKUL groupchange
                   | OPENLINKINDEX groupchange
                   | CLOSELINKINDEX groupchange
                   | OPENCOLUMN groupchange
                   | CLOSECOLUMN groupchange
                   | CLOSETABLE groupchange
                   | '''


def p_handleteamdata(p):
    '''handleteamdata : OPENHEADER CONTENT skiptag CLOSEHEADER OPENHEADER CONTENT CONTENT skiptag CLOSEHEADER OPENHEADER CONTENT CONTENT CLOSEHEADER
                      | '''
    if(len(p) == 14):
        #print(p[2] + " " + p[6] + " " + p[7] + " " + p[12])
        home_team.append(p[2])
        away_team.append(p[12])
        score.append([p[6], p[7]])

def p_handlescore(p):
    '''handlescore : OPENLINKINDEX CONTENT skiptag CLOSELINKINDEX handlescore
                   | OPENHEADER CONTENT OPENHEADER CONTENT CONTENT skiptag CLOSEHEADER CONTENT CLOSEHEADER
                   | OPENHEADER OPENCOLUMN CONTENT CLOSECOLUMN OPENHEADER CONTENT CONTENT skiptag CLOSEHEADER CONTENT CLOSEHEADER
                   | '''


    if(len(p) == 6):
        scorer.append(p[2])
        

def p_handleawayscore(p):
    '''handleawayscore : OPENLINKINDEX CONTENT CONTENT skiptag CLOSELINKINDEX handleawayscore
                       | OPENLINKINDEX CONTENT handleawayscore
                       | OPENTABLE OPENCOLUMN CONTENT CONTENT skiptag CONTENT CLOSECOLUMN CLOSETABLE
                       | OPENHEADER CONTENT CONTENT skiptag CLOSEHEADER OPENCOLUMN CONTENT CLOSECOLUMN
                       | OPENHEADER CONTENT OPENHEADER CONTENT CONTENT skiptag CLOSEHEADER CONTENT CLOSEHEADER OPENHEADER CLOSEHEADER
                       | '''
    # if(len(p) == 7):
    #     print(p[3])

def p_handlehomescorer(p):
    '''handlehomescorer : OPENCOLUMN skiptag OPENLINKUL handlescore CLOSELINKUL CLOSECOLUMN
                        | OPENCOLUMN CLOSECOLUMN
                        | OPENLINKINDEX CONTENT CONTENT handleawayscore
                        | '''

def p_handleawaypenaltyscorer(p):
    '''handleawaypenaltyscorer : OPENCOLUMN skiptag OPENLINKUL handleawayscore CLOSELINKUL CLOSECOLUMN
                               | OPENCOLUMN CLOSECOLUMN
                               | OPENLINKINDEX CONTENT CONTENT handleawayscore
                               | '''

def p_handlereport(p):
    '''handlereport : OPENCOLUMN skiptag CLOSECOLUMN
                    | OPENHEADER CONTENT CLOSEHEADER OPENCOLUMN CONTENT skiptag CLOSECOLUMN
                    | '''

def p_handlescorerdata(p):
    '''handlescorerdata : handlehomescorer handlereport handlehomescorer
                        | OPENHEADER CONTENT CLOSEHEADER OPENCOLUMN CONTENT skiptag CLOSECOLUMN
                        | '''

def p_handlestadiumdata(p):
    '''handlestadiumdata : CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                         | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                         | OPENCOLUMN skiptag CLOSELINKUL CLOSECOLUMN
                         | '''
    if(len(p) == 11):
        #print(p[1] + " " + p[5] + " " + p[8])
        stad_name.append(p[1])
        attendance.append(p[5])
        ref_name.append([p[8]])

    
    if(len(p) == 12):
        #print(p[1] + " " + p[5] + " " + p[8] + " " + p[11])
        stad_name.append(p[1])
        attendance.append(p[5])
        ref_name.append([p[8], p[11]])
    

def p_handlepenaltyscoredata(p):
    '''handlepenaltyscoredata : handlehomescorer OPENHEADER CONTENT CONTENT CLOSEHEADER handleawaypenaltyscorer'''

def p_handlepenalty(p):
    '''handlepenalty : OPENHEADER CONTENT CLOSEHEADER handlepenaltyscoredata
                     | '''


def p_time(p):
    '''time : TIME skiptag OPENTABLE handleteamdata handlescorerdata handlepenalty CLOSETABLE handlestadiumdata groupchange time
            | '''


def p_table(p):
    '''table : BEGINTABLE skiptag time'''


def p_error(p):
    pass







#########################################################################################
#########DRIVER FUNCTION#######

def match_data():
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
    ret = [home_team, away_team, score, stad_name, attendance, ref_name, scorer]
    return ret