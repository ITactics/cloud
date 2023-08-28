import os
import uuid
from flask import Flask

app = Flask(__name__)

@app.route('/hostname')
def get_hostname():
    return os.uname().nodename


@app.route('/author')
def get_author():
    author = os.environ.get('AUTHOR', 'Max Kauger')
    return author

@app.route('/id')
def get_id():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.debug = True  # Включение режима отладки
    app.run(host='0.0.0.0', port=8000) # Запуск приложения на всех адресах, порт 8000
