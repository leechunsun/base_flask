import os
from flask import Flask
from logging.config import dictConfig
from exceptions.project_excepions import IllegalConfigEnvException


class App:

    def __init__(self, config_env=None):
        self.config_env = config_env
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.conf_dir = os.path.join(self.base_dir, "conf")

    def generic_app(self):
        app = Flask("ip_proxy")
        # 导入setting配置文件
        app.config.from_pyfile(self._gen_settings_file_path())
        # 导入日志配置
        log = app.config.get("LOGGING", {})
        dictConfig(log)

        return app

    def _gen_settings_file_path(self):

        if self.config_env is None or self.config_env == "dev":
            conf_file = "settings.py"
        elif self.config_env == "pre":
            conf_file = "settings_pre.py"
        elif self.config_env == "prd":
            conf_file = "settings_prd.py"
        else:
            raise IllegalConfigEnvException("config env is illegal! fail to start the project !")
        return os.path.join(self.conf_dir, conf_file)
