from app.services.swagger import SwaggerService


class Services:
    Swagger = None

    @staticmethod
    def init_services(app, domain):
        # TODO: read from file system and init them...
        Services.Swagger = SwaggerService.init(app, domain)
