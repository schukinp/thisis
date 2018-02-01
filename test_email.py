from selene.api import s, browser
from random import choice
import string


def random_email():
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(5)) + '@example.com'


def test_email(email):
    browser.open_url('https://thisis.media')
    s('input[type="email"]').set(email)
    s('label[for="policy-checkbox"]').click()
    s('button.subscribe-btn').click()
    assert s('span.subscribe-success-text').text == confirm_text


if __name__ == '__main__':
    email = random_email()
    confirm_text = 'Готово! Вы подписаны на почтовую рассылку This Is. Вы можете отписаться от нее в любом дайджесте'
    test_email(email)
    print('Тест прошел успешно!')