import tkinter as tk
from tkinter import ttk

root= tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
#
# def display_chat():
#     pass
#
# USER = tk.StringVar
# for i in range(50):
#     ttk.Label(scrollable_frame, text="sample").pack()
#
# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")
#
# entry= tk.Entry(root,textvariable=USER, width=10)
# entry.pack(side="bottom", pady=10)
# btn = tk.Button(root, width=10, command=display_chat)
# btn.pack(side="bottom", pady=10, padx=30)
# root.mainloop()

list_t = { "list": ["hi", "hello"], "list2": "no"}
message = input("you: ")
for word in message:
    if message in list_t["list"]:
        print("yes")