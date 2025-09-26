import json;
import random;
import subprocess;

'''print("stdout:", questions.stdout)
print("stderr:", questions.stderr)
print("returncode:", questions.returncode)'''
topics_values = {
    "General Knowledge": "9",
    "Entertainment: Books": "10",
    "Entertainment: Film": "11",
    "Entertainment: Music": "12",
    "Entertainment: Musicals & Theatres": "13",
    "Entertainment: Television": "14",
    "Entertainment: Video Games": "15",
    "Entertainment: Board Games": "16",
    "Science & Nature": "17",
    "Science: Computers": "18",
    "Science: Mathematics": "19",
    "Mythology": "20",
    "Sports": "21",
    "Geography": "22",
    "History": "23",
    "Politics": "24",
    "Art": "25",
    "Celebrities": "26",
    "Animals": "27",
    "Vehicles": "28",
    "Entertainment: Comics": "29",
    "Science: Gadgets": "30",
    "Entertainment: Japanese Anime & Manga": "31",
    "Entertainment: Cartoon & Animations": "32"
}


topics_serailNum = {
    1: "General Knowledge",
    2: "Science & Nature",
    3: "Science: Computers",
    4: "Science: Mathematics",
    5: "Entertainment: Cartoon & Animations"
}

questions = None;
def validate_int(prompt=None)->int:
    'validates for number'
    while True:
           try: 
                n = int (input(prompt))
                if(n>=1 and n<=5):
                    return n
           except ValueError:
                print("\033[31mPlease enter an number!\033[0m")

def askTopicToQuestions():
    global questions;
    print("\033[34m---Choose a topic for quiz(enter number)---\033[0m" )
    for i, topic in topics_serailNum.items():
        print(f"{i}. {topic}")
    topicSrNum = validate_int("Enter serial number(1-5): ")
    questions = subprocess.run(
        ["node", 'script.js'],
        input = topics_values[topics_serailNum[topicSrNum]],
        capture_output=True, text=True).stdout
    # print(questions)
    questions = json.loads(questions); #converting json stings into json
# askTopicToQuestions();
#api data formate: {"response_code": val, "results": [{}, {},.....]}
#user data formate: {"highest_score": int, "correct_ans": int, "total_ques": int}
# username= None
def save_data(db):
    with open(f'{username}.json', 'w') as file:
        json.dump(db, file, indent=2)
"""\033[ starts the escape sequence.
31m, 32m, etc., specify the color.
\033[0m resets the color back to default.
30: Black
31: Red
32: Green
33: Yellow
34: Blue
35: Magenta
36: Cyan
37: White"""
def load_db():
    'returns db of user; if not present, it creates a new one with default values and greets the new user'
    # print(F"UERNAME: {username}")
    try:
        with open(f'{username}.json', "r") as file:
            # return json.load(f'{username}.json')
            return json.load(file)
    except FileNotFoundError:
        print(f"\033[32m{username}\033[0m,Best of Luck for your first game!")
        print("\033[36mNew database created for you!\033[0m")
        newDB = { "highest_score":0, "correct_ans": 0, "total_ques":0 };
        save_data(newDB);
        return newDB
def signinORsignup():
    "welcomes user and signs in or up and If user is not new one, it greets and creates database(if not already)"
    global username; # to declare a variable within a function as global variable
    print("Welcome! Please sign in or sign up.")
    username = input("Enter your username: ").strip().title()
    user_db = load_db()
    if(user_db["total_ques"]):
        print(f"Nice to see you again \033[32m{username}!\033[0m")

import urllib.parse;
def logOptions(correct, inc_list):
    'log options and returns the correct ans identifier (chr)'
    cor_ind = random.randint(0,3)
    op = 97;
    for i in range(3): #it will only pirnt if 0<= cor_ind <=2
        if(cor_ind == i ):
            print(f'({chr(op)})',urllib.parse.unquote(correct).replace("&quot;","\""))
            op += 1
        print(f'({chr(op)})',urllib.parse.unquote(inc_list[i]))
        op += 1
    # for cor_ind ==3
    if( cor_ind ==3):
        print(f'({chr(op)})',correct)
    return chr(97+cor_ind);

#user data formate: {"highest_score": int, "correct_ans": int, "total_ques": int}

# asking questions and saving them in the database of the current user
def quiz():
    """Taking quiz; asking questions and saving progress..."""
    user_db = load_db()
    correct_ans = 0;
    #questions_asked += 5
    score = 0;
    askTopicToQuestions();
    if(questions["response_code"] != 0):
        print(f"\033[31m{questions['ERROR']}\033[0m")
        return;
    # questions = personalise_quiz(); # functions return a generator object, genetates question
    for ques in questions["results"]:
        print(F"\nQues: {urllib.parse.unquote(ques['question'])}")
        correct_op = logOptions(ques["correct_answer"],ques["incorrect_answers"])
        user_ans = input("Correct option is?: ")
        # ques['user_ans'] = user_ans
        # user_db["questionsAsked"].append(ques);
        if( user_ans == correct_op):
            score += 1
            correct_ans += 1
            print("\033[32mCorrect answer!\033[0m")
        else:
            print(f"\033[31mWrong!\033[0m The correct answer was {urllib.parse.unquote(ques['correct_answer'])}.")
    print(f"\nYour score is: {score}")

    user_db["total_ques"] += 5
    user_db['correct_ans'] += correct_ans
    if(score > user_db['highest_score']):
        print("\033[35mWooaa...You set new Highest Score!\033[0m")
        user_db['highest_score'] = score;
    # updating the user database
    save_data(user_db);
    return 1

#driver code


signinORsignup();
isSuccessful = quiz();#If quiz executes successfully it will return one else none
if isSuccessful:
    ch = input("---Want to see your stats(y or n)??: ")
    if ch == "y":
        userDB = load_db()
        print(f"\nHighest score: \033[33m{userDB['highest_score']}\033[0m")            
        print(f"Total questions asked: \033[33m{userDB['total_ques']}\033[0m")
        print(f"Correct answers: \033[33m{userDB['correct_ans']}\033[0m")
        acc = round(userDB['correct_ans']/userDB['total_ques']*100)
        print(f"Accuracy: \033[33m{acc}%\033[0m")

