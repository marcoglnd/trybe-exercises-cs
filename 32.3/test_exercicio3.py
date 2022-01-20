import pytest
from exercicio3 import verify_email

def test_raises_error_when_email_format_invalid():
    with pytest.raises(ValueError, match='Email deve possuir @'):
        verify_email('omeusuarionomewebsite.extensao')

def test_raises_error_when_username_dont_start_with_letter():
    with pytest.raises(ValueError, match='Nome do usuário deve iniciar com letra'):
        verify_email('1omeusuario@nomewebsite.extensao')

def test_raises_error_when_username_format_invalid():
    with pytest.raises(ValueError, match='Nome do usuário deve conter somente letras, dígitos, traços e underscores'):
        verify_email('omeu**suario@nomewebsite.extensao')

def test_raises_error_when_website_format_invalid():
    with pytest.raises(ValueError, match='Nome do website deve conter somente letras e dígitos'):
        verify_email('omeusuario@nome--website.extensao')
        
def test_raises_error_when_extension_length_invalid():
    with pytest.raises(ValueError, match='Tamanho máximo da extensão é três'):
        verify_email('omeusuario@nomewebsite.extensao')

def test_returns_success_message_when_email_valid():
    verify_email('omeusuario@nomewebsite.com')
