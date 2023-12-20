from tkinter import *
import diagnostician


class Application:
    def __init__(self, file):
        self.file = file
        self.win = Tk()
        self.diagnosing = diagnostician.Diagnostician(self.file)
        self.win.title('Asystent diagnostyczny')
        self.win_width = self.win.winfo_screenwidth()
        self.win_height = self.win.winfo_screenheight()
        self.win.geometry(f'{self.win_width}x{self.win_height}')
        self.win.configure(background='#0b429c')
        self.symptom_txt_var = StringVar()
        self.symptom_txt_var.set(self.diagnosing.ask_question())
        self.diseases = None
        self.symptoms = None
        self.draw()

    def draw(self):
        self.title_adv()
        self.line()
        self.questions()
        self.ans_buttons()
        self.line()
        self.bottom_info()

    def title_adv(self):
        label = Label(self.win, text='Asystent diagnostyczny chorób układu pokarmowego',
                      background='#0b429c', foreground='white',
                      font=("Segoe UI", 35, "bold"), pady=10)
        label.pack()

    def line(self):
        canvas = Canvas(self.win, width=self.win_width,
                        height=10, background='#0b429c',
                        highlightbackground='#0b429c')
        canvas.create_line(0, 0, self.win_width, 0, fill='white', width=15)
        canvas.pack()

    def questions(self):
        label = Label(self.win, text=f'Czy pacjent posiada objaw:',
                      background='#0b429c', foreground='white',
                      font=("Segoe UI", 20), pady=10)
        label.pack()
        label1 = Label(self.win, textvariable=self.symptom_txt_var,
                       background='#0b429c', foreground='white',
                       font=("Segoe UI", 20, "bold"))
        label1.pack()

    def update_text(self):
        if self.diagnosing.counter >= 0:
            self.symptom_txt_var.set(self.diagnosing.ask_question())
        else:
            self.symptom_txt_var.set("Brak możliwych objawów")

    def ans_buttons(self):
        label = Label(self.win, background='#0b429c')
        yes_button = Button(label, text='TAK',
                            fg='white', background='#0b429c',
                            bd=3, activebackground='#0e4eb5',
                            activeforeground='white',
                            font=("Segoe UI", 20),
                            width=6,
                            command=lambda: [self.fill_symptoms(), self.diagnosing.positive(),
                                             self.update_text(), button_state()])
        no_button = Button(label, text='NIE',
                           fg='white', background='#0b429c',
                           bd=3, activebackground='#0e4eb5',
                           activeforeground='white',
                           font=("Segoe UI", 20),
                           width=6,
                           command=lambda: [self.diagnosing.negative(), self.update_text(), button_state()])

        ans_button = Button(label, text='DIAGNOZUJ',
                            fg='white', background='#0b429c',
                            bd=3, activebackground='#0e4eb5',
                            activeforeground='white', width=11,
                            font=("Segoe UI", 20), command=lambda: [self.clear_textbox(), self.diagnosing.diagnose(),
                                                                    self.fill_diseases(), button_state()])
        ans_button.config(state=DISABLED)

        restart_button = Button(label, text='RESTART',
                                fg='white', background='#0b429c',
                                bd=3, activebackground='#0e4eb5',
                                activeforeground='white',
                                font=("Segoe UI", 20), width=11,
                                command=self.restart)
        yes_button.pack(side=LEFT, pady=20, padx=10)
        no_button.pack(side=RIGHT, pady=20, padx=10)
        ans_button.pack(pady=10)
        restart_button.pack(side=BOTTOM, pady=10)
        label.pack()

        def button_state():
            if self.symptom_txt_var.get() == "Brak możliwych objawów":
                ans_button.config(state=NORMAL)
                yes_button.config(state=DISABLED)
                no_button.config(state=DISABLED)
            if self.diseases.get(1.0, END) != "\n":
                ans_button.config(state=DISABLED)

    def bottom_info(self):
        core_label = Label(self.win, background='#0b429c')
        left_core = Label(core_label, background='#0b429c')
        right_core = Label(core_label, background='#0b429c')
        label = Label(left_core, text='Zarejestrowane symptomy',
                      background='#0b429c', foreground='white',
                      font=("Segoe UI", 20, "bold"))
        self.symptoms = Text(left_core, background='#0b429c',
                             foreground='white', font=("Segoe UI", 13),
                             spacing3=3, spacing1=3, padx=15)
        label2 = Label(right_core, text='Możliwe choroby',
                       background='#0b429c', foreground='white',
                       font=("Segoe UI", 20, "bold"))
        self.diseases = Text(right_core, background='#0b429c',
                             foreground='white', font=("Segoe UI", 13),
                             spacing3=3, spacing1=3, padx=15)
        label.pack(side=TOP, fill=BOTH)
        self.symptoms.pack(side=BOTTOM, fill=BOTH)
        label2.pack(side=TOP, fill=BOTH)
        self.diseases.pack(side=BOTTOM, fill=BOTH)
        left_core.pack(side=LEFT, fill=BOTH, padx=25)
        right_core.pack(side=RIGHT, fill=BOTH, padx=25)
        core_label.pack(fill=BOTH)

    def fill_symptoms(self):
        if self.diagnosing.counter >= 0:
            self.symptoms.config(state="normal")
            self.symptoms.insert(END, f'# {self.symptom_txt_var.get()}\n')
            self.symptoms.config(state="disabled")
        else:
            pass

    def fill_diseases(self):
        self.clear_textbox()
        self.diseases.config(state="normal")
        for item in self.diagnosing.diseases_percentage:
            self.diseases.insert(END, f'{item[0]}     {item[1]}%\n')
        self.diseases.config(state="disabled")

    def clear_textbox(self):
        self.diseases.config(state="normal")
        self.diseases.delete(1.0, END)
        self.diseases.config(state="disabled")

    def restart(self):
        self.win.destroy()
        self.__init__(self.file)

    def run_app(self):
        self.win.mainloop()
