from shift_light import light_control_service, config_service


class ShiftLightService(object):
    def __init__(self, light_control_service: light_control_service, config_service: config_service):
        self.light_control_service = light_control_service
        self.config_service = config_service

    def toggle_lights(self, rpms: int) -> None:
        self.__activate_lights(rpms)
        self.__deactivate_lights(rpms)

    def __activate_lights(self, rpms: int) -> None:
        if rpms >= self.config_service.get_first_green_lights_threshold():
            self.light_control_service.activate_first_green_lights()
        if rpms >= self.config_service.get_second_green_lights_threshold():
            self.light_control_service.activate_second_green_lights()
        if rpms >= self.config_service.get_first_yellow_lights_threshold():
            self.light_control_service.activate_first_yellow_lights()
        if rpms >= self.config_service.get_second_yellow_lights_threshold():
            self.light_control_service.activate_second_yellow_lights()
        if rpms >= self.config_service.get_red_lights_threshold():
            self.light_control_service.activate_red_lights()

    def __deactivate_lights(self, rpms: int) -> None:
        if rpms < self.config_service.get_red_lights_threshold():
            self.light_control_service.deactivate_red_lights()
        if rpms < self.config_service.get_second_yellow_lights_threshold():
            self.light_control_service.deactivate_second_yellow_lights()
        if rpms < self.config_service.get_first_yellow_lights_threshold():
            self.light_control_service.deactivate_first_yellow_lights()
        if rpms < self.config_service.get_second_green_lights_threshold():
            self.light_control_service.deactivate_second_green_lights()
        if rpms < self.config_service.get_first_green_lights_threshold():
            self.light_control_service.deactivate_first_green_lights()
