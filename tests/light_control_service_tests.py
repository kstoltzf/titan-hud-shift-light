import unittest

from gpiozero import LED, Device
from gpiozero.pins.mock import MockFactory

from shift_light import light_control_service


class LightControlServiceTests(unittest.TestCase):
    light_control_service_test: light_control_service

    def setUp(self) -> None:
        self.light_control_service_test = light_control_service.LightControlService()

        Device.pin_factory = MockFactory()
        self.light_control_service_test.left_first_green_led = LED(1)
        self.light_control_service_test.right_first_green_led = LED(2)
        self.light_control_service_test.left_second_green_led = LED(3)
        self.light_control_service_test.right_second_green_led = LED(4)
        self.light_control_service_test.left_first_yellow_led = LED(5)
        self.light_control_service_test.right_first_yellow_led = LED(6)
        self.light_control_service_test.left_second_yellow_led = LED(7)
        self.light_control_service_test.right_second_yellow_led = LED(8)
        self.light_control_service_test.left_red_led = LED(9)
        self.light_control_service_test.right_red_led = LED(10)

    def test_activate_first_green_lights_activates_both_first_green_lights(self):
        self.light_control_service_test.left_first_green_led.off()
        self.light_control_service_test.right_first_green_led.off()

        self.light_control_service_test.activate_first_green_lights()

        self.assertEqual(True, self.light_control_service_test.left_first_green_led.is_active)
        self.assertEqual(True, self.light_control_service_test.right_first_green_led.is_active)

    def test_activate_second_green_lights_activates_both_second_green_lights(self):
        self.light_control_service_test.left_second_green_led.off()
        self.light_control_service_test.right_second_green_led.off()

        self.light_control_service_test.activate_second_green_lights()

        self.assertEqual(True, self.light_control_service_test.left_second_green_led.is_active)
        self.assertEqual(True, self.light_control_service_test.right_second_green_led.is_active)

    def test_activate_first_yellow_lights_activates_both_first_yellow_lights(self):
        self.light_control_service_test.left_first_yellow_led.off()
        self.light_control_service_test.right_first_yellow_led.off()

        self.light_control_service_test.activate_first_yellow_lights()

        self.assertEqual(True, self.light_control_service_test.left_first_yellow_led.is_active)
        self.assertEqual(True, self.light_control_service_test.right_first_yellow_led.is_active)

    def test_activate_second_yellow_lights_activates_both_second_yellow_lights(self):
        self.light_control_service_test.left_second_yellow_led.off()
        self.light_control_service_test.right_second_yellow_led.off()

        self.light_control_service_test.activate_second_yellow_lights()

        self.assertEqual(True, self.light_control_service_test.left_second_yellow_led.is_active)
        self.assertEqual(True, self.light_control_service_test.right_second_yellow_led.is_active)

    def test_activate_red_lights_activates_both_red_lights(self):
        self.light_control_service_test.left_red_led.off()
        self.light_control_service_test.right_red_led.off()

        self.light_control_service_test.activate_red_lights()

        self.assertEqual(True, self.light_control_service_test.left_red_led.is_active)
        self.assertEqual(True, self.light_control_service_test.right_red_led.is_active)

    def test_deactivate_first_green_lights_deactivates_both_first_green_lights(self):
        self.light_control_service_test.left_first_green_led.on()
        self.light_control_service_test.right_first_green_led.on()

        self.light_control_service_test.deactivate_first_green_lights()

        self.assertEqual(False, self.light_control_service_test.left_first_green_led.is_active)
        self.assertEqual(False, self.light_control_service_test.right_first_green_led.is_active)

    def test_deactivate_second_green_lights_deactivates_both_second_green_lights(self):
        self.light_control_service_test.left_second_green_led.on()
        self.light_control_service_test.right_second_green_led.on()

        self.light_control_service_test.deactivate_second_green_lights()

        self.assertEqual(False, self.light_control_service_test.left_second_green_led.is_active)
        self.assertEqual(False, self.light_control_service_test.right_second_green_led.is_active)

    def test_deactivate_first_yellow_lights_deactivates_both_first_yellow_lights(self):
        self.light_control_service_test.left_first_yellow_led.on()
        self.light_control_service_test.right_first_yellow_led.on()

        self.light_control_service_test.deactivate_first_yellow_lights()

        self.assertEqual(False, self.light_control_service_test.left_first_yellow_led.is_active)
        self.assertEqual(False, self.light_control_service_test.right_first_yellow_led.is_active)

    def test_deactivate_second_yellow_lights_deactivates_both_second_yellow_lights(self):
        self.light_control_service_test.left_second_yellow_led.on()
        self.light_control_service_test.right_second_yellow_led.on()

        self.light_control_service_test.deactivate_second_yellow_lights()

        self.assertEqual(False, self.light_control_service_test.left_second_yellow_led.is_active)
        self.assertEqual(False, self.light_control_service_test.right_second_yellow_led.is_active)

    def test_deactivate_red_lights_deactivates_both_red_lights(self):
        self.light_control_service_test.left_red_led.on()
        self.light_control_service_test.right_red_led.on()

        self.light_control_service_test.deactivate_red_lights()

        self.assertEqual(False, self.light_control_service_test.left_red_led.is_active)
        self.assertEqual(False, self.light_control_service_test.right_red_led.is_active)

    def tearDown(self) -> None:
        self.light_control_service_test.left_first_green_led.close()
        self.light_control_service_test.right_first_green_led.close()
        self.light_control_service_test.left_second_green_led.close()
        self.light_control_service_test.right_second_green_led.close()
        self.light_control_service_test.left_first_yellow_led.close()
        self.light_control_service_test.right_first_yellow_led.close()
        self.light_control_service_test.left_second_yellow_led.close()
        self.light_control_service_test.right_second_yellow_led.close()
        self.light_control_service_test.left_red_led.close()
        self.light_control_service_test.right_red_led.close()

if __name__ == '__main__':
    unittest.main()
