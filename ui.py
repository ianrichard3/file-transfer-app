import customtkinter as ctk

ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("File Transfer")

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        # Rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)


        # Title
        self.title = ctk.CTkLabel(self, text="File Transfer", font=("helvetica", 25))
        

        # /// Buttons

        # Main Menu
        self.new_transfer = ctk.CTkButton(self, 100, 20, 1.5, text="New Transfer")
        self.manage_devices = ctk.CTkButton(self, 100, 20, 1.5, text="Manage Devices")
        self.options = ctk.CTkButton(self, 100, 20, 1.5, text="Options")
        self.close = ctk.CTkButton(self, 100, 20, 1.5, text="Exit")
        self.back = ctk.CTkButton(self, 100, 20, 1.5, text="Back")

    





        self.show_main_menu()

    def show_main_menu(self):
        self.title.grid(row=0, column=0, columnspan=3)
        self.new_transfer.grid(row=1, column=1)
        self.manage_devices.grid(row=2, column=1)
        self.options.grid(row=3, column=1)
        self.close.grid(row=4, column=1)
    
    def hide_main_menu(self):
        self.title.grid_forget()
        self.new_transfer.grid_forget()
        self.manage_devices.grid_forget()
        self.options.grid_forget()
        self.close.grid_forget()


app = App()



app.mainloop()