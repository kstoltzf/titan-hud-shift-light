import pika

from shift_light import shift_light_service, config_service


class RabbitmqService(object):
    def __init__(self, shift_light_service: shift_light_service, config_service: config_service):
        self.shift_light_service = shift_light_service
        self.config_service = config_service

    def start(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.config_service.get_rabbitmq_host(),
                                      virtual_host=self.config_service.get_rabbitmq_vhost()))
        channel = connection.channel()
        channel.basic_consume(queue=self.config_service.get_rabbitmq_queue(),
                              on_message_callback=self.__process, auto_ack=True)
        channel.start_consuming()

    def __process(self, ch, method, properties, body) -> None:
        self.shift_light_service.toggle_lights(int(body))
