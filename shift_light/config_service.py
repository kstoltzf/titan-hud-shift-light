import configparser


class ConfigService(object):
    config: configparser
    rabbitmq_config: configparser.SectionProxy

    def __init__(self, config_file: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.rabbitmq_config = self.config['RabbitMQ']

    def get_rabbitmq_host(self) -> str:
        return self.rabbitmq_config['host']

    def get_rabbitmq_vhost(self) -> str:
        return self.rabbitmq_config['vhost']

    def get_rabbitmq_queue(self) -> str:
        return self.rabbitmq_config['queue']
