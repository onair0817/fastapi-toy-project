from dependency_injector import containers, providers

from my_db_client import MyDbClient

import services


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["endpoints"])
    # config = providers.Configuration(yaml_files=["config.yml"])

    my_client = providers.ThreadSafeSingleton(MyDbClient)

    my_service = providers.Factory(
        services.MyService,
        client=my_client,
    )
