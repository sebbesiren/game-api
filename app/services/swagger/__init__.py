from eve_swagger import swagger, add_documentation
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config


class SwaggerService:
    swagger = None

    @staticmethod
    def init(app, domain):
        app.register_blueprint(swagger)
        add_documentation({
            'x-stuff': {'test': '1'}
        })
        SwaggerService.init_flask_swagger_ui(app)
        SwaggerService.add_security_definitions(app, domain)

        # TODO: Handle function endpoint conversion to swagger...

    @staticmethod
    def init_flask_swagger_ui(app):
        add_documentation({
            "schemes": [
                "http",
                "https"
            ]
        })
        base_url = '/docs'
        api_url = '/api-docs'
        api_urls = [
            {
                "name": "Game API - All",
                "url": "/api-docs"
            },
            {
                "name": "Game API - Game 1",
                "url": "/api-docs/game_1"
            },
            {
                "name": "Game API - Game 2",
                "url": "/api-docs/game_2"
            }
        ]
        swagger_ui_blueprint = get_swaggerui_blueprint(
            base_url=base_url,
            api_url=api_url,
            config={
                "app_name": "SN Game API",
                "docExpansion": "none",
                "urls": api_urls
            }
        )
        app.register_blueprint(
            blueprint=swagger_ui_blueprint,
            url_prefix=base_url
        )

    # TODO: http for development, https for other environments

    @staticmethod
    def add_security_definitions(app, domain):
        add_documentation(
            app.config["SWAGGER_SECURITY"]
        )

        for item in domain:
            if "resource_methods" in domain[item]:
                for method in domain[item]["resource_methods"]:
                    if method in ["GET", "POST", "PATCH", "PUT", "DELETE"]:
                        add_documentation({'paths': {f'/{item}': {method.lower(): {'security': [
                            {'ApiKeyAuth': []}
                        ]}}}})
            if "item_methods" in domain[item]:
                for method in domain[item]["item_methods"]:
                    if method in ["GET", "POST", "PATCH", "PUT", "DELETE"]:
                        item_id = domain[item]["item_title"].lower()
                        item_id = "{" + item_id + "Id}"
                        add_documentation(
                            {'paths': {f'/{item}/{item_id}': {method.lower(): {'security': [
                                {'ApiKeyAuth': []}
                            ]}}}})

        # doc = {
        #     "paths": {},
        #     "definitions": {}
        # }
        # for model in MODELS:
        #     doc["definitions"].update(cerberus_type_to_swagger_types(MODELS[model], model))
        # for r in routes:
        #     doc["paths"][f"/{r}"] = routes[r]["methods"]
        #
        # add_documentation(doc)

        # TODO: generate documentation (for function endpoints)
        # documentation = {
        #     'paths': {
        #         '/status':
        #             {'get':
        #                 {'parameters': [
        #                     {
        #                         'in': 'query',
        #                         'name': 'foobar',
        #                         'required': False,
        #                         'description': 'special query parameter',
        #                         'type': 'string'
        #                     }
        #                 ]
        #                 }
        #             }
        #     }
        # }
        # add_documentation(documentation)
