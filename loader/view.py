from flask import Blueprint, request, render_template
import functions
import logging

#Объявление блюпринта
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('')
def load_upload_page():

    """
    Вывод на экран формы для добавления поста
    :return:
    """

    return render_template('post_form.html')


@loader_blueprint.route('', methods=['POST'])
def upload_page():

    """
    Добавление поста и вывод на экран формы с отображением добавленного поста
    :return:
    """

    picture = request.files.get('picture')
    content = request.form.get('content')

    picture_catalog = functions.save_picture(picture)
    if not picture_catalog:
        logging.info(f'{picture.filename} - не является картинкой')
        return 'Вы выбрали не изображение!!!'

    functions.save_content({'pic': picture_catalog, 'content': content})

    return render_template('post_uploaded.html', picture=picture_catalog, content=content)

