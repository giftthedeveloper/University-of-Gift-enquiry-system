import json
import re
import bot_response_system as random_responses
import tkinter as tk
import tkinter.ttk as ttk
#loading the json file



def load_json(file):
    with open(file) as bot_responses:
        print("file loaded successfully")
        return json.load(bot_responses)

#to store the response data
responses_data = load_json("bot.json")

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.;-_]\s*', input_string)
    score_list= []

#checking all the responses
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

#to check if they are required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
#total no of required_words should match required_score
        if required_score == len(required_words):
            for word in split_message: #check each wordthe user typed
                if word in response["user_input"]:
                    response_score += 1



#add score to the list
        score_list.append(response_score)

#find the best response and return it if they are not at all return 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string == "":
        return "hiiiiiii :)"
    if best_response !=0:
        return responses_data[response_index]["bot_response"]

    return random_responses.random_bot_unknown_response()

def thing():
    print("Glory to God")


root = tk.Tk()
root.title("UNIVERSITY OF GIFT RESPONSE BOT (BOB)")
width = 600
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x =(screenwidth/2) - (width/2)
y = (screenheight/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg ="#282828")


# # =====================================
# container = ttk.Frame(root)
# canvas = tk.Canvas(container)
# scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)
#
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)
# #++++++++++++++++++++++++++++++++++++++++
# USER = tk.StringVar()
# #+++++++++++++++++++++++++++++++++++++
# def display_sender_chat():
#     global sender_rec
#     user = chat_input.get()
#     CHAT =get_response(user)
#
#     sender_rec = tk.Label(scrollable_frame, bg="white", text=user, font=("helvetica", 17))
#     sender_rec.pack()
#     bot_rec = tk.Label(scrollable_frame, bg="#035aba", fg="#ffffff", text=CHAT, font=("helvetica", 17))
#     bot_rec.pack(side="top", anchor="w", padx=10, pady=20)
#     USER.set("")

# =====================================
# container.pack()
# canvas.pack(side="left", fill="both", expand=1)
# scrollbar.pack(side="right", fill="y")
#
#
# global chat_input
# chat_input= tk.Entry(root,textvariable=USER, bg="white", fg="blue", width=40, font=("helvetica", 17))
# chat_input.pack(side="bottom", pady=5)
# send_btn = tk.Button(root,bg='#035aba',fg="#ffffff",text="SEND", font=("helvetica bold",15), command=display_sender_chat)
# send_btn.pack(side="bottom", pady=5, padx=30)

#========================================
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=1)

my_canvas = tk.Canvas(main_frame,  bg="#282828")
my_canvas.pack(side="left",fill="both",expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
my_scrollbar.pack(side="right", fill="y")

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion = my_canvas.bbox("all")))

second_frame = tk.Frame(my_canvas, bg="#282828")
my_canvas.create_window((260,100), window=second_frame,anchor="center")
# myscrollbar.config(command=root.yview)
# parent_s= ttk.Treeview(subroot,yscrollcommand=myscrollbar.set)
#
# root.config(yscrollcommand=myscrollbar.set)
user_u = tk.StringVar()

# CHAT = get_response(user)
def get_input():
    global sender_rec
    #sender_rec = tk.Label(root, bg="white", text=str(USER.get()), fg="blue")


def display_sender_chat():
    get_input()
    global user
    user = chat_input.get()
    CHAT = get_response(user)


    sender_rec = tk.Label(second_frame, bg="white", text=user, font=("helvetica", 12))
    sender_rec.pack(side="top", anchor="e", padx=10, pady=10)
    bot_rec = tk.Label(second_frame, bg="#035aba", fg="#ffffff", text=CHAT, font=("helvetica", 12))
    bot_rec.pack(side="top", anchor="w", padx=10, pady=20)

    user_u.set("")


# chat_space = tk.Frame(root, width=600)
# chat_space.pack(side="bottom", pady=50)
global chat_input
chat_input = tk.Entry(root, bg="white",textvariable=user_u, fg="blue", width=40, font=("helvetica", 17))
# scrollbar2 = tk.Scrollbar(root, orient="vertical")
# scrollbar2.pack(side="right")
chat_input.insert("end","")
chat_input.place(x=30, y=460)
send_btn = tk.Button(root, bg='#035aba', fg="#ffffff", text="SEND", font=("helvetica bold", 15),
                      command=display_sender_chat)
send_btn.place(x=505, y=458)

# while True:
#     user_input = input("You: ")
#     print("Bot: ", get_response(user_input))

root.mainloop()