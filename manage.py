from app import create_app
from flask_script import Manager,Server

app = create_app('development')

manage = Manager(app)
manage.add_command('server',Server)

@manage.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manage.run()