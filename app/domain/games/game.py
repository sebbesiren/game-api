from config import Config

games = {
    'item_title': 'Game',
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH'],
    'schema': {
        'name': {
            'type': 'string',
            'allowed': Config.GAMES,
            'unique': True,
            'required': True
        },
        'game_settings': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'game--settings',
                'embeddable': True
            }
        },
        'description': {
            'type': 'string'
        }
    }
}
