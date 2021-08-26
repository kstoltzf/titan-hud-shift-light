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


if __name__ == '__main__':
    unittest.main()
