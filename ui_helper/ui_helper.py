from tkinter import filedialog, messagebox, Tk, Frame, Button, Label, scrolledtext
import tkinter as tk
import time

from PIL import Image, ImageTk


class UIHelper:
    def __init__(self, ml_action):
        self.root = Tk()
        self.ml_action = ml_action
        self.navbar = self.create_navbar()
        self.action_frame = self.create_action_frame()
        self.result_frame = self.create_result_frame()
        self.result_label = self.create_result_label(self.result_frame)
        self.root.title('OCR by Mkoltonowski & Mbielenis')
        self.root.geometry('1280x720+0+0')
        self.root.resizable(False, False)
        self.root.wm_attributes("-transparentcolor", 'grey')
        self.root.mainloop()

    @staticmethod
    def image_prompt():
        image = filedialog.askopenfilename(
            title="Wybierz obraz z którego AI rozpozna słowa",
            filetypes=[("Obrazki", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")
                       ])
        return image

    @staticmethod
    def img_error_prompt():
        messagebox.showerror('Brak pliku', 'Error: Nie wprowadzono obrazka')

    @staticmethod
    def success_message_prompt(message):
        messagebox.showinfo(title='Zakończono rozpoznanie', message=message)

    def create_navbar(self):
        frame = Frame(self.root, bg="#333440", height=53, width=1280)
        frame.pack(fill="x")
        return frame

    @staticmethod
    def add_bg_image(parent, bg_image_path, width, height):
        img = ImageTk.PhotoImage(Image.open(bg_image_path).resize((width, height), Image.LANCZOS))
        label = tk.Label(parent, image=img)
        label.img = img
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_action_frame(self):
        frame = Frame(self.root, bg="#272630", height=667, width=752)
        frame.pack(side="left", fill="y")
        frame.pack_propagate(False)

        self.add_bg_image(frame, "./assets/image.png", width=752, height=668)

        # Label(frame, text="OCR", fg="white", bg="grey", font=("Inter", 48)).pack(side="top", fill="x", pady=(120,20))
        # Label(frame,
        #       text="Nie jest zły,\n nie jest też dobry,\n można powiedzieć że jest średni",
        #       fg="gray",
        #       # bg="grey",
        #       font=("Inter", 18),
        #       pady=40,
        #       wraplength=450
        # ).pack(side="top", fill="x")
        self.create_add_image_button(frame)
        return frame

    def print_results(self):
        result = self.ml_action()
        # if result["status"] == "error":
        #     color = "red"
        # else:
        #     color = "black"

        timestamp = time.time()

        formatted_time = f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}]: "

        self.result_label.insert("end","\n" + formatted_time + result["message"])
        print(result)

    def create_result_frame(self):
        frame = Frame(self.root, bg="#D9D9D9", height=667, width=528)
        frame.pack(side="left", fill="y", expand=True)
        return frame

    def create_result_label(self, frame):
        label = scrolledtext.ScrolledText(frame, wrap="word")
        label.pack(side="left", fill="both", expand=True)
        return label

    def create_add_image_button(self, parent):
        button = Button(parent, width=parent.winfo_width() // 2, text="Analizuj obrazek",
                        command=self.print_results, font=("Inter", 24), bg="#73FC9A", padx=20, pady=10, relief=tk.GROOVE, borderwidth=2)
        button.pack(side="top", pady=(420,0), padx=(0,70), fill="none")
