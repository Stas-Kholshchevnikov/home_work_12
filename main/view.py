from flask import Blueprint, render_template, request
import functions
import logging
import conf

#Объявление блюпринта
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('')
def main_page():

    """
    Вывод на экран главной странички (рендер index.html)
    :return:
    """

    return render_template('index.html')


@main_blueprint.route('search')
def search_post_page():

    """
    Вывод на экран результатов поиска постов
    :return:
    """

    subword = request.args['s']
    search_post = functions.search_post(subword)

    if not search_post:

        #Вывод сообщения в случае не открытия файла с постами
        return f'Файл "{conf.POST_PATH}" не возможно открыть'

    #Запись лога по поиску
    logging.info(f'Поиск постов по содержимому "{subword}"')
    return render_template('post_list.html', subword=subword, search_post=search_post)
