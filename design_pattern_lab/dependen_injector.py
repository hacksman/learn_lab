# coding: utf-8
# @Time : 2021/2/28 11:16 AM

import os
import sys
from loguru import logger


from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide


# before
# class AppClient:
#
#     def __init__(self, api_key, timeout):
#         self.api_key = api_key
#         self.timeout = timeout
#
#
# class Service:
#
#     def __init__(self, api_client: AppClient):
#         self.api_client = api_client
#
#
# def main(service: Service):
#     pass
#
#
# if __name__ == '__main__':
#     main(service=Service(
#         api_client=AppClient(
#             api_key=os.getenv("API_KEY"),
#             timeout=os.getenv("TIMEOUT")
#         )
#     ))


class AppClient:

    def __init__(self, api_key, timeout):
        self.api_key = api_key
        self.timeout = timeout
        
        logger.info(f"api_key={self.api_key}\ttimeout={self.timeout}")


class Service:

    def __init__(self, api_client: AppClient):
        self.api_client = api_client
        logger.info(f"api_client={self.api_client}")


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    print('value>>>>', str(config.api_key))

    api_client = providers.Singleton(AppClient, api_key=config.api_key, timeout=config.timeout.as_int())

    service = providers.Factory(Service, api_client=AppClient)


@inject
def main(service: Service = Provide[Container.service]):
    pass


if __name__ == '__main__':
    container = Container()
    container.config.api_key.from_env("API_KEY")
    container.config.timeout.from_env("TIMEOUT")
    container.wire(modules=[sys.modules[__name__]])

    main()
