from shift_light import light_control_service


class ShiftLightService(object):
    def __init__(self, light_activation_service_initializer: light_control_service):
        self.light_activation_service = light_activation_service_initializer

    def toggle_lights(self, rpms: int) -> None:
        self.__activate_lights(rpms)
        self.__deactivate_lights(rpms)

    def __activate_lights(self, rpms: int) -> None:
        if rpms >= 4000:
            self.light_activation_service.activate_first_green_lights()
        if rpms >= 4500:
            self.light_activation_service.activate_second_green_lights()
        if rpms >= 5000:
            self.light_activation_service.activate_first_yellow_lights()
        if rpms >= 5500:
            self.light_activation_service.activate_second_yellow_lights()
        if rpms >= 6000:
            self.light_activation_service.activate_red_lights()

    def __deactivate_lights(self, rpms: int) -> None:
        if rpms < 6000:
            self.light_activation_service.deactivate_red_lights()
        if rpms < 5500:
            self.light_activation_service.deactivate_second_yellow_lights()
        if rpms < 5000:
            self.light_activation_service.deactivate_first_yellow_lights()
        if rpms < 4500:
            self.light_activation_service.deactivate_second_green_lights()
        if rpms < 4000:
            self.light_activation_service.deactivate_first_green_lights()
