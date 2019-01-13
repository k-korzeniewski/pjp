from Services.Service import Service
from ApplicationContext import ApplicationContext


class Manager:
    __services = []
    __output = None

    @classmethod
    def append_service(cls, service: Service):
        if service.get_instance() in cls.__services:
            raise ValueError("This service is already added")
        service.change_output(cls.__output)
        cls.__services.append(service.get_instance())
        print(cls.__services)

    @classmethod
    def remove_service(cls, service: Service):
        if service.get_instance() not in cls.__services:
            raise ValueError("This service is not added")
        if service in cls.__services:
            cls.__services.remove(service.get_instance())
        print(cls.__services)

    @classmethod
    def start_services(cls):
        for service in cls.__services:
            for link in ApplicationContext.link_list:
                service.start(link)

    @classmethod
    def get_services_list(cls) -> list:
        return cls.__services

    @classmethod
    def change_output(cls,output):
        cls.__output = output
