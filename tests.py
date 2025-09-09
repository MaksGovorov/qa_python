import pytest
from main import BooksCollector


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

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.get_list_of_favorites_books()


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

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('20 тысяч лье под водой')
        collector.set_book_genre('20 тысяч лье под водой', 'Фантастика')
        genres = collector.get_books_genre()
        assert isinstance(genres, dict)
        assert genres['20 тысяч лье под водой'] == 'Фантастика'

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Ледокол')
        collector.set_book_genre('Ледокол', 'Ужасы')
        genre = collector.get_book_genre('Ледокол')
        assert genre == 'Ужасы'

