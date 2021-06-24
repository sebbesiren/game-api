from eve import Eve
from app.domain import DOMAIN
from app.services import Services
from config import Config


def create_app():
    app = Eve()
    Services.init_services(app=app, domain=DOMAIN)

    return app
