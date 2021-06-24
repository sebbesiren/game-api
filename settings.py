from app.domain import DOMAIN

############################################
#
#   MongoDb
#
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'game_api'

# MONGO_URI=mongodb://127.0.0.1:27017/ada
# MONGO_DB=ada


############################################
#
#   EVE settings
#

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

############################################
#
#   Operations Log
#
OPLOG = True
OPLOG_ENDPOINT = "oplog"
OPLOG_RETURN_EXTRA_FIELD = True

############################################
#
#   Swagger
#
SWAGGER_INFO = {
    'title': 'GAME API',
    'version': '1.0',
    'description': 'GAME REST API',
    'termsOfService': 'Licensed according to...',
    'contact': {
        'name': 'Sebastian Nöbbelin',
        'url': 'https://nothing.com'
    },
    'license': {
        'name': 'Some License',
        'url': 'https://nothing.com',
    },
    'schemes': ['http', 'https'],
}

SWAGGER_SECURITY = {
    'securityDefinitions': {
        'BasicAuth': {
            'type': 'basic',
        },
        'ApiKeyAuth': {
            'type': 'apiKey',
            'name': 'X-API-Key',
            'in': 'header',
            'description': 'This is where you use the Token that is retrieved from the Authenticate Endpoints'
        }
    }
}
