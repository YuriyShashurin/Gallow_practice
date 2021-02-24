import pytest
from gallow import WORDS, GallowGame, random_word

WORD = 'blackbox'

def test_random_word():
    game_test  = GallowGame(name='Yura')
    assert game_test.hidden_word in WORDS

@pytest.mark.parametrize("input_letter", ['a', 'b', 'w', 'f'])
def test_valid_input_right_case(input_letter):
    game_test = GallowGame()
    result_valid = game_test.valid_user_input(input_letter)
    assert result_valid

@pytest.mark.parametrize("input_letter", ['aa', '1', 'b1', '1a'])
def test_valid_input_wrong_case(input_letter):
    game_test = GallowGame()
    result_valid = game_test.valid_user_input(input_letter)
    assert not result_valid

def test_check_create_game():
    name = 'Yuriy'
    game_test = GallowGame()
    game_test.name = name
    assert game_test.name == name
    assert game_test.MAX_WRONG_ATTEMPTS == 4
    assert game_test.current_wrong_attempts == 0
    assert game_test.user_letters == {}
    assert game_test.guessed == {}
    assert game_test.hidden_word in WORDS

@pytest.mark.parametrize("input_letter", ['b', 'c', 'k', 'x'])
def test_show_result_if_in_hidden(input_letter):
    game_test = GallowGame()
    game_test.hidden_word = WORD
    game_test.show_result(input_letter)
    assert input_letter in game_test.guessed

@pytest.mark.parametrize("input_letter", ['f', 'w', 'z', 'y'])
def test_show_result_if_not_in_hidden(input_letter):
    game_test = GallowGame()
    game_test.hidden_word = WORD
    game_test.show_result(input_letter)
    assert input_letter not in game_test.guessed

@pytest.mark.parametrize("input_letter", ['b', 'c', 'k', 'x'])
def test_check_result_if_in_hidden(input_letter):
    game_test = GallowGame()
    game_test.hidden_word = WORD
    assert game_test.check_letter(input_letter)


@pytest.mark.parametrize("input_letter", ['f', 'w', 'z', 'y'])
def test_check_result_if_not_in_hidden(input_letter):
    game_test = GallowGame()
    game_test.hidden_word = WORD
    assert not game_test.check_letter(input_letter)

def check_count_wrong_attempts():
    game_test = GallowGame()
    assert game_test.current_wrong_attempts + 1 == 1

@pytest.mark.parametrize("count", [0, 1, 2, 3,])
def check_continue_game(count):
    game_test = GallowGame()
    game_test.current_wrong_attempts = count
    assert not game_test.check_attemps()

def check_win_game():
    game_test = GallowGame()
    game_test.hidden_word = WORD
    game_test.guessed = WORD
    assert game_test.hidden_word == game_test.guessed

def check_fail_game():
    game_test = GallowGame()
    game_test.current_wrong_attempts = 4
    assert game_test.check_attemps()