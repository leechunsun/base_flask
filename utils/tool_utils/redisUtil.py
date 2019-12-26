from redis import Redis

from exceptions.project_excepions import IllegalConditionException


class RedisUtil:

    def __init__(self, app, condition=None):
        self.app = app
        self.condition = condition if condition else "default"

    def get_connection(self, **kwargs):
        if self.condition not in self.app.config["REDIS_CONFIGS"]:
            raise IllegalConditionException("condition of redis is illegal! please check")
        return Redis(**self.app.config["REDIS_CONFIGS"].get(self.condition), **kwargs)
