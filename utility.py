import pyodbc
from color import style
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BELLY;'
                      'Database=belay.oop;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT equastion from belly')
answer = []
class sql():
    def __init__(self):
        self.answer = []
        self.score = 0
    def con(self):
        self.ur_an = []
        for row in cursor:
            print(style.BOLD + style.RED + "\t\t\tWELCOME TO QUIZ GAME")
            while True:
                re = input(style.MAGENTA + "#_Are you ready to play? yes/no")
                if re=='yes':
                    name = input("enter your name")
                    Id = input("enter your Id")
                    cat = input("enter catagory")
                    if cat=='1':
                        ur_an = []
                        cursor.execute('SELECT equastion    from belly where catagory = 1')
                        row = cursor.fetchall()
                        for equastion in row:
                            print(style.YELLOW + f'{equastion}')
                            ans = input("please enter your answer")
                            ur_an.append(ans)
                        print(style.RESET+"your name is:" + style.MAGENTA + f'{name}', "and", "your Id is:" + style.MAGENTA + f'{Id}')
                        print("your answer are:" + style.MAGENTA + f'{ur_an}')
                        print(style.CYAN + "The correct as are---------------------")
                        cursor.execute('SELECT answer  from belly where catagory = 1')
                        for answer in cursor:
                            row_to_list = list(answer)
                            print(row_to_list)
                    elif cat=='2':
                        ur_an = []
                        cursor.execute('SELECT equastion, opetion from belly where catagory = 2')
                        row = cursor.fetchall()
                        for equastion in row:
                            print(style.YELLOW + f'{equastion}')
                            ans = input("please enter your answer")
                            ur_an.append(ans)
                        print("your name is:" + style.MAGENTA + f'{name}' "and", "your Id is:" + style.MAGENTA + f'{Id}')
                        print("your answer are:" + style.MAGENTA + f'{ur_an}')
                        print(style.CYAN + "The correct as are---------------------")
                        cursor.execute('SELECT answer from belly where catagory = 2')
                        for answer in cursor:
                            row_to_list = list(answer)
                            print(style.MAGENTA + f'{row_to_list}')
                    elif cat=='3':
                        ur_an = []
                        cursor.execute('SELECT equastion, opetion from belly where catagory = 3')
                        row = cursor.fetchall()
                        for equastion in row:
                            print(style.BLUE + f'{equastion}')
                            ans = input("please enter your answer")
                            ur_an.append(ans)
                        print("your name is:" + style.MAGENTA + f'{name}' "and", "your Id is:" + style.MAGENTA + f'{Id}')
                        print("your answer are:" + style.MAGENTA + f'{ur_an}')
                        print(style.CYAN + "The correct as are---------------------")
                        cursor.execute('SELECT answer from belly where catagory = 3')
                        for answer in cursor:
                            row_to_list = list(answer)
                            print(style.MAGENTA + f'{row_to_list}')

                    else:
                        print("please select catagory from (1, 2, 3)")

                    print("Thank you")
                else:
                    break