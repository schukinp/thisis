from selene.api import s, browser, ss
from random import choice


def test_homepage():
    browser.open_url('https://thisis.media')
    s('#anchor-media').click()
    s('#anchor-culture').click()
    s('#anchor-video').click()
    s('#anchor-about-us').click()
    choice(ss('div.about-us__cards-wrapper.swiper-container__preview > div')).click()
    s('img[alt="This is media"]').click()
    assert browser.title() == 'This Is Media'
    print('Тест прошел успешно!')


test_homepage()