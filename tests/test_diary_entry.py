from lib.diary_entry import *

def load_diary():
    with open('diary.txt', 'r') as file:
        return file.read()

diary = str(load_diary())

def test_diary_entry_functional():
    diary_entry = DiaryEntry('title', 'contents')
    assert(diary_entry)

def test_diary_entry_count_words_returns_int():
    diary_entry = DiaryEntry('this title', 'this is the contents')
    assert type(diary_entry.count_words()) == int

def test_diary_entry_count_words_accurate():
    diary_entry = DiaryEntry('this title', 'this is the contents')
    assert diary_entry.count_words() == 4

def test_diary_entry_reading_time_returns_int():
    diary_entry = DiaryEntry('this title', diary)
    assert type(diary_entry.reading_time(1)) == int

def test_diary_entry_reading_time_accurate():
    diary_entry = DiaryEntry('this title', diary)
    assert diary_entry.reading_time(100) == 10

def test_diary_entry_reading_chunk_returns_string():
    diary_entry = DiaryEntry('this title', diary)
    assert type(diary_entry.reading_chunk(1, 1)) == str

def test_diary_entry_reading_chunk_returns_string_right_length():
    diary_entry = DiaryEntry('this title', diary)
    assert len(diary_entry.reading_chunk(100, 1).split(' ')) == 100

def test_diary_entry_reading_chunk_returns_next_chunk():
    diary_entry = DiaryEntry('this title', 'this is the contents')
    diary_entry.reading_chunk(1, 1)
    assert diary_entry.reading_chunk(1, 1) == 'is'