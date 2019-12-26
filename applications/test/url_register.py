from applications.test.views import *


def test_register(api):
    api.add_resource(Test, '/test')
