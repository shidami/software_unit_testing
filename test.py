from game1 import GuessGame, generate_number, give_hints, validate_input


def test_generate_number():
    number = generate_number()
    assert len(number) == 4
    assert number.isdigit()
    assert 1000 <= int(number) <= 9999


def test_give_hints():
    assert give_hints("1234", "1234") == "oooo"
    assert give_hints("1234", "1243") == "ooxx"
    assert give_hints("1234", "4321") == "xxxx"
    assert give_hints("1234", "5678") == ""


def test_game_play(mocker):
    # Mocking the user input to 'quit'
    mocker.patch('builtins.input', return_value='quit')
    game = GuessGame()
    # Capture print outputs
    cap = mocker.patch('builtins.print')
    game.play()
    cap.assert_called_with("Thanks for playing!")


def test_validate_input():
    assert validate_input("12345") == False
    assert validate_input("abcd") == False
    assert validate_input("12a4") == False
    assert validate_input("1234") == True



