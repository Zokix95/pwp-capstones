class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "Your are registered as user: {name}, email: {email}, books read: {books}.".format\
            (name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email has been updated to: {email}".format(email=self.email))

    def read_book(self, book, rating=None):
        self.rating = rating
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_values = 0
        for key, value in self.books.items():
            number_values += 1
            sum += value
            average = sum / number_values
        return average

    def __hash__(self):
        return hash((self.name, self.email))

    #def get_books(self):
    #    for key, value in self.books.items():
    #        print key
    #        print value

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "Title: '{title}', ISBN: {isbn}".format\
            (title=self.title, isbn=self.isbn)

    def __eq__(self, other_user):
        if self.title == other_user.title and self.isbn == other_user.isbn:
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Your ISBN has been updated to: {isbn}".format(isbn=self.isbn))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("This is an invalid rating.")

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    #def get_ratings(self):
    #    return self.ratings

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format\
            (title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, books=None):
        books = []
        self.users[email] = User(name, email)
        if books is not None:
            for b in books:
                for book, rating in b.items():
                    self.add_book_to_user(book, email, rating)
                return books


    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        return(max(self.books, key=self.books.get))

    def highest_rated_book(self):
        average_ratings_books = {}
        for book in self.books:
            average_ratings_books[book] = book.get_average_rating()
        print(max(average_ratings_books, key=average_ratings_books.get))

    def most_positive_user(self):
        pass
        average_ratings_user = {}
        for user in self.users.values():
            average_ratings_user[user] = user.get_average_rating()
        print(max(average_ratings_user, key=average_ratings_user.get))