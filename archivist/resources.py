class BaseResource:
    @property
    def channel(self):
        raise NotImplementedError()

    @property
    def tag(self):
        raise NotImplementedError()

    def is_resource(self, message):
        return self.tag in message.text


class PythonResources(BaseResource):
    channel = '@rpythonresources'
    tag = '#python'


class JSResources(BaseResource):
    channel = '@rjavascriptresources'
    tag = '#js'


def get_resource(message):
    for resource in resource_list:
        if resource.is_resource(message):
            return resource


resource_list = [
    PythonResources(),
    JSResources()
]
