'''
# from main import BooksCollector

# # класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# # обязательно указывать префикс Test
# class TestBooksCollector:

#     # пример теста:
#     # обязательно указывать префикс test_
#     # дальше идет название метода, который тестируем add_new_book_
#     # затем, что тестируем add_two_books - добавление двух книг
#     def test_add_new_book_add_two_books(self):
#         # создаем экземпляр (объект) класса BooksCollector
#         collector = BooksCollector()

#         # добавляем две книги
#         collector.add_new_book('Гордость и предубеждение и зомби')
#         collector.add_new_book('Что делать, если ваш кот хочет вас убить')

#         # проверяем, что добавилось именно две
#         # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
#         assert len(collector.get_books_rating()) == 2

#     # напиши свои тесты ниже
#     # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
'''


import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Обломов', 'Заводной апельсин'])
    def test_add_new_book_added_correctly(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()


    def test_add_new_book_empty_name_not_added(self, collector):
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()


    def test_add_new_book_not_added_if_too_long(self, collector):
        long_name = 'ABC' * 50
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()


    def test_set_book_genre_and_get(self, collector):
        collector.add_new_book('Заводной апельсин')
        collector.set_book_genre('Заводной апельсин', 'Фантастика')
        assert collector.get_book_genre('Заводной апельсин') == 'Фантастика'


    def test_set_book_genre_invalid_genre_does_not_change(self, collector):
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Триллер')
        assert collector.get_book_genre('Ангелы и демоны') == ''


    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book('Колобок')
        collector.add_new_book('Ледокол')
        collector.set_book_genre('Колобок', "Мультфильмы")  
        collector.set_book_genre('Ледокол', "Ужасы") 
        assert 'Колобок' in collector.get_books_for_children()
        assert 'Ледокол' not in collector.get_books_for_children()


    def test_add_book_in_favorites_and_get_list(self, collector):
        collector.add_new_book('Аквариум')
        collector.add_book_in_favorites('Аквариум')
        assert collector.get_list_of_favorites_books() == ['Аквариум']


    def test_add_book_in_favorites_cannot_add_twice(self, collector):
        collector.add_new_book('Остров сокровищ')
        collector.add_book_in_favorites('Остров сокровищ')
        collector.add_book_in_favorites('Остров сокровищ')
        assert collector.get_list_of_favorites_books().count('Остров сокровищ') == 1


    @pytest.mark.parametrize(
        'genre, books_list',
        [
            ('Фантастика', ['20 тысяч лье под водой']),
            ('Ужасы', ['Ледокол']),
            ('Детективы', []),  
        ]
    )
    def test_get_books_with_specific_genre_parametrized(self, collector, genre, books_list):
        collector.add_new_book('20 тысяч лье под водой')
        collector.add_new_book('Ледокол')
        collector.set_book_genre('20 тысяч лье под водой', "Фантастика")
        collector.set_book_genre('Ледокол', "Ужасы")
        assert collector.get_books_with_specific_genre(genre) == books_list
