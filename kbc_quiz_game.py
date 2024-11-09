import time

print("KAUN BANEGA CROREPATI MEIN AAPKA SWAGAT HAI ")

questions= [
    "Which team won the 1983 Cricket World Cup?" ,
    "Who won the Man of the Tournament award in the 2016 T20 World Cup?" ,
    "Which team won the 2003 Cricket World Cup?" ,
    "Who won the Man of the Tournament award in the 2022 Cricket World Cup?" ,
    "Who holds the record for the most sixes in T20 internationals?"
    ] 

options= [
    ["AUS", "IND", "WI", "SL"], ["Samuels", "Malinga", "Kohli", "Braithwait"], ["Eng", "Pak", "Ind", "Aus"], ["Kohli", "Babar", "Curran", "Buttler"], [ "Rohit", "Morgan", "SKY", "Maxwell"]
    ]

answers= ["B", "C", "D", "C", "A"]

levels= [100000, 200000, 300000, 400000, 500000]
money=0

def ask_question(i):
    print(f"\nQuestion {i+1} for Rs.{levels[i]}:")
    print(f"{questions[i]}")
    time.sleep(3)
    print(f"A: {options[i][0]}    B: {options[i][1]}")
    print(f"C: {options[i][2]}    D: {options[i][3]}")

def get_user_answer():
    while True:
        user_answer = input("Choose Option A, B, C, or D: ").upper()
        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        else:
            print("Invalid option, please choose A, B, C, or D.")

for i in range(len(questions)):
    ask_question(i)
    user_answer = get_user_answer()

    if user_answer == answers[i]:
        money += levels[i]
        print(f"Correct! You have won Rs.{levels[i]}")
        print(f"Total winnings: Rs.{money}\n")
    else:
        print("Wrong answer... Your journey ends here.")
        break

print(f"Thank you for playing! Your total prize is Rs.{money}")
