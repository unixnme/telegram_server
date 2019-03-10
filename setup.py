from setuptools import setup

setup(
    name='telegram_server',
    version='0.1.0',
    author='Young Mo Kang',
    author_email='kang.youngmo@gmail.com',
    packages=['server', 'client'],
    scripts=[],
    description='Telegram bot server and communications API',
    install_requires=[
        "python-telegram-bot >= 11.1.0",
    ],
)