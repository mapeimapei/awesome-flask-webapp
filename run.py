'''
入口文件
'''
from app import create_app
from app.models import db


__author__ = "带土"

app = create_app()
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=app.config["PORT"])
