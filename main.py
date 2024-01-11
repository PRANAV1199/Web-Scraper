##importing functions from lex files to get the data
from Awards import award
from Team import team
from StadiumCapacity import venue_details
from GMatches import match_data

##opening log file to log the data
try: 
    log_file = open('log_file.txt', 'a')
except:
    print("Log File cannot be created")

##getting the data from all the lex files and storing that in appropriate lists
matches_details = match_data()
stadium_name, stadium_capacity = venue_details()
team_list = team()
p_AWARDS, p_fair, p_GG_YOUNG, p_PLAYER = award()


##function to print goals forwarded and conceded by a team
def goals_conceded():
    ##using the global matches_details list
    global matches_details
    # matches_details = match_data()
    print()

    ##asking the user for team name whose data is to be shown 
    team_name = input("Enter the team name : ")

    ##declaring variables which store total goals conceded and forwarded respectively
    concede = 0
    forward = 0

    ##declaring variable to see if the name entered by the user is valid or not
    temp = 0
    for i in range(0, len(matches_details[0])):
        if(team_name == matches_details[0][i]):
            temp = 1
            ##goals conceded and forwarded in a home game match
            forward += int(matches_details[2][i][0])
            concede += int(matches_details[2][i][1])
        if(team_name == matches_details[1][i]):
            temp = 1
            ##goals conceded and forwarded in an away game match
            forward += int(matches_details[2][i][1])
            concede += int(matches_details[2][i][0])

    if(temp == 0):
        print("Invalid Team Name")
    else:
        print("Conceded Goals : " + str(concede))
        print("forwarded Goals : " + str(forward))
        ##logging the data to log file
        log_file.write("Goad Forwarded and Conceded by " + str(team_name)  + "  " + str(forward) + " " + str(concede) + "\n")
    print()
    return


##function to print group stage match details
def group_stage(matches_details):
    goals = [0, 1, 3, 7, 9, 12, 14, 20, 22, 24, 24, 26, 27, 30, 30, 32, 34, 36, 39, 39, 43, 44, 46, 47, 48, 51, 57, 58, 60, 63, 68, 68, 69, 71, 75, 75, 78, 79, 80, 86, 87, 92, 93, 93, 98, 101, 102, 103, 106]
    
    ##using while loop so the group stage menu runs indefinetly until user prompts to get out of it
    while(True):
        ##printing the group stage info
        print("################ Gruop Stage Info ###################")
        print("Press A for Group A data")
        print("Press B for Group B data")
        print("Press C for Group C data")
        print("Press D for Group D data")
        print("Press E for Group E data")
        print("Press F for Group F data")
        print("Press G for Group G data")
        print("Press H for Group H data")
        print("Press b to go back to Match Menu")
        print("Press q to go back to Main Menu")

        ##getting the user input
        x = input("Select Option : ")

        ##for group A info
        if x == 'A':
            print()
            print("##### Group A Info #####")
            ##printing the qualified teams from Group A
            print("Qualified Teams from Group A are : Netherlands and Senegal")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i] + " vs " + matches_details[1][i])
            temp = int(input("Select Match : ")) - 1

            ##if user enters invalid match choice
            if(temp > 5):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group B info
        elif x == 'B':
            print()
            print("##### Group B Info #####")
            ##printing the qualified teams from Group B
            print("Qualified Teams from Group B are : England and United States")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+6] + " vs " + matches_details[1][i+6])
            temp = int(input("Select Match : ")) + 5


            ##if user enters invalid match choice
            if(temp > 11):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group C info
        elif x == 'C':
            print()
            print("##### Group C Info #####")
            ##printing the qualified teams from Group C
            print("Qualified Teams from Group C are : Argentina and Poland")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+12] + " vs " + matches_details[1][i+12])
            temp = int(input("Select Match : ")) + 11


            ##if user enters invalid match choice
            if(temp > 17):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group D info
        elif x == 'D':
            print()
            print("##### Group D Info #####")
            ##printing the qualified teams from Group D
            print("Qualified Teams from Group D are : France and Australia")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+18] + " vs " + matches_details[1][i+18])
            temp = int(input("Select Match : ")) + 17


            ##if user enters invalid match choice
            if(temp > 23):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group E info
        elif x == 'E':
            print()
            print("##### Group E Info #####")
            ##printing the qualified teams from Group E
            print("Qualified Teams from Group E are : Japan and Spain")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+24] + " vs " + matches_details[1][i+24])
            temp = int(input("Select Match : ")) + 23


            ##if user enters invalid match choice
            if(temp > 29):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group F info
        elif x == 'F':
            print()
            print("##### Group F Info #####")
            ##printing the qualified teams from Group F
            print("Qualified Teams from Group F are : Morocco and Croatia")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+30] + " vs " + matches_details[1][i+30])
            temp = int(input("Select Match : ")) + 29

            ##if user enters invalid match choice
            if(temp > 35):
                print()
                print("Invalid Match Choice")
                print()
                break


            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group G info
        elif x == 'G':
            print()
            print("##### Group G Info #####")
            ##printing the qualified teams from Group G
            print("Qualified Teams from Group G are : Brazil and Switzerland")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+36] + " vs " + matches_details[1][i+36])
            temp = int(input("Select Match : ")) + 35


            ##if user enters invalid match choice
            if(temp > 41):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##for group H info
        elif x == 'H':
            print()
            print("##### Group H Info #####")
            ##printing the qualified teams from Group H
            print("Qualified Teams from Group H are : Portugal and South Korea")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 6):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+42] + " vs " + matches_details[1][i+42])
            temp = int(input("Select Match : ")) + 41


            ##if user enters invalid match choice
            if(temp > 47):
                print()
                print("Invalid Match Choice")
                print()
                break

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[temp], goals[temp+1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")

        ##if user prompts to go back to "Match Menu"
        elif x == 'b':
            break

        ##if user prompts to go back to "Main Menu"
        elif x == 'q':
            return 1

        ##if user enters some invalid choice
        else:
            print()
            print("Invalid Choice")
            print()
    return

##function to print the knockout match details
def knockout_stage(matches_details):
    goals = [106, 110, 113, 116, 119, 125, 130, 134, 139, 145, 153, 154, 157, 159, 161, 164, 171]
    no_goals_scored = [4, 3, 3, 3, 2, 5, 0, 5, 2, 3, 1, 3, 2, 2, 3, 3]

    ##while loop will run indefinelty until the user prompts to get out of it
    while(True):

        ##printing the knockout stage menu to user
        print("################ Knockout Stage Info ###################")
        print("Press 1 for Round of 16 Info")
        print("Press 2 for Quarter Finals Info")
        print("Press 3 for Semi Finals Info")
        print("Press 4 for Third Place Match Info")
        print("Press 5 for Finals Info")
        print("Press b to go back to Match Menu")
        print("Press q to go back to Main Menu")

        ##taking the user input
        x = input("Select Option : ")

        ##for round of 16 info
        if x == '1':
            print()
            print("##### Round of 16 Info #####")
            ##printing the teams which qualified to Quarterfinals
            print("Qualified Teams from Round of 16 are : Netherlands, Argentina, Croatia, Brazil, England, France, Morocco, Portugal")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 8):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+48] + " vs " + matches_details[1][i+48])
            y = int(input("Select Match : "))
            temp = y + 47 

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[y-1], goals[y-1]+no_goals_scored[y-1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")
            print()

        ##for Quarterfinals info
        elif x == '2':
            print()
            print("##### QuarterFinals Info #####")
            ##printing the teams which qualified to Semifinals
            print("Qualified Teams from QuarterFinals are : Argentina, Croatia, France, Morocco")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 4):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+56] + " vs " + matches_details[1][i+56])
            y = int(input("Select Match : "))
            temp = y + 55
            y += 8

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[y-1], goals[y-1]+no_goals_scored[y-1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")
            print()

        ##for Semifinals info
        elif x == '3':
            print()
            print("##### SemiFinals Info #####")
            ##printing the teams which qualified to Finals
            print("Teams which Reached Finals are : Argentina and France")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 2):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+60] + " vs " + matches_details[1][i+60])
            y = int(input("Select Match : "))
            temp = y + 59
            y += 12

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[y-1], goals[y-1]+no_goals_scored[y-1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")
            print()

        ##for ithird place match info
        elif x == '4':
            print()
            print("##### Third Place Match Info #####")
            ##printing the team which won the third place
            print("Teams which Secured Third Place is : Croatia")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 1):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+62] + " vs " + matches_details[1][i+62])
            y = int(input("Select Match : "))
            temp = y + 61
            y += 14

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[y-1], goals[y-1]+no_goals_scored[y-1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")
            print()

        ##for finals info
        elif x == '5':
            print()
            print("##### Finals Info #####")
            ##printing the teams which won the FIFA World Cup 2022
            print("Fifa World Cup 2022 Winner : Argentina")

            ##Printing match choice to ask user to get which match data
            for i in range(0, 1):
                print("Press " + str(i+1) + " to get details of Match " + matches_details[0][i+63] + " vs " + matches_details[1][i+63])
            y = int(input("Select Match : "))
            temp = y + 62
            y += 15

            ##printing match details
            print(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]))
            print("Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]))
            print("Referee Name : " + str(matches_details[5][temp]))

            ##logging match details to log file
            log_file.write(str(matches_details[0][temp]) + " " + str(matches_details[2][temp][0]) + " : " + str(matches_details[2][temp][1]) + " " + str(matches_details[1][temp]) + "\n")
            log_file.write("    Stadium Name : " + str(matches_details[3][temp]) + "   " + "Attendance : " + str(matches_details[4][temp]) + "\n")
            log_file.write("    Referee Name : " + str(matches_details[5][temp]) + "\n")

            ##printing goal scorers of the match
            print("Goal Scorers : ")
            log_file.write("    Goal Scorers : ")
            for i in range(goals[y-1], goals[y-1]+no_goals_scored[y-1]):
                print(matches_details[6][i])
                
                ##logging goal scorers of the match to log file
                log_file.write(" " + str(matches_details[6][i]))
            log_file.write("\n")
            print()
        
        ##if user prompts to go back to "Match Menu"
        elif x == 'b':
            break

        ##if user prompts to go back to "Main Menu"
        elif x == 'q':
            return 1

        ##if user enters some invalid choice
        else:
            print()
            print("Invalid Choice")
            print()
    return

##function to print all the teams participated in the tournament
def teams():
    ##using the global team_list list
    global team_list
    # team_list = team()
    ##variable to remember the index of team
    i = 1
    print()
    log_file.write("Teams are : \n")
    for x in team_list:
        ##printing the team name
        print(str(i) + ". " + x)
        ##logging team name to log file
        log_file.write("    " + str(i)  + ". " + x + "\n")
        i += 1
    
    print()
    return


##function to print venue details
def venue():
    ##using the global stadium_name and stadium_capacity lists
    global stadium_name
    global stadium_capacity
    # stadium_name, stadium_capacity = venue_details()
    print()
    for i in  range(0, len(stadium_name)):
        ##printing the stadium data
        print("Stadium Name : " +  stadium_name[i] + "       Stadium Capacity :  " + stadium_capacity[i])
        ##logging stadium data to log file
        log_file.write("Stadium Name : " + str(stadium_name[i]) + "  Stadium Capacity : " + str(stadium_capacity[i]) + "\n" )
    print()
    return


##function which fetches and displays the match information
def matches():
    ##using the global matches_details list
    global matches_details
    # matches_details = match_data()

    ##while loop to be in Match Menu indefinetly until user prompts to get out of it
    while(True):

        ##printing the match menu options
        print()
        print("################## Match Menu #################")
        print("Press 1 for Group Stage Data")
        print("Press 2 for Knockout Matches")
        print("Press b to go back to Main Menu")

        ##taking the user choice
        x = input("Select Option : ")


        ##when user prompts to see the group stage match details
        if x == '1':
            ret = group_stage(matches_details)
            ##when user wants to get back to main menu
            if(ret == 1):
                break
        ##when user prompts to see the knockout stage match details
        elif x == '2':
            ret = knockout_stage(matches_details)
            ##when user wants to get back to main menu
            if(ret == 1):
                break
        ##when user wants to go back to main menu
        elif x == 'b':
            break
        ##when user enters any invalid choice
        else:
            print("Invalid Choice")
    matches_details.clear()
    return


## function which fetches and prints the awards won
def awards():
    ## using the global lists
    global p_AWARDS
    global p_fair
    global p_GG_YOUNG
    global p_PLAYER
    # p_AWARDS, p_fair, p_GG_YOUNG, p_PLAYER = award()
    ## while loop to be in Awards Menu indefinetly until user prompts to get out of it
    while(True):

        ## printing awards menu
        print("##############  Awards Menu  ###########")
        print("1. BALL awards")
        print("2. Boot awards")
        print("3. Golden Glove awards")
        print("4. Young awards")
        print("5. Fair awards")
        print("Press b to go back to Main Menu")

        ##taking the user input
        x=input("Select option : ")

        ##printing Ball Awards
        if x=='1':
            print()
            print("BALL awards")
            ##golden ball, silver ball and bronze ball awards
            print(p_AWARDS[2]+" : "+p_PLAYER[2])
            print(p_AWARDS[1]+" : "+p_PLAYER[1])
            print(p_AWARDS[0]+" : "+p_PLAYER[0])
            
            ##printing the ball awards to log file
            log_file.write("Ball Awards : \n" )
            log_file.write("    " + str(p_AWARDS[2]) + " : " + str(p_PLAYER[2]) + "\n")
            log_file.write("    " + str(p_AWARDS[1]) + " : " + str(p_PLAYER[1]) + "\n")
            log_file.write("    " + str(p_AWARDS[0]) + " : " + str(p_PLAYER[0]) + "\n")
            print()
        
        ##printing Boot Awards
        elif x=='2':
            print()
            print("Boot awards")
            ##golden boot, silver boot and bronze boot awards
            print(p_AWARDS[5]+"  :  "+p_PLAYER[5])
            print(p_AWARDS[4]+"  :  "+p_PLAYER[4])
            print(p_AWARDS[3]+"  :  "+p_PLAYER[3])

            ##printing the boot awards to log file
            log_file.write("Boot Awards : \n" )
            log_file.write("    " + str(p_AWARDS[5]) + " : " + str(p_PLAYER[5]) + "\n")
            log_file.write("    " + str(p_AWARDS[4]) + " : " + str(p_PLAYER[4]) + "\n")
            log_file.write("    " + str(p_AWARDS[3]) + " : " + str(p_PLAYER[3]) + "\n")
            print()
        
        ##printing golden glove award
        elif x=='3':
            print()
            print("Golden Golve Award : " + p_GG_YOUNG[0])

            ##printing Golden Glove award to log file
            log_file.write("Golden Glove Award : " + str(p_GG_YOUNG[0]) + "\n")
            print()

        ##printing Emerging player award
        elif x=='4':
            print()
            print("Emerging Young Player Award :  " + p_GG_YOUNG[1])

            ##printing Emerging player award to log file
            log_file.write("Emerging Player Award : " + str(p_GG_YOUNG[1]) + "\n")
            print()

        ##printing Fair Play Award
        elif x=='5':
            print()
            print("Fair PLay Award :  " + p_fair[0])

            ##printing Fair Play award to log file
            log_file.write("Fair Play Award : " + str(p_fair[0]) + "\n")
            print()
        
        ##if user wants to go back to main menu
        elif x == 'b':
            break
        ##if user enters an invalid choice
        else:
            print("Invalid Choice")
    return





def base_function():
    ## while loop to run the main menu indefinetly until user prompts to quit
    while(True):
        print()
        ##printing the main menu options
        print("####################    MAIN MENU    ####################")
        print("Press 1 for All teams participated in the tournament")
        print("Press 2 for Venue Details")
        print("Press 3 for Match Details")
        print("press 4 for Awards")
        print("Press 5 to find Goals conceded and forwarded by a team")
        print("Press q to exit the menu")

        ##taking the user choice of options
        choice = input("Enter your choice : ")

        ##calling various functions using if else for handling each of the details
        if(choice == '1'):
            teams()
        elif(choice == '2'):
            venue()
        elif(choice == '3'):
            matches()
        elif(choice == '4'):
            awards()
        elif(choice == '5'):
            goals_conceded()
        ## when user prompts to quit the main menu
        elif(choice == 'q'):
            print("Thank you!")
            break
        ## when user gives any invalid argument
        else:
            print("Invalid choice")

    return
        


#########Calling the base function which runs the main menu
base_function() 