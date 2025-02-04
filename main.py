from plyer import notification
import threading
import time
from flask import Flask, render_template, request
import my_functions
from colorama import Fore, Back, Style
import datetime

time_per = str()
app = Flask(__name__)

print(Fore.GREEN + 'Loading...')
print(Style.RESET_ALL)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recreation')
def recreation():
    my_fact = my_functions.get_fact()
    my_quote = my_functions.get_qoute()[0]
    author = my_functions.get_qoute()[1]
    link = my_functions.get_youtube_vid()
    hack = my_functions.get_study_hack()
    return render_template('recreation.html', fact = my_fact, quote = my_quote, source = link, hack = hack)

@app.route('/reminders', methods = ['POST', 'GET'])
def reminders():
    if request.method == "POST":
        # Get
        water = request.form.get('water')
        meditation = request.form.get('meditation')
        exercise = request.form.get('exercise')
        rest = request.form.get('rest')
        entertain = request.form.get('entertain')
        # Set
        my_functions.set_reminder('water', water)
        my_functions.set_reminder('meditate', meditation)
        my_functions.set_reminder('exercise', exercise)
        my_functions.set_reminder('rest', rest)
        my_functions.set_reminder('entertain', entertain)
    return render_template('reminders.html')

@app.route('/timetable', methods=['POST', 'GET'])
def timetable():
    if request.method == 'POST':
        task = request.form.get('name')
        link = request.form.get('link')
        time_per = request.form.get('curr_row')
        if task == "":
            task == "nan"
        if link == "":
            link = "nan"
        my_functions.set_time_table(time_per, task, link)
        array = my_functions.check_time_table()
        for i in range(len(array)):
            slot = array[i][0]
            if slot == '9-10':
                task1 = array[i][1]
                link1 = array[i][2]
            elif slot == '10-11':
                task2 = array[i][1]
                link2 = array[i][2]
            elif slot == '11-12':
                task3 = array[i][1]
                link3 = array[i][2]
            elif slot == '12-13':
                task4 = array[i][1]
                link4 = array[i][2]
            elif slot == '13-14':
                task5 = array[i][1]
                link5 = array[i][2]
            elif slot == '14-15':
                task6 = array[i][1]
                link6 = array[i][2]
            elif slot == '15-16':
                task7 = array[i][1]
                link7 = array[i][2]
            elif slot == '16-17':
                task8 = array[i][1]
                link8 = array[i][2]
            elif slot == '17-18':
                task9 = array[i][1]
                link9 = array[i][2]
            elif slot == '18-19':
                task10 = array[i][1]
                link10 = array[i][2]
            elif slot == '19-20':
                task11 = array[i][1]
                link11 = array[i][2]
            elif slot == '20-21':
                task12 = array[i][1]
                link12 = array[i][2]
        task_list = {
            "task1": task1,
            "task2": task2,
            "task3": task3,
            "task4": task4,
            "task5": task5,
            "task6": task6,
            "task7": task7,
            "task8": task8,
            "task9": task9,
            "task10": task10,
            "task11": task11,
            "task12": task12,
            "link1": link1,
            "link2": link2,
            "link3": link3,
            "link4": link4,
            "link5": link5,
            "link6": link6,
            "link7": link7,
            "link8": link8,
            "link9": link9,
            "link10": link10,
            "link11": link11,
            "link12": link12}
        for j in range(1,13):
            if str(task_list["task"+str(j)])=="nan":
                task_list["task"+str(j)] = ""
            if str(task_list["link"+str(j)])=="nan":
                task_list["link"+str(j)] = ""
        return render_template('timetable.html', **task_list)
    
    # Normal
    array = my_functions.check_time_table()
    for i in range(len(array)):
        slot = array[i][0]
        if slot == '9-10':
            task1 = array[i][1]
            link1 = array[i][2]
        elif slot == '10-11':
            task2 = array[i][1]
            link2 = array[i][2]
        elif slot == '11-12':
            task3 = array[i][1]
            link3 = array[i][2]
        elif slot == '12-13':
            task4 = array[i][1]
            link4 = array[i][2]
        elif slot == '13-14':
            task5 = array[i][1]
            link5 = array[i][2]
        elif slot == '14-15':
            task6 = array[i][1]
            link6 = array[i][2]
        elif slot == '15-16':
            task7 = array[i][1]
            link7 = array[i][2]
        elif slot == '16-17':
            task8 = array[i][1]
            link8 = array[i][2]
        elif slot == '17-18':
            task9 = array[i][1]
            link9 = array[i][2]
        elif slot == '18-19':
            task10 = array[i][1]
            link10 = array[i][2]
        elif slot == '19-20':
            task11 = array[i][1]
            link11 = array[i][2]
        elif slot == '20-21':
            task12 = array[i][1]
            link12 = array[i][2]
    task_list = {
        "task1": task1,
        "task2": task2,
        "task3": task3,
        "task4": task4,
        "task5": task5,
        "task6": task6,
        "task7": task7,
        "task8": task8,
        "task9": task9,
        "task10": task10,
        "task11": task11,
        "task12": task12,
        "link1": link1,
        "link2": link2,
        "link3": link3,
        "link4": link4,
        "link5": link5,
        "link6": link6,
        "link7": link7,
        "link8": link8,
        "link9": link9,
        "link10": link10,
        "link11": link11,
        "link12": link12}
    for j in range(1,13):
            if str(task_list["task"+str(j)])=="nan":
                task_list["task"+str(j)] = ""
            if str(task_list["link"+str(j)])=="nan":
                task_list["link"+str(j)] = ""
    return render_template('timetable.html', **task_list)

def alert():
    while True:
        current_time = datetime.datetime.now()
        if current_time.second == 0:
            while True:
                curr_time = datetime.datetime.now()
                water = str(my_functions.reminder_check('water'))
                meditate = str(my_functions.reminder_check('meditate'))
                exercise= str(my_functions.reminder_check('exercise'))
                rest = str(my_functions.reminder_check('rest'))
                entertain = str(my_functions.reminder_check('entertain'))
                if water == "True":
                    if curr_time.minute == 31:
                        print("water alert")
                        title = 'Pani peelo friends 😂'
                        message= 'Drink Water reminder by Time.It'
                        notification.notify(title= title,message= message,app_icon = None,timeout= 5,toast=False)
                        time.sleep(30)
                elif meditate == "True":
                    if curr_time.hour == 8 and curr_time.minute == 0 or curr_time.hour == 18 and curr_time.minute == 0:
                        print("meditate alert")
                        title = 'Meditate to relax your soul!'
                        message= 'Meditation reminder by Time.It'
                        notification.notify(title= title,message= message,app_icon = None,timeout= 5,toast=False)
                        time.sleep(30)
                elif exercise == "True":
                    if curr_time.hour == 9 or curr_time.hour and curr_time.minute == 0 or curr_time.hour == 19:
                        print("exercise alert")
                        title = 'Sometimes a workout is the only therapy you need!'
                        message= 'Exercise reminder by Time.It'
                        notification.notify(title= title,message= message,app_icon = None,timeout= 5,toast=False)
                        time.sleep(30)
                elif rest == "True":
                    if curr_time.hour % 4 == 0 and curr_time.minute == 0 and 8 <= curr_time.hour <= 20:
                        print("relax alert")
                        title = 'Take a 5 min break to boost your productivity!'
                        message= 'Relax reminder by Time.It'
                        notification.notify(title= title,message= message,app_icon = None,timeout= 5,toast=False)
                        time.sleep(30)
                elif entertain == "True":
                    if curr_time.hour % 3 == 0 and curr_time.minute == 0 and 9 <= curr_time.hour <= 21:
                        print("entertainment alert")
                        title = 'Did you watch the stand up of the day on the Time.It site?'
                        message= 'Entertainment reminder by Time.It'
                        notification.notify(title= title,message= message,app_icon = None,timeout= 5,toast=False)
                        time.sleep(30)
                time.sleep(30)

thread = threading.Thread(target=alert)
thread.start()
app.run(debug=True, port='5000')