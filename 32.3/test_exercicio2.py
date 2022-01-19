from exercicio2 import letters_to_phone_numbers

def test_returns_expected_string_when_oitudobem_is_inserted():
    assert letters_to_phone_numbers('oitudobem') == '648836236'

def test_returns_expected_string_when_empty_string_is_inserted():
    assert letters_to_phone_numbers('') == ''

def test_returns_expected_string_when_special_characters_are_inserted():
    assert letters_to_phone_numbers('!@*ˆ#!(*') == '!@*ˆ#!(*'
