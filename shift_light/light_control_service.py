from gpiozero import LED


class LightControlService(object):
    left_first_green_led: LED
    right_first_green_led: LED
    left_second_green_led: LED
    right_second_green_led: LED
    left_first_yellow_led: LED
    right_first_yellow_led: LED
    left_second_yellow_led: LED
    right_second_yellow_led: LED
    right_red_led: LED
    left_red_led: LED

    def activate_first_green_lights(self) -> None:
        self.left_first_green_led.on()
        self.right_first_green_led.on()

    def activate_second_green_lights(self) -> None:
        self.left_second_green_led.on()
        self.right_second_green_led.on()

    def activate_first_yellow_lights(self) -> None:
        self.left_first_yellow_led.on()
        self.right_first_yellow_led.on()

    def activate_second_yellow_lights(self) -> None:
        self.left_second_yellow_led.on()
        self.right_second_yellow_led.on()

    def activate_red_lights(self) -> None:
        self.left_red_led.on()
        self.right_red_led.on()

    def deactivate_first_green_lights(self) -> None:
        self.left_first_green_led.off()
        self.right_first_green_led.off()

    def deactivate_second_green_lights(self) -> None:
        self.left_second_green_led.off()
        self.right_second_green_led.off()

    def deactivate_first_yellow_lights(self) -> None:
        self.left_first_yellow_led.off()
        self.right_first_yellow_led.off()

    def deactivate_second_yellow_lights(self) -> None:
        self.left_second_yellow_led.off()
        self.right_second_yellow_led.off()

    def deactivate_red_lights(self) -> None:
        self.left_red_led.off()
        self.right_red_led.off()
