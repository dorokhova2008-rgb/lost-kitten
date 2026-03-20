import os
import pickle

class Book:
    def __init__(self, title, author, status="доступна"):
        self.title = title
        self.author = author
        self.status = status

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.author} ({self.status})"

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def show_menu(self):
        pass

class User(Person):
    def __init__(self, name, borrowed_books=None):
        super().__init__(name)
        if borrowed_books:
            self.borrowed_books = borrowed_books
        else:
            self.borrowed_books = []

    def get_books(self):
        return self.borrowed_books

    def borrow_book(self, title):
        self.borrowed_books.append(title)

    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)

    def show_menu(self):
        print("1. Просмотреть доступные книги")
        print("2. Взять книгу")
        print("3. Вернуть книгу")
        print("4. Мои книги")
        print("0. Выход")

class Librarian(Person):
    def show_menu(self):
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Зарегистрировать пользователя")
        print("4. Список пользователей")
        print("5. Список книг")
        print("0. Выход")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    def load_data(self):
        if os.path.exists("books.pkl"):
            with open("books.pkl", "rb") as f:
                self.books = pickle.load(f)
                for line in f:
                    title, author, status = line.strip().split(";")
                    self.books.append(Book(title, author, status))

        if os.path.exists("users.pkl"):
            with open("users.pkl", "rb") as f:
                self.users = pickle.load(f)
                for line in f:
                    parts = line.strip().split(";")
                    name = parts[0]
                    if len(parts) > 1 and parts[1]:
                         books = parts[1].split(",")
                    else:
                         books = []
                    self.users.append(User(name, books))

    def save_data(self):
        with open("books.pkl", "wb") as f:
            pickle.dump(self.books, f)
            for book in self.books:
                f.write(f"{book.get_title()};{book.get_author()};{book.get_status()}\n")

        with open("users.pkl", "wb") as f:
            pickle.dump(self.users, f)
            for user in self.users:
                books = ",".join(user.get_books())
                f.write(f"{user.get_name()};{books}\n")

    def find_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user
        return None

    def find_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None

    def add_book(self):
        title = input("Название: ")
        author = input("Автор: ")
        self.books.append(Book(title, author))
        print("Книга добавлена.")

    def remove_book(self):
        title = input("Название книги: ")
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print("Книга удалена.")
        else:
            print("Книга не найдена.")

    def register_user(self):
        name = input("Имя пользователя: ")
        if self.find_user(name):
            print("Такой пользователь уже существует.")
        else:
            self.users.append(User(name))
            print("Пользователь зарегистрирован.")

    def show_users(self):
        for user in self.users:
            print(user.get_name())

    def show_books(self):
        for book in self.books:
            print(book)

    def show_available_books(self):
        for book in self.books:
            if book.get_status() == "доступна":
                print(book)

    def borrow_book(self, user):
        title = input("Название книги: ")
        book = self.find_book(title)

        if not book:
            print("Книга не найдена.")
            return

        if book.get_status() == "выдана":
            print("Книга уже выдана.")
        else:
            book.set_status("выдана")
            user.borrow_book(title)
            print("Книга выдана.")

    def return_book(self, user):
        title = input("Название книги: ")
        book = self.find_book(title)

        if not book:
            print("Книга не найдена.")
            return

        if title not in user.get_books():
            print("Вы не брали эту книгу.")
            return

        book.set_status("доступна")
        user.return_book(title)
        print("Книга возвращена.")

library = Library()

print("Выберите роль:")
print("1. Библиотекарь")
print("2. Пользователь")

role = input("Ваш выбор: ")

if role == "1":
    name = input("Имя библиотекаря: ")
    librarian = Librarian(name)

    while True:
        librarian.show_menu()
        choice = input("Выбор: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.register_user()
        elif choice == "4":
            library.show_users()
        elif choice == "5":
            library.show_books()
        elif choice == "0":
            break

elif role == "2":
    name = input("Имя пользователя: ")
    user = library.find_user(name)

    if not user:
        print("Пользователь не найден.")
    else:
        while True:
            user.show_menu()
            choice = input("Выбор: ")

            if choice == "1":
                library.show_available_books()
            elif choice == "2":
                library.borrow_book(user)
            elif choice == "3":
                library.return_book(user)
            elif choice == "4":
                print("Ваши книги:", user.get_books())
            elif choice == "0":
                break

library.save_data()
print("Данные сохранены.")


