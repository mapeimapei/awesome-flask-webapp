'''
入口文件
'''
from app import create_app

__author__ = "带土"
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9000)
