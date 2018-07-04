import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('application.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name