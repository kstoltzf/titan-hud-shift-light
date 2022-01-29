import unittest

from shift_light import config_service


class ConfigServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config_service_test = config_service.ConfigService('./tests/test.ini')

    def test_get_rabbitmq_host_returns_expected_value(self):
        host = self.config_service_test.get_rabbitmq_host()

        self.assertEqual('test_host', host)

    def test_get_rabbitmq_vhost_returns_expected_value(self):
        vhost = self.config_service_test.get_rabbitmq_vhost()

        self.assertEqual('test_vhost', vhost)

    def test_get_rabbitmq_queue_returns_expected_value(self):
        queue = self.config_service_test.get_rabbitmq_queue()

        self.assertEqual('test_queue', queue)

    def test_get_first_green_lights_threshold_returns_expected_value(self):
        value = self.config_service_test.get_first_green_lights_threshold()

        self.assertEqual(4000, value)

    def test_get_second_green_lights_threshold_returns_expected_value(self):
        value = self.config_service_test.get_second_green_lights_threshold()

        self.assertEqual(4500, value)

    def test_get_first_yellow_lights_threshold_returns_expected_value(self):
        value = self.config_service_test.get_first_yellow_lights_threshold()

        self.assertEqual(5000, value)

    def test_get_second_yellow_lights_threshold_returns_expected_value(self):
        value = self.config_service_test.get_second_yellow_lights_threshold()

        self.assertEqual(5500, value)

    def test_get_red_lights_threshold_returns_expected_value(self):
        value = self.config_service_test.get_red_lights_threshold()

        self.assertEqual(6000, value)

    def test_get_left_first_green_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_left_first_green_led_pin()

        self.assertEqual(1, pin)

    def test_get_right_first_green_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_right_first_green_led_pin()

        self.assertEqual(2, pin)

    def test_get_left_second_green_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_left_second_green_led_pin()

        self.assertEqual(3, pin)

    def test_get_right_second_green_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_right_second_green_led_pin()

        self.assertEqual(4, pin)

    def test_get_left_first_yellow_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_left_first_yellow_led_pin()

        self.assertEqual(5, pin)

    def test_get_right_first_yellow_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_right_first_yellow_led_pin()

        self.assertEqual(6, pin)

    def test_get_left_second_yellow_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_left_second_yellow_led_pin()

        self.assertEqual(7, pin)

    def test_get_right_second_yellow_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_right_second_yellow_led_pin()

        self.assertEqual(8, pin)

    def test_get_left_red_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_left_red_led_pin()

        self.assertEqual(9, pin)

    def test_get_right_red_led_pin_returns_expected_value(self):
        pin = self.config_service_test.get_right_red_led_pin()

        self.assertEqual(10, pin)


if __name__ == '__main__':
    unittest.main()
