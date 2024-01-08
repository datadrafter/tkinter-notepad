import tkinter as tk
from tkinter import filedialog

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Notepad")
        self.text = tk.Text(self,wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        self.menu.add_cascade(label="New", command=self.new_file)
        self.menu.add_cascade(label="Open", command=self.open_file)
        self.menu.add_cascade(label="Save", command=self.save_file)
        self.menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        self.menu.add_cascade(label="Cut", command=self.cut)
        self.menu.add_cascade(label="Copy", command=self.copy)
        self.menu.add_cascade(label="Paste", command=self.paste)
        self.menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("Notepad")

    def open_file(self):
        file = filedialog.askopenfile(mode="w", defaultextension=".txt",filetypes=[("Text Documents", "*.txt"), ("All files","*.*")])
        if file:
            contents = file.read()
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name+"-Notepad")

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension="*.txt", filetypes=[("Text Documents", "*.txt"), ("All files","*.*")])
        if file:
            contents = self.text.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name+"-Notepad")

     
    def cut(self):
        self.text.event_generate("<<Cut>>")
    def copy(self):
        self.text.event_generate("<<Copy>>")
    def paste(self):
        self.text.event_generate("<<Paste>>")

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()
