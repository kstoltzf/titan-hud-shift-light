import os
import sys

from shift_light import shift_light_service, light_control_service, rabbitmq_service, config_service


def main(rabbitmq_service: rabbitmq_service):
    rabbitmq_service.start()


if __name__ == '__main__':
    config_service = config_service.ConfigService('../config.ini')
    light_control_service = light_control_service.LightControlService()
    shift_light_service = shift_light_service.ShiftLightService(light_control_service)
    rabbitmq_service = rabbitmq_service.RabbitmqService(shift_light_service, config_service)
    try:
        main(rabbitmq_service)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)