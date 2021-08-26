import unittest

from shift_light import config_service


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.config_service = config_service.ConfigService('test.ini')

    def test_get_rabbitmq_host_returns_expected_value(self):
        host = self.config_service.get_rabbitmq_host()

        self.assertEqual('test_host', host)

    def test_get_rabbitmq_vhost_returns_expected_value(self):
        vhost = self.config_service.get_rabbitmq_vhost()

        self.assertEqual('test_vhost', vhost)

    def test_get_rabbitmq_queue_returns_expected_value(self):
        queue = self.config_service.get_rabbitmq_queue()

        self.assertEqual('test_queue', queue)

    def test_get_first_green_lights_threshold(self):
        value = self.config_service.get_first_green_lights_threshold()

        self.assertEqual(4000, value)

    def test_get_second_green_lights_threshold(self):
        value = self.config_service.get_second_green_lights_threshold()

        self.assertEqual(4500, value)

    def test_get_first_yellow_lights_threshold(self):
        value = self.config_service.get_first_yellow_lights_threshold()

        self.assertEqual(5000, value)

    def test_get_second_yellow_lights_threshold(self):
        value = self.config_service.get_second_yellow_lights_threshold()

        self.assertEqual(5500, value)

    def test_get_red_lights_threshold(self):
        value = self.config_service.get_red_lights_threshold()

        self.assertEqual(6000, value)


if __name__ == '__main__':
    unittest.main()
