from flask_restful import Resource
import logging
from flask import current_app


logger = logging.getLogger("log")


class Test(Resource):

    def get(self):

        logger.info("hello i am test!")

        return {"a": "zzzz"}
