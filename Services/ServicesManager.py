from Services.Service import Service
from ApplicationContext2 import ApplicationContext


class Manager:
    __services = []

    @classmethod
    def append_service(cls, service: Service):
        if service in cls.__services:
            raise ValueError("This service is already added")
        cls.__services.append(service)
        print(cls.__services)

    @classmethod
    def remove_service(cls, service: Service):
        if service not in cls.__services:
            raise ValueError("This service is not added")
        if service in cls.__services:
            cls.__services.remove(service)
        print(cls.__services)

    @classmethod
    def start_services(cls):
        for service in cls.__services:
            for link in ApplicationContext.link_list:
                service.start(link)

    @classmethod
    def get_services_list(cls) -> list:
        return cls.__services
