from lib.diary import *
from lib.diary_entry import *
import pytest

def load_diary():
    with open('diary.txt', 'r') as file:
        return file.read()

def load_diary_100():
    with open('diary_100.txt', 'r') as file:
        return file.read()

def load_diary_200():
    with open('diary_200.txt', 'r') as file:
        return file.read()
    
diary = str(load_diary())
diary_100 = str(load_diary_100())
diary_200 = str(load_diary_200())

def test_diary_adds_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry('title', 'contents')
    diary.add(diary_entry)
    assert diary.full_diary[0] == diary_entry

def test_diary_all_returns_all_entries():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'contents_1')
    diary_entry_2 = DiaryEntry('title_2', 'contents_2')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry, diary_entry_2]

def test_diary_count_words_returns_int():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'this is the first')
    diary_entry_2 = DiaryEntry('title_2', 'and second')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert type(diary.count_words()) == int

def test_diary_count_words_accurate():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'this is the first')
    diary_entry_2 = DiaryEntry('title_2', 'and second')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.count_words() == 6

def test_diary_reading_time_returns_int():
    diary = Diary()
    diary_entry = DiaryEntry('title', 'contents')
    assert type(diary.reading_time(1)) == int

def test_diary_reading_time_accurate():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.reading_time(100) == 3

def test_diary_find_best_entry_for_reading_time_exact_match():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.find_best_entry_for_reading_time(100, 1) == diary_entry_100

def test_diary_find_best_entry_for_reading_time_error_no_appropriate_entry():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary.add(diary_entry_100)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(50, 1)
    error_message = str(err.value)
    assert error_message == "No Appropriate Entry for Time Available"

def test_diary_find_best_entry_for_reading_time__not_exact_match():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.find_best_entry_for_reading_time(150, 1) == diary_entry_200