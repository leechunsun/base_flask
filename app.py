from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from conf import App
from utils.tool_utils.redisUtil import RedisUtil


# allow the condition are ["dev", "pre", "prd"]
app = App("dev").generic_app()

db = SQLAlchemy(app)

redis_connection = RedisUtil(app).get_connection()

# 路由注册
api = Api(app, prefix="/aa")
from applications.test.url_register import test_register
test_register(api)




if __name__ == '__main__':
    app.run()
    pass
