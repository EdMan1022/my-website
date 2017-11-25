from my_website.create_app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from my_website.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig())

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
