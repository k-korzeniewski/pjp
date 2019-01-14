class ServiceContext:
    def __init__(self):
        self.values = dict()

    def get_values(self, key):
        return self.values[key]

    def set_values(self, key, value):
        self.values[key] = value


class Service:
    context = None
    output = None

    def __init__(self, context: ServiceContext):
        if (context is None):
            raise ValueError("Context must be provided")

        self.context = context

    def get_instance(self):
        raise NotImplementedError("get_instance() must be implemented -> service must be singleton")

    def start(self, *arguments):
        raise NotImplementedError("start() method must be implemented")

    def set_context(self, context):
        self.context = context

    def change_output(self, output):
        self.output = output
