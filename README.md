# Tests for BooksCollector

## Реализованные тесты

- test_add_new_book_added_correctly — проверяет, что книга корректно добавляется.  
- test_add_new_book_empty_name_not_added — проверяет, что книга с пустым названием не добавляется.  
- test_add_new_book_not_added_if_too_long — проверяет, что слишком длинное название книги не добавляется.  
- test_set_book_genre_and_get — проверяет установку жанра книги и его получение.  
- test_set_book_genre_invalid_genre_does_not_change — проверяет, что при некорректном жанре книга остаётся без жанра.  
- test_get_books_for_children_excludes_age_restricted — проверяет, что из детского списка исключаются книги с «18+» жанрами.  
- test_add_book_in_favorites_and_get_list — проверяет добавление книги в избранное и получение списка.  
- test_add_book_in_favorites_cannot_add_twice — проверяет, что одну и ту же книгу нельзя добавить в избранное дважды.  
- test_delete_book_from_favorites — проверяет удаление книги из избранного.  
- test_get_books_with_specific_genre_parametrized — проверяет возврат списка книг по заданному жанру (параметризованные тесты).