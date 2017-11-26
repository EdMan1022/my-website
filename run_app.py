from my_website.create_app import create_app
from my_website.config import DevelopmentConfig

app = create_app(DevelopmentConfig())


if __name__ == '__main__':
    app.run()
