import unittest

from shift_light import shift_light_service
from shift_light import light_control_service
from unittest.mock import MagicMock


class ShiftLightServiceTests(unittest.TestCase):
    light_control_service_test: light_control_service
    shift_light_service_test: shift_light_service

    def setUp(self) -> None:
        self.light_control_service_test = light_control_service.LightControlService()
        self.light_control_service_test.activate_first_green_lights = MagicMock()
        self.light_control_service_test.activate_second_green_lights = MagicMock()
        self.light_control_service_test.activate_first_yellow_lights = MagicMock()
        self.light_control_service_test.activate_second_yellow_lights = MagicMock()
        self.light_control_service_test.activate_red_lights = MagicMock()
        self.light_control_service_test.deactivate_first_green_lights = MagicMock()
        self.light_control_service_test.deactivate_second_green_lights = MagicMock()
        self.light_control_service_test.deactivate_first_yellow_lights = MagicMock()
        self.light_control_service_test.deactivate_second_yellow_lights = MagicMock()
        self.light_control_service_test.deactivate_red_lights = MagicMock()
        self.shift_light_service_test = shift_light_service.ShiftLightService(self.light_control_service_test)

    def test_toggle_lights_should_activate_first_green_lights_when_rpms_are_equal_to_4000(self):
        self.shift_light_service_test.toggle_lights(4000)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_not_called()
        self.light_control_service_test.activate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_first_green_lights_when_rpms_are_greater_than_4000(self):
        self.shift_light_service_test.toggle_lights(4100)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_not_called()
        self.light_control_service_test.activate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_second_green_lights_when_rpms_are_equal_to_4500(self):
        self.shift_light_service_test.toggle_lights(4500)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_second_green_lights_when_rpms_are_greater_than_4500(self):
        self.shift_light_service_test.toggle_lights(4600)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_first_yellow_lights_when_rpms_are_equal_to_5000(self):
        self.shift_light_service_test.toggle_lights(5000)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_first_yellow_lights_when_rpms_are_greater_than_5000(self):
        self.shift_light_service_test.toggle_lights(5001)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_second_yellow_lights_when_rpms_are_equal_to_5500(self):
        self.shift_light_service_test.toggle_lights(5500)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_second_yellow_lights_when_rpms_are_greater_than_5500(self):
        self.shift_light_service_test.toggle_lights(5600)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_red_lights.assert_not_called()

    def test_toggle_lights_should_activate_red_lights_when_rpms_are_equal_to_6000(self):
        self.shift_light_service_test.toggle_lights(6000)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_red_lights.assert_called_once()

    def test_toggle_lights_should_activate_red_lights_when_rpms_are_greater_than_6000(self):
        self.shift_light_service_test.toggle_lights(6200)

        self.light_control_service_test.activate_first_green_lights.assert_called_once()
        self.light_control_service_test.activate_second_green_lights.assert_called_once()
        self.light_control_service_test.activate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.activate_red_lights.assert_called_once()

    def test_toggle_lights_should_deactivate_first_green_lights_when_rpms_are_less_than_4000(self):
        self.shift_light_service_test.toggle_lights(3999)

        self.light_control_service_test.deactivate_first_green_lights.assert_called_once()
        self.light_control_service_test.deactivate_second_green_lights.assert_called_once()
        self.light_control_service_test.deactivate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_red_lights.assert_called_once()

    def test_toggle_lights_should_deactivate_second_green_lights_when_rpms_are_less_than_4500(self):
        self.shift_light_service_test.toggle_lights(4400)

        self.light_control_service_test.deactivate_first_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_green_lights.assert_called_once()
        self.light_control_service_test.deactivate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_red_lights.assert_called_once()

    def test_toggle_lights_should_deactivate_first_yellow_lights_when_rpms_are_less_than_5000(self):
        self.shift_light_service_test.toggle_lights(4900)

        self.light_control_service_test.deactivate_first_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_first_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_red_lights.assert_called_once()

    def test_toggle_lights_should_deactivate_second_yellow_lights_when_rpms_are_less_than_5500(self):
        self.shift_light_service_test.toggle_lights(5400)

        self.light_control_service_test.deactivate_first_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_yellow_lights.assert_called_once()
        self.light_control_service_test.deactivate_red_lights.assert_called_once()

    def test_toggle_lights_should_deactivate_red_lights_when_rpms_are_less_than_6000(self):
        self.shift_light_service_test.toggle_lights(5900)

        self.light_control_service_test.deactivate_first_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_green_lights.assert_not_called()
        self.light_control_service_test.deactivate_first_yellow_lights.assert_not_called()
        self.light_control_service_test.deactivate_second_yellow_lights.assert_not_called()
        self.light_control_service_test.deactivate_red_lights.assert_called_once()


if __name__ == '__main__':
    unittest.main()
