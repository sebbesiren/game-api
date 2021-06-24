from config import Config

game_settings = {
    'item_title': 'Game-Settings',
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH'],
    'schema': {
        'game': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'games',
                'embeddable': True
            }
        },
        'generic_settings': {
            'type': 'dict',
            'schema': {
                'lives': {
                    'type': 'number'
                },
            }
        }
    }
}
