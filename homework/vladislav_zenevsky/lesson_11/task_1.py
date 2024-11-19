class Book:
    page_material = 'Бумага'
    presence_of_text = True

    def __init__(self, book_name, author, number_of_pages, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved


class SchoolBook(Book):

    def __init__(self, book_name, author, number_of_pages, isbn, reserved, subject, grade, exercises):
        super().__init__(book_name, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.exercises = exercises


book_1 = Book('1984', 'Джордж Оруэлл', 328, '9780451524935', True)
book_2 = Book('Убить пересмешника', 'Харпер Ли', 281, '9780061120084', True)
book_3 = Book('Мастер и Маргарита', 'Михаил Булгаков', 480, '9780140455465', False)
book_4 = Book('Гарри Поттер и философский камень', 'Джоан Роулинг', 223, '9780747532699', True)
book_5 = Book('Преступление и наказание', 'Фёдор Достоевский', 671, '9780140449136', False)

book_list = [book_1, book_2, book_3, book_4, book_5]
for book in book_list:
    print(
        f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
        f'материал: {book.page_material}' + (', зарезервирована' if book.reserved else ''))

school_book_1 = SchoolBook('Основы программирования', 'Иван Иванов', 300, '9785123456789', False, 'Программирование',
                           '10', True)
school_book_2 = SchoolBook('Математика для 9 класса', 'Мария Петрова', 250, '9785987654321', True, 'Математика', '9',
                           True)
school_book_3 = SchoolBook('История России', 'Александр Смирнов', 500, '9785111112223', False, 'История', '11', False)

school_book_3.reserved = True

school_book_list = [school_book_1, school_book_2, school_book_3]
for book in school_book_list:
    print(
        f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
        f'предмет: {book.subject}, класс: {book.grade}' + (', зарезервирована' if book.reserved else ''))
