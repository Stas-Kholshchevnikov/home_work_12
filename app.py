from flask import Flask, send_from_directory
from loader.view import loader_blueprint
from main.view import main_blueprint
import logging


def main():
    app = Flask(__name__)

    #Создание логера
    logging.basicConfig(filename='log-info.log', level=logging.INFO, encoding='UTF-8',
                        format='%(asctime)s : %(message)s')

    #Регистрация блюпринтов в проекте
    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(loader_blueprint, url_prefix='/post')

    # Обработчик GET запроса по пути загрузки сохраненных локально картинок
    @app.route("/uploads/<path:path>")
    def static_dir(path):
        return send_from_directory("uploads", path)

    app.run()


if __name__ == "__main__":
    main()
