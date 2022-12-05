from flask import Flask

from api.phone import phone
from api.command import command
from settings import SERVER_CONFIG

app = Flask(__name__)

app.register_blueprint(phone)
app.register_blueprint(command)

if __name__ == "__main__":
    app.run(host=SERVER_CONFIG["address"], port=SERVER_CONFIG["port"])
