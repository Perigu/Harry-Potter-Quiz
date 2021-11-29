from tkinter import *
import random, pygame

def file(z, new_question = 0, old = 1):
    file = open('Q&A.txt', 'r')
    read = file.read()
    lines = read.splitlines()
    list = [x.split('||') for x in lines]
    file.close()

    if z == 'r':
        file.close()
        return list
    elif z == 'a':
        file = open('Q&A.txt', 'a')
        if len(list) != 0:
            file.write('\n')
        file.write('||'.join(new_question))
        file.close()
    elif z == 'e':
        file = open('Q&A.txt', 'w')
        list[old] = new_question
        for x in range(0, len(list)):
            if x > 0 and x < len(list):
                file.write('\n')
            file.write('||'.join(list[x]))
        file.close()
    elif z == 'd':
        file = open('Q&A.txt', 'r')
        read = file.read()
        lines = read.splitlines()
        lines[old] = '\n'
        file.close()
        file = open('Q&A.txt', 'w')
        for x in lines:
            if x != '\n':
                if lines.index(x) != 0:
                    file.write('\n')
                file.write(x)
        file.close()

def clear():
    for x in window.winfo_children():
        x.destroy()

def mainmenu():
    global mus
    clear()
    title = Label(window, text = 'Harry Potter Quiz!!!', font = ('Aerial 15 bold'))
    title.grid(column = 0, row = 0, padx = 145, pady = (60,35))
    pb = Button(window, text = 'Play', font =  ('Aerial 10'), command = play_menu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    pb.grid(column = 0, row = 1, pady = 15)
    eb = Button(window, text = 'Edit Quiz', font = ('Aerial 10'), command = edit_menu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    eb.grid(column = 0, row = 2, pady = 15)
    sb = Button(window, text = 'Scoreboard', font = ('Aerial 10'), command = scbd, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    sb.grid(column = 0, row = 3, pady = 15)
    hb = Button(window, text = 'Help', font = ('Aerial 10'), command = lambda: help('h'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    hb.grid(column = 0, row = 4, pady = 15)
    exit = Button(window, text = 'Exit', font = ('Aerial 10'), command = window.destroy, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    exit.grid(column = 0, row = 5, pady = 15)
    mus = Button(window, text = '🔉', font = ('Aerial 15'), command = music, height = 1, width = 2, bd = 4, bg = 'grey85', activebackground = 'grey75')
    mus.grid(column = 0, row = 6, pady = (35,0))
    credits = Label(window, text='Developed by:\nIgor Sobreira', font = ('Aerial 10 bold'))
    credits.grid(column = 0, row = 7, pady =30)

def play_menu():
    clear()
    tip = Label(window, text = 'Try and answer all ten questions correctly. Easy questions are worth 40 points, Normal are worth 60 and Hard ones, 100!!!', font = ('Aerial 12 italic'), wraplength = 300)
    tip.grid(column = 0, row = 0, padx = 92, pady = 40)
    title = Label(window, text = 'Enter your name', font = ('Aerial 15 bold'))
    title.grid(column = 0, row = 1, pady = 30)
    text = Text(bg = 'grey80', bd = 3, height = 1, width = 20)
    text.grid(column = 0, row = 2)
    error = Label(font = ('Aerial 12 italic'), fg = 'red')
    error.grid(column = 0, row = 3)

    begin = Button(window, text = 'Begin!', font = ('Aerial 10'), command = lambda: ready_check(text.get(1.0, END)), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    begin.grid(column = 0, row = 4, pady = (40,20))
    back = Button(window, text = 'Back', font = ('Aerial 10'), command = mainmenu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 5, pady = 100)

def ready_check(player):
    player = player.strip()
    list = file('r')

    error = Label(font = ('Aerial 12 italic'), fg = 'red')
    error.grid(column = 0, row = 3)
    if len(player) == 0:
        error.config(text = 'Error: No name')
    elif len(list) < 10:
        clear()
        title = Label(text = "There aren't enough questions... :(\nAdd some more!", font = ('Aerial 15 bold'))
        title.grid(column = 0, row = 0, padx = 80, pady = 180)
        button = Button(text = 'Add more', command = add_difficulty, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        button.grid(column = 0, row = 1)
    else:
        game(player, randomize())

def randomize():
    list = file('r')
    random_questions = random.sample(range(0, len(list)), 10)
    questions = []
    for x in range(0, 10):
        z = list[random_questions[x]]
        questions.append(z)
    return questions

def game(player, questions, score = 0, points = 0, summary = [], got = 0):
    score += points
    if questions[0][1] == 'H':
        level = 'Hard'
        points = 100
        summary.append('h')
    elif questions[0][1] == 'N':
        level = 'Normal'
        points = 60
        summary.append('n')
    elif questions[0][1] == 'E':
        level = 'Easy'
        points = 40
        summary.append('e')

    question = (questions[0][0][:127] + '...') if len(questions[0][0]) > 127 else questions[0][0]
    player = (player[:17] + '...') if len(player) > 17 else player
    answers = []
    for x in range(1,6):
        a = 'a' + str(x)
        a = (questions[0][x + 1][:43] + '...') if len(questions[0][x + 1]) > 43 else questions[0][x + 1]
        answers.append(str(a))
    c = answers[0]
    r_answers = random.sample(answers, len(answers))

    clear()
    l = Label(text = level, font = ('Aerial 10 italic'))
    l.grid(column = 0, row = 0, pady = (25,15))
    q = Label(text = question, font = ('Aerial 12 bold'), wraplength = 300)
    q.grid(column = 0, row = 1, pady = (0, 10))
    name = Label(text = player, font = ('Aerial 12'))
    name.grid(column = 0, row = 7, pady = 15)
    
    for x in range(1,6):
        o = 'o' + str(x)
        o = Button(text = r_answers[x - 1], font = ('Aerial 12'), wraplength = 390, height = 2, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75')
        o.grid(column = 0, row = x + 1, padx = 82, pady = 14)
        
        if len(questions) == 1:
                if o['text'] == c:
                    o.config(command = lambda: game_end(player, score, points, summary, (got + 1)))
                else:
                    o.config(command = lambda: game_end(player, score, 0, summary, got))
        else:
                if o['text'] == c:
                    o.config(command = lambda: game(player, questions, score, points, summary, (got + 1)))
                else:
                    o.config(command = lambda: game(player, questions, score, 0, summary, got))
                    
    questions.pop(0)

def game_end(player, score, points, summary, got = 0):
    score += points
    scbd_add(player, score, got)
    summ = 'You were given ' + str(summary.count('h')) + ' Hard, ' + str(summary.count('n')) + ' Normal and ' + str(summary.count('e')) + ' Easy questions.' 
    summary.clear()
    score = 'Score: ' + str(score)
    grade = 'You got ' + str(got) + ' out of 10!'
    
    clear()
    title = Label(text = 'The end', font = ('Aerial 16 bold'))
    title.grid(column = 0, row = 0, padx = 195, pady = (140,20))
    sum = Label(text = summ, font = ('Aerial 11 italic'))
    sum.grid(column = 0, row = 1, pady = 10)
    scr = Label(text = score, font = ('Aerial 15'))
    scr.grid(column = 0, row = 2, pady = 10)
    grd = Label(text = grade, font = ('Aerial 13'))
    grd.grid(column = 0, row = 3, pady = (10))
    score = Button(window, text = 'Scoreboard', font = ('Aerial 10'), command = scbd, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    score.grid(column = 0, row = 4, pady = (30,90))
    back = Button(window, text = 'Return', font = ('Aerial 10'), command = mainmenu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 5)

def edit_menu():
    clear()
    edit = Button(window, text = 'Edit a question', font = ('Aerial 10'), command = lambda: question_list(0, 'edit'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    edit.grid(column = 0, row = 0, padx = 174, pady = (160, 20))
    add = Button(window, text = 'Add a question', font = ('Aerial 10'), command = add_difficulty, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    add.grid(column = 0, row = 1, padx = 170, pady = 20)
    delete = Button(window, text = 'Remove a question', font = ('Aerial 10'), command = lambda: question_list(0, 'remove'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    delete.grid(column = 0, row = 2, padx = 170, pady = 20)
    back = Button(window, text = 'Back', font = ('Aerial 10'), command = mainmenu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 3, padx = 170, pady = 60)

def question_list(p, mode):
    list = file('r')
    page_number = p
    T = 'Total: ' + str(len(list))
    question_number = [(x + page_number * 5) for x in range (0, 5)] 

    clear()
    title = Label(window, text = 'Select a question', font = ('Aerial 15 bold'))
    title.grid(column = 1, row = 0, pady = (30,0))
    total = Label(window, text = T, font = ('Aerial 12 bold'))
    total.grid(column = 1, row = 1, pady = (0,20))
    q1 = Button(window, text = get_name(question_number[0])[:80], font = ('Aerial 10'), height = 3, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75', wraplength = 280)
    q1.grid(column = 1, row = 2, pady = 10)
    if get_name(question_number[0]) != '':
        if mode == 'edit':
            q1.config(command = lambda: edit_question(question_number[0]))
        else:
            q1.config(command = lambda: remove_question(question_number[0]))
    q2 = Button(window, text = get_name(question_number[1])[:80], font = ('Aerial 10'), height = 3, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75', wraplength = 280)
    q2.grid(column = 1, row = 3, pady = 10)
    if get_name(question_number[1]) != '':
        if mode == 'edit':
            q2.config(command = lambda: edit_question(question_number[1]))
        else:
            q2.config(command = lambda: remove_question(question_number[1]))
    q3 = Button(window, text = get_name(question_number[2])[:80], font = ('Aerial 10'), height = 3, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75', wraplength = 280)
    q3.grid(column = 1, row = 4, pady = 10)
    if get_name(question_number[2]) != '':
        if mode == 'edit':
            q3.config(command = lambda: edit_question(question_number[2]))
        else:
            q3.config(command = lambda: remove_question(question_number[2]))
    q4 = Button(window, text = get_name(question_number[3])[:80], font = ('Aerial 10'), height = 3, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75', wraplength = 280)
    q4.grid(column = 1, row = 5, pady = 10)
    if get_name(question_number[3]) != '':
        if mode == 'edit':
            q4.config(command = lambda: edit_question(question_number[3]))
        else:
            q4.config(command = lambda: remove_question(question_number[3]))
    q5 = Button(window, text = get_name(question_number[4])[:80], font = ('Aerial 10'), height = 3, width = 35, bd = 4, bg = 'grey85', activebackground = 'grey75', wraplength = 280)
    q5.grid(column = 1, row = 6, pady = 10)
    if get_name(question_number[4]) != '':
        if mode == 'edit':
            q5.config(command = lambda: edit_question(question_number[4]))
        else:
            q5.config(command = lambda: remove_question(question_number[4]))

    back = Button(window, text = 'Back', font = ('Aerial 10'), command = edit_menu, height = 1, width = 10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 7, padx = (8,0), pady = 30)
    if p > 0:
        back.config(command = lambda: question_list(p-1, mode))
    if get_name(question_number[4] + 1) != '':
        next = Button(window, text = 'Next', font = ('Aerial 10'), command = lambda: question_list(p+1, mode), height = 1, width = 10, bd = 4, bg = 'grey85', activebackground = 'grey75')
        next.grid(column = 2, row = 7, padx = (0,10), pady = 30)

def get_name(name):
    list = file('r')
    try:
        question_name = list[name][0]
    except IndexError:
        question_name = ''
    return question_name

def edit_question(question):
    list = file('r')
    clear()
    title = Label(window, text = 'Editing', font = ('Aerial 15 bold'))
    title.grid(column = 1, row = 0, pady = (25,10))
    label1 = Label(window, text = 'Correct Answer', font = ('Aerial 10 bold'))
    label1.grid(column = 0, row = 2, padx = 0)
    label2 = Label(window, text = 'Answer nº 2.', font = ('Aerial 10'))
    label2.grid(column = 0, row = 3, padx = (15,0))
    label3 = Label(window, text = 'Answer nº 3.', font = ('Aerial 10'))
    label3.grid(column = 0, row = 4, padx = (15,0))
    label4 = Label(window, text = 'Answer nº 4.', font = ('Aerial 10'))
    label4.grid(column = 0, row = 5, padx = (15,0))
    label5 = Label(window, text = 'Answer nº 5.', font = ('Aerial 10'))
    label5.grid(column = 0, row = 6, padx = (15,0))
    label6 = Label(window, text = 'Difficulty', font = ('Aerial 10'))
    label6.grid(column = 1, row = 7, padx = (0, 150))

    text0 = Text(window, bg = 'grey80', bd = 3, height = 4, width = 35)
    text0.grid(column = 1, row = 1, pady = (15,10))
    text0.insert(INSERT, list[question][0])
    text1 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text1.grid(column = 1, row = 2, pady = 14)
    text1.insert(INSERT, list[question][2])
    text2 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text2.grid(column = 1, row = 3, pady = 14)
    text2.insert(INSERT, list[question][3])
    text3 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text3.grid(column = 1, row = 4, pady = 14)
    text3.insert(INSERT, list[question][4])
    text4 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text4.grid(column = 1, row = 5, pady = 14)
    text4.insert(INSERT, list[question][5])
    text5 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text5.grid(column = 1, row = 6, pady = 14)
    text5.insert(INSERT, list[question][6])

    text6 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 8)
    text6.grid(column = 1, row = 7, pady = (5,10))
    text6.insert(INSERT, list[question][1])

    back = Button(window, text = 'Back', font = ('Aerial 10'), command = lambda: question_list(0, 'edit'), height = 1, width =10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 8, padx = (10,0))
    save = Button(window, text = 'Save', font = ('Aerial 10'), command = lambda: edit_end(text0.get(1.0,END), text6.get(1.0,END), text1.get(1.0,END), text2.get(1.0,END), text3.get(1.0,END), text4.get(1.0,END), text5.get(1.0,END), question), height = 1, width =10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    save.grid(column = 2, row = 8, padx = (0,10))

def edit_end(q,d,a1,a2,a3,a4,a5, old):
    q = " ".join(q.splitlines())
    d = d.upper()
    new_question = [q,d,a1,a2,a3,a4,a5]
    new_question = [str(x).rstrip() for x in new_question]

    if new_question[1] == 'HARD' or new_question[1] == 'H':
        new_question[1] = 'H'
    elif new_question[1] == 'NORMAL' or new_question[1] == 'N':
        new_question[1] = 'N'
    elif new_question[1] == 'EASY' or new_question[1] == 'E':
        new_question[1] = 'E'
    else:
        new_question[1] = 'Z'

    error = Label(window, font = ('Aerial 12 italic'), fg = 'red')
    error.grid(column = 1, row = 8)
    if len(new_question[0]) == 0:
        error.config(text = 'Error: No question')
    elif len(new_question[1]) == 0 or len(new_question[2]) == 0 or len(new_question[3]) == 0 or len(new_question[4]) == 0 or len(new_question[5]) == 0:
        error.config(text = 'Error: Empty answers')
    elif len(new_question[6]) == 0:
        error.config(text = 'Error: No difficulty')
    elif new_question[1] != 'H' and new_question[1] != 'E' and new_question[1] != 'N':
        print(new_question[1])
        error.config(text = 'Error: Invalid difficuty')
    else:
        file('e', new_question, old)
        clear()
        title = Label(window, text = 'Changes saved!', font = ('Aerial 15 bold'))
        title.grid(column = 0, row = 0, padx = 160, pady = 180)
        back = Button(window, text = 'Return', font = ('Aerial 10'), command = lambda: edit_menu(), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        back.grid(column = 0, row = 1)

def add_difficulty():
    clear()
    title = Label(window, text = 'Choose the difficulty', font = ('Aerial 15 bold'))
    title.grid(column = 0, row = 0, padx = 140, pady = 75)
    easy = Button(window, text = 'Easy', font = ('Aerial 10'), command = lambda: add_question('E'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    easy.grid(column = 0, row = 1, pady = 20)
    medium = Button(window, text = 'Normal', font = ('Aerial 10'), command = lambda: add_question('N'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    medium.grid(column = 0, row = 2, pady = 20)
    hard = Button(window, text = 'Hard', font = ('Aerial 10'), command = lambda: add_question('H'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    hard.grid(column = 0, row = 3, pady = 20)
    back = Button(window, text = 'Back', font = ('Aerial 10'), command = edit_menu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 4, pady = 80)

def add_question(difficulty):
    clear()
    for x in range(0,6):
        label = 'label' + str(x)
        answer = 'Answer nº ' + str(x)
        if x == 0:
            label = Label(window, text = 'Add a question', font = ('Aerial 15 bold'))
            label.grid(column = 1, row = 0, pady = (45,15))
        elif x == 1:
            label = Label(window, text = 'Correct Answer', font = ('Aerial 10 bold'))
            label.grid(column = 0, row = x + 1, padx = (0,5))
        else:
            label = Label(window, text = answer, font = ('Aerial 10'))
            label.grid(column = 0, row = x + 1, padx = (15,0))

    text0 = Text(window, bg = 'grey80', bd = 3, height = 4, width = 35)
    text0.grid(column = 1, row = 1, pady = (10,10))
    text1 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text1.grid(column = 1, row = 2, pady = 15)
    text2 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text2.grid(column = 1, row = 3, pady = 15)
    text3 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text3.grid(column = 1, row = 4, pady = 15)
    text4 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text4.grid(column = 1, row = 5, pady = 15)
    text5 = Text(window, bg = 'grey85', bd = 3, height = 2, width = 35)
    text5.grid(column = 1, row = 6, pady = 15)

    back = Button(window, text = 'Back', font = ('Aerial 10'), command = add_difficulty, height = 1, width=10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 7, padx = (5,0), pady = 25)
    next = Button(window, text = 'Next', font = ('Aerial 10'), command = lambda: add_end(text0.get(1.0,END), difficulty, text1.get(1.0,END), text2.get(1.0,END), text3.get(1.0,END), text4.get(1.0,END), text5.get(1.0,END)), height = 1, width=10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    next.grid(column = 2, row = 7, padx = (0,10), pady = 25)

def add_end(q,d,a1,a2,a3,a4,a5):
    q = " ".join(q.splitlines())
    new_question = [q,d,a1,a2,a3,a4,a5]
    new_question = [str(x.strip()) for x in new_question]

    error = Label(window, font = ('Aerial 12 italic'), fg = 'red')
    error.grid(column = 1, row = 7)
    if len(new_question[0]) == 0:
        error.config(text = 'Error: No question')
    elif len(new_question[2]) == 0 or len(new_question[3]) == 0 or len(new_question[4]) == 0 or len(new_question[5]) == 0 or len(new_question[6]) == 0:
        error.config(text = 'Error: Answers missing')
    elif new_question[1] != 'H' and new_question[1] != 'N' and new_question[1] != 'E':
        error.config(text = 'Error: Invalid difficulty')
    elif len(new_question[1]) == 0:
        error.config(text = 'Error: No difficulty')
    else:
        file('a', new_question)
        clear()
        title = Label(window, text = 'Question added!', font = ('Aerial 15 bold'))
        title.grid(column = 0, row = 0, padx = 160, pady = 180)
        back = Button(window, text = 'Return', font = ('Aerial 10'), command = lambda: edit_menu(), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        back.grid(column = 0, row = 1)

def remove_question(question):
    set = file('r')[question]
    set[0] = (set[0][:100] + '...') if len(set[0]) > 100 else set[0]
    set[1] = (set[1][:67] + '...') if len(set[1]) > 67 else set[1]
    set[2] = (set[2][:67] + '...') if len(set[2]) > 67 else set[2]
    set[3] = (set[3][:67] + '...') if len(set[3]) > 67 else set[3]
    set[4] = (set[4][:67] + '...') if len(set[4]) > 67 else set[4]
    set[5] = (set[5][:67] + '...') if len(set[5]) > 67 else set[5]

    clear()
    title = Label(window, text = 'Delete this question?', font = ('Aerial 15 bold'))
    title.grid(column = 0, row = 0, padx = 140, pady = (40,10))
    q = Label(window, text = set[0], font = ('Aerial 12 bold'), wraplength = 300)
    q.grid(column = 0, row = 1, pady = 10)
    a1 = Label(window, text = set[2], font = ('Aerial 10 italic'), wraplength = 200)
    a1.grid(column = 0, row = 2, pady = 10)
    a2 = Label(window, text = set[3], font = ('Aerial 10 italic'), wraplength = 200)
    a2.grid(column = 0, row = 3, pady = 10)
    a3 = Label(window, text = set[4], font = ('Aerial 10 italic'), wraplength = 200)
    a3.grid(column = 0, row = 4, pady = 10)
    a4 = Label(window, text = set[5], font = ('Aerial 10 italic'), wraplength = 200)
    a4.grid(column = 0, row = 5, pady = 10)
    a5 = Label(window, text = set[6], font = ('Aerial 10 italic'), wraplength = 200)
    a5.grid(column = 0, row = 6, pady = 10)
    d = Label(window, font = ('Aerial 10 bold'),)
    d.grid(column = 0, row = 7, pady = (10, 0))
    if set[1] == 'E':
        d.config(text = 'Easy')
    elif set[1] == 'N':
        d.config(text = 'Normal')
    else:
        d.config(text = 'Hard')
    back = Button(window, text = 'No', font = ('Aerial 10'), command = lambda: question_list(0, 'remove'), height = 1, width = 10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 8, padx = (0, 300), pady = 20)
    delete = Button(window, text = 'Yes', font = ('Aerial 10'), command = lambda: remove_end(question), height = 1, width = 10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    delete.grid(column = 0, row = 8, padx = (300, 0), pady = 20)

def remove_end(question):
    file('d', old = question)
    clear()
    title = Label(window, text = 'Question removed!', font = ('Aerial 15 bold'))
    title.grid(column = 0, row = 0, padx = 160, pady = 180)
    back = Button(window, text = 'Return', font = ('Aerial 10'), command = lambda: edit_menu(), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 0, row = 1)

def scbd_add(player, score, got):
    file = open('Scores.txt', 'r')
    read = file.read()
    lines = read.splitlines()
    scores = [x.split('||') for x in lines]
    file.close()

    new_score = [str(player), str(score), str(got)]
    scores = scores[::-1]

    for x in scores:
        if new_score[0] == x[0]:
            scores.pop(scores.index(x))

    for x in scores:
        if int(new_score[1]) == int(x[1]):
            scores.insert(scores.index(x) + 1, new_score)
            break
        elif int(new_score[1]) < int(x[1]):
            scores.insert(scores.index(x), new_score)
            break
        elif scores.index(x) == (len(scores) - 1):
            scores.insert(len(scores), new_score)
            break
    if len(scores) == 0:
        scores.append(new_score)

    scores = scores[::-1]
    file = open('Scores.txt', 'w')
    for x in range(0, len(scores)):
        if x > 0 and x < len(scores):
            file.write('\n')
        file.write('||'.join(scores[x]))
    file.close()

def scbd():
    file = open('Scores.txt', 'r')
    read = file.read()
    lines = read.splitlines()
    list = [x.split('||') for x in lines]
    file.close()

    clear()
    title = Label(text = 'SCOREBOARD', font = ('Aerial 15 bold'))
    title.grid(column = 1, row = 0, padx = (48,0), pady = (30, 25))
    back = Button(window, text = 'Back', font = ('Aerial 10'), command = mainmenu, height = 1, width = 10, bd = 4, bg = 'grey85', activebackground = 'grey75')
    back.grid(column = 1, row = 11, padx = (50,0), pady = 20)

    for x in range(1, 11):
        rank = 'rank' + str(x)
        name = 'name' + str(x)
        score = 'score' + str(x)
        grade = 'grade' + str(x)

        rank = Label(text = '', font = ('Aerial 12 bold'), height = 2, width = 5, bg = 'grey85')
        rank.grid(column = 0, row = x, padx = (35,0))
        name = Label(text = 'AAABBBCCCDDDEEEFFF...', font = ('Aerial 12 bold'), height = 2, width = 25, bg = 'grey85')
        name.grid(column = 1, row = x)
        score = Label(text = '', font = ('Aerial 12 bold'), height = 2, width = 5, bg = 'grey85')
        score.grid(column = 2, row = x)
        grade = Label(text = '', font = ('Aerial 12 bold'), height = 2, width = 5, bg = 'grey85')
        grade.grid(column = 3, row = x)
        
        try:
            rank.config(text = str(x) + 'º')
            player = (list[x - 1][0][:17] + '...') if len(list[x - 1][0]) > 17 else list[x - 1][0]
            name.config(text = player)
            score.config(text = list[x - 1][1])
            grade.config(text = str(list[x - 1][2]) + '/10')
        except IndexError:
            rank.config(text = '', bg = '#F0F0F0')
            name.config(text = '', bg = '#F0F0F0')
            score.config(text = '', bg = '#F0F0F0')
            grade.config(text = '', bg = '#F0F0F0')

def help(h):
    clear()
    if h == 'h':
        title = Label(text = 'Help Menu', font = ('Aerial 15 bold'))
        title.grid(column = 0, row = 0, padx = 188, pady = (70,55))
        game = Button(text = 'Game', font = ('Aerial 10'), command = lambda: help('g'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        game.grid(column = 0, row = 1, pady = 15)
        edit = Button(text = 'Editing', font = ('Aerial 10'), command = lambda: help('e'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        edit.grid(column = 0, row = 2, pady = 15)
        score = Button(text = 'Scoreboard', font = ('Aerial 10'), command = lambda: help('s'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        score.grid(column = 0, row = 3, pady = 15)
        back = Button(text = 'Back', font = ('Aerial 10'), command = mainmenu, height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        back.grid(column = 0, row = 4, pady = 90)
    else:
        title = Label(text = 'Editing', font = ('Aerial 20 bold'))
        title.grid(column = 0, row = 0, pady = (80,30))
        info = Label(text = '', font = ('Aerial 13'), height = 15, width = 40, bg = 'grey85', wraplength = 300)
        info.grid(column = 0, row = 1, padx = 62)
        back = Button(text = 'Back', font = ('Aerial 10'), command = lambda: help('h'), height = 1, width = 15, bd = 4, bg = 'grey85', activebackground = 'grey75')
        back.grid(column = 0, row = 4, pady = 50)
        if h == 'g':
            title.config(text = 'Game')
            info.config(text = 'The game consists of 10 randomly sorted questions of 3 different levels. Each question has only ONE correct answer. Easy questions reward the player 40 poins, Normal questions rewad 60, and Hard, 100.\n\nTo encourage players, in order to achieve maximum score, you must be lucky enough to be sorted as many hard questions as possible.')
        elif h == 'e':
            title.config(text = 'Editing')
            info.config(text = 'When adding or editing a question, you cannot leave a blank space. Every question must have a body, 5 answers and a difficulty.\n\nWhen editing, on the Difficulty field, type Easy, Normal, Hard, E, N or H, accordingly.')
        elif h == 's':
            title.config(text = 'Scoreboard')
            info.config(text = "The scoreboard shows the 10 highest scoring players, in order.\n\nIf your last score was higher than the previous one, it is updated.\n\nFor competitive reasons, if two scores are the same, the most recent player to achieve it will get the higher position.\n\nYou cannot edit or erase the scoreboard's content through the game.")

def music():
    if mus['text'] == '🔊':
        pygame.mixer.music.pause()
        mus.config(text = '🔇')
    elif mus['text'] == '🔉':
        pygame.mixer.music.set_volume(0.7)
        mus.config(text = '🔊')
    elif mus ['text'] == '🔈':
        pygame.mixer.music.set_volume(0.4)
        mus.config(text = '🔉')
    else:
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.unpause()
        mus.config(text = '🔈')

pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops = -1)
window = Tk()
window.title('HPQ')
window.geometry('500x600')
mainmenu()
window.mainloop()