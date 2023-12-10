import ttkbootstrap as tkboot
from tkinter import Canvas, PhotoImage, HORIZONTAL, END, StringVar, Frame, LEFT, W, RIGHT, Listbox, VERTICAL, Y, X, CENTER


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def start_window(parent):

    def transition_to_main_window():
        signin_window.destroy()
        parent.deiconify()

    signin_window = tkboot.Toplevel()
    signin_window.geometry("600x290")
    signin_window.title('Start')
    signin_window.resizable(False, False)
    signin_window.iconbitmap(bitmap="images/app_logo.ico")
    signin_window.protocol('WM_DELETE_WINDOW', parent.quit)
    width, height = 1070, 600
    center_window(signin_window, width, height)

    app_Style = tkboot.Style()
    app_Style.configure("Sucess.TButton", font=('', 12, "bold"))

    start_frame = tkboot.Frame(signin_window, style="dark")
    start_frame.grid(row=0, column=0, padx=100, pady=50, sticky="WE")

    welcome_text = tkboot.Label(start_frame, text="Expense Tracker", font=("", 20, "bold"), background="#20374C")
    welcome_text.grid(row=0, column=0, pady=(20,5))

    instruction_text = tkboot.Label(start_frame,
                                text="Welcome to Expense Tracker - Your Personal Finance Manager!\n"
                                     "Effortlessly manage your expenses and gain insights into your spending habits.\n\n"
                                     "Here's how to get started:\n"
                                     "1. Click on 'Home' to record your daily expenses.\n\n"
                                     "2. Use 'Graph' to visualize your spending patterns over time.\n\n"
                                     "3. Add, update, or delete records as needed.\n\n"
                                     "4. Explore features like searching, resetting, and more.\n\n"
                                     "Let's take control of your finances! Click 'Start' below to begin.",
                                font=("", 12),
                                background="#20374C", justify=LEFT)
    instruction_text.grid(row=1, column=0, pady=(0, 20))

    start_button = tkboot.Button(start_frame,
                                   text="Start",
                                   style='success.TButton',
                                   takefocus=False,
                                   width=20,
                                   command=transition_to_main_window)
    start_button.grid(row=4, column=0, pady=20, ipady=5)

    exit_button = tkboot.Button(start_frame,
                            text="Exit",
                            style='danger.TButton', 
                            takefocus=False,
                            width=20,
                            command=signin_window.destroy) 
    exit_button.grid(row=5, column=0, pady=10, ipady=5)

    signin_window.columnconfigure(0, weight=10)
    start_frame.columnconfigure(0, weight=10)