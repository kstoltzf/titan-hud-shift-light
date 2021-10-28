import unittest
from unittest.mock import patch, MagicMock, ANY

import pika

from shift_light import rabbitmq_service, light_control_service, shift_light_service, config_service


class RabbitMqServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config_service_test = config_service.ConfigService('./tests/test.ini')
        self.light_control_service_test = light_control_service.LightControlService(self.config_service_test, True)
        self.shift_light_service_test = shift_light_service.ShiftLightService(self.light_control_service_test,
                                                                              self.config_service_test)
        self.rabbitmq_service_test = \
            rabbitmq_service.RabbitmqService(self.shift_light_service_test, self.config_service_test)

    @patch('pika.BlockingConnection')
    def test_start_starts_consuming_messages(self, mock_blocking_connection):
        mock_channel = MagicMock()
        mock_blocking_connection.return_value.channel.return_value = mock_channel
        expected_connection_parameters = pika.ConnectionParameters(host='test_host', virtual_host='test_vhost')

        self.rabbitmq_service_test.start()

        mock_blocking_connection.assert_called_once_with(expected_connection_parameters)
        mock_channel.basic_consume.assert_called_with(queue='test_queue', on_message_callback=ANY, auto_ack=True)
        mock_channel.start_consuming.assert_called_once()


if __name__ == '__main__':
    unittest.main()
