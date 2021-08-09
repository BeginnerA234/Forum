import random

import requests
from bs4 import BeautifulSoup
from time import sleep

URL = 'https://dota2.ru/forum/'


def get_html(url):
    r = requests.get(url)
    return r.text


def get_links(html: str) -> dict:
    """
    Достаем название раздела.
    Название и ссылку на подраздел
    """
    soup = BeautifulSoup(html, 'lxml')
    chapters = soup.find_all(class_='forum-page__title')
    divs = soup.find_all(class_='forum-page__list')

    all_links = {}

    for chapter, div in zip(chapters, divs):

        # название раздела
        chapter_title = chapter.text.strip()
        all_links[chapter_title] = []

        items = div.find_all(class_='forum-page__item unread')
        sections = div.find_all(class_='forum-page__item unread')

        for item, section in zip(items, sections):
            # название подраздела
            section_name = section.find(class_='forum-page__item-title').text.strip()
            section_link = item.find(class_='forum-page__item-title')['href']
            all_links[chapter_title].append(
                {
                    'name': section_name,
                    'link': section_link
                }
            )

    return all_links


def titles_and_links_theme(html):
    """Достаем названия и ссылки на темы"""

    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all(class_='forum-section__table')
    data = {}
    for i in div:
        themes = i.find_all(class_='forum-section__title')
        for y in themes:
            title = y.text.strip()
            link = y.find('a')['href'].split('forum')[-1][1:-1]
            data[title] = link

    return data


def get_comments(html):
    """Достаем все комментарии из темы"""

    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all(class_='messageText baseHtml')
    comments = []

    for item in items:
        comments.append(item.text.strip().split('...')[-1].strip())

    return comments


def main(chapter: object, subsection: object, theme: object, comment: object, user: object):
    html = get_html(URL)
    all_links = get_links(html)

    users = user.objects.all()

    for chapter_title, links in all_links.items():
        # создаем раздел
        _chapter = chapter.objects.create(title=chapter_title)
        print(f'Раздел {_chapter.title} успешно создан')

        for section in links:
            _subsection = subsection.objects.create(title=section['name'], chapter=_chapter)
            print('_'*100)
            print(f'Подраздел {_subsection} успешно создан')
            print('_'*100)
            html = get_html(URL + section['link'])  # получили html подраздела
            data = titles_and_links_theme(html)  # получили названия тем и ссылки
            sleep(1)

            for theme_title, link in data.items():
                html = get_html(URL + link)
                comments = get_comments(html)  # получили комментарии темы
                # sleep(3)

                for my_comment in comments:

                    if not theme.objects.filter(title=theme_title).exists():
                        _theme = theme.objects.create(
                            creator=random.choice(users), sub_section=_subsection,
                            title=theme_title, content=my_comment
                        )
                        print(f'Тема {_theme} успешно создана')

                    else:
                        _theme = theme.objects.get(title=theme_title)
                        comment.objects.create(
                            creator=random.choice(users),
                            theme=_theme,
                            comment=my_comment
                        )
                print(f'Комментарии для темы {theme_title} загружены')
                sleep(1)
        sleep(2)
    return
