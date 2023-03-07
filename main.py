import time as tm
import datetime
import os
class PlayerDiv():
    def __init__(self):
        print("Welcome to TBF player control panel")
        time_is_now = datetime.datetime.now()
        date = datetime.datetime.strftime(time_is_now, '%c')
        print("System opened:"+ date)
        print("-------------------------------")

    def add_player(self):
        time_is_now = datetime.datetime.now()
        date = datetime.datetime.strftime(time_is_now, '%c')
        valid_database_check = input("Please choose active database:")
        print("Please enter needless informations")
        player_name = input("Please enter player's name:")
        player_no = input("Please enter player's number:")
        player_team = input("Please enter player's team:")
        with open(valid_database_check,"a",encoding="utf-8") as file0:
            file0.write("Player's name:"+player_name+"\n"+"Player's team:"+player_team+"\n"+
                        "Player's no:"+player_no+"\n"+"Attend Date:"+date+"\n"+"--------------------------------\n")
            print("Progress worked")

    def delete_database(self):
        try:
            file_name = input("Please choose delete file:")
            tm.sleep(2)
            os.remove(file_name)
            print(file_name, "Deleted")
        except:
            print("System: an unexpected error was encountered")

    def read_file(self):
        with open("Players.txt","r",encoding="utf-8") as file0:
            players = file0.read()
            print(players)

    def create_new_databse(self):
        new_database_name = input("Please enter new database's name:")
        with open(new_database_name,"w") as file:
            print("New Database object created")

    def show_all_active_database(self):
        folder_path = 'D:\Pycharm-projects\\NBADiv'
        total_txt_files = 0

        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                total_txt_files += 1
        print("Total Database number :",total_txt_files)

        txt_files = []

        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                txt_files.append(filename)

        print("Active Databases:")
        for file in txt_files:
            print("-"+file)


Panel = PlayerDiv()

while True:
    progress = input("""
1-Create a new Database(.txt)
2-Add new player
3-Delete database
4-Read Database
5-Show Databases
Q-Quit
Choose progress:
    """)
    if(progress == "Q"):
        break
    if(progress == "1"):
        Panel.create_new_databse()
        break
    elif(progress == "2"):
        Panel.add_player()
    elif(progress == "3"):
        Panel.delete_database()
    elif(progress == "4"):
        Panel.read_file()
    elif(progress == "5"):
        Panel.show_all_active_database()
