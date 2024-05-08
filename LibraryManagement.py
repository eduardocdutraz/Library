import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk

class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("400x500")
        self.master.config(bg="#ebebeb")

        self.books=[]
        self.lendlist=[]

        self.loginFrame = tk.Frame(self.master, bg="#ebebeb")
        self.loginFrame.pack(pady=20)

        self.loginLabel = tk.Label(self.loginFrame, text="Library Management System", font=("Helvetica",16),bg="#ebebeb",fg='#333')
        self.loginLabel.pack()

        self.usernameLabel = tk.Label(self.loginFrame, text="Username", font=("Helvetica",12),bg="#ebebeb",fg='#333')
        self.usernameLabel.pack(pady=(20,5))
        self.usernameEntry = tk.Entry(self.loginFrame, font=("Helvetica",12))
        self.usernameEntry.pack(pady=5)

        self.passwordLabel = tk.Label(self.loginFrame, text="Password", font=("Helvetica",12),bg="#ebebeb",fg='#333')
        self.passwordLabel.pack(pady=(10,5))
        self.passwordEntry = tk.Entry(self.loginFrame, show="*", font=("Helvetica", 12))
        self.passwordEntry.pack(pady=5)

        self.loginButton = ttk.Button(self.loginFrame, text="Login", command=self.login, style='TButton')
        self.loginButton.pack(pady=20, fill=tk.X)

        self.registerButton = ttk.Button(self.loginFrame, text="Register", command=self.register, style='TButton')
        self.registerButton.pack(pady=10, fill=tk.X)

        self.username=""
        self.password=""
        self.librarians=[]

    def login(self):
        self.username=self.usernameEntry.get()
        self.password=self.passwordEntry.get()
        for librarian in self.librarians:
            if self.username==librarian[0] and self.password==librarian[1]:
                self.loginFrame.destroy()
                self.libraryManagementScreen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username=self.usernameEntry.get()
        self.password=self.passwordEntry.get()
        self.librarians.append([self.username, self.password])
        messagebox.showinfo("Success", "Registration successful. You can now login.")
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0, tk.END)

    def libraryManagementScreen(self):
        self.managementFrame = tk.Frame(self.master, bg="#ebebeb")
        self.managementFrame.pack(pady=20)

        self.addBookLabel = tk.Label(self.managementFrame, text="Add Book", font=("Helvetica",16), bg='#ebebeb',fg='#333')
        self.addBookLabel.pack()
        self.addBookEntry = tk.Entry(self.managementFrame, font=('helvetica',12))
        self.addBookEntry.pack(pady=5)
        self.addButton = ttk.Button(self.managementFrame, text='Add Book', command=self.addBook, style='TButton')
        self.addButton.pack(pady=10, fill=tk.X)

        self.removeBookLabel = tk.Label(self.managementFrame, text="Remove Book", font=("Helvetica",16), bg='#ebebeb',fg='#333')
        self.removeBookLabel.pack()
        self.removeBookEntry = tk.Entry(self.managementFrame, font=('helvetica',12))
        self.removeBookEntry.pack(pady=5)
        self.removeBookButton = ttk.Button(self.managementFrame, text='Remove Book', command=self.removeBook, style='TButton')
        self.removeBookButton.pack(pady=10, fill=tk.X)

        self.issueBookLabel = tk.Label(self.managementFrame, text="Issue Book", font=("Helvetica",16), bg='#ebebeb',fg='#333')
        self.issueBookLabel.pack()
        self.issueBookEntry = tk.Entry(self.managementFrame, font=('helvetica',12))
        self.issueBookEntry.pack(pady=5)
        self.issueBookButton = ttk.Button(self.managementFrame, text='Issue Book', command=self.issueBook, style='TButton')
        self.issueBookButton.pack(pady=10, fill=tk.X)

        self.viewBooksButton = ttk.Button(self.managementFrame, text='View Books', command=self.viewBook, style='TButton')
        self.viewBooksButton.pack(pady=20, fill=tk.X)

    def addBook(self):
        book=self.addBookEntry.get()
        self.books.append(book)
        messagebox.showinfo("Success", "Book added successfully")
        self.addBookEntry.delete(0, tk.END)

    def removeBook(self):
        book=self.removeBookEntry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success","Book removed successfully")
        else:
            messagebox.showerror("Error","This book does not exist.")
        self.removeBookEntry.delete(0, tk.END)

    def issueBook(self):
        book=self.issueBookEntry.get()
        if book in self.books:
            self.lendlist.append(book)
            self.books.remove(book)
            messagebox.showinfo("Success","Book issued successfully")
        else:
            messagebox.showerror("Error","Book not found")
        self.issueBookEntry.delete(0,tk.END)

    def viewBook(self):
        if self.books:
            message= "\n".join(self.books)
            messagebox.showinfo("Library Books",message)
        else:
            messagebox.showinfo("Library Books", "No books available in the library.")

if __name__=="__main__":
    root=tk.Tk()
    app=LibraryManagement(root)
    root.mainloop()
