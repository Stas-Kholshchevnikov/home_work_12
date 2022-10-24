import json
import logging
import conf


def load_all_posts():
    """
    Фукнция загрузки всех постов из json файла, с проверкой на возможность открытия файла
    :return:
    """
    try:
        with open(conf.POST_PATH, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except Exception:
        #Запись лога в случае не удачного открытия файла
        logging.info(f'Файл "{conf.POST_PATH}" не возможно открыть')
        return


def search_post(subword):
    """
    Поиск поста по вхождению в него искомого слова
    :param subword:
    :return:
    """
    search_post_list = []
    posts = load_all_posts()
    if not posts:
        return
    for post in posts:
        if subword.lower() in post['content'].lower():
            search_post_list.append(post)
    return search_post_list


def save_picture(picture):
    """
    Сохранение картинки в uploads и сохранение пути к ней
    :param picture:
    :return:
    """
    picture_name = picture.filename
    picture_type = picture_name.split('.')[-1]

    # Прверка файла на принадлежность к картинке по р асширению. Список допустимых расширений в файле conf.py
    if picture_type not in conf.CORRECT_TYPES:
        return

    picture.save(f'./{conf.UPLOAD_FOLDER}/{picture_name}')

    return f'/{conf.UPLOAD_FOLDER}/{picture_name}'


def save_json_posts(posts):
    """
    Сохранение словаря с постами в файл json
    :param posts:
    :return:
    """
    with open(conf.POST_PATH, 'w', encoding='UTF-8') as file:
        json.dump(posts, file, ensure_ascii=False)


def save_content(content):
    """
    Добавление нового поста в словарь с постами
    :param content:
    :return:
    """
    all_posts = load_all_posts()
    all_posts.append(content)

    save_json_posts(all_posts)
