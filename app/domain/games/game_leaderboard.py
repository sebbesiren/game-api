game_leaderboards = {
    'item_title': 'Game-Leaderboard',
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
        'game_settings': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'game--settings',
                'embeddable': True
            }
        },
        'leaderboard': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'score': {
                        'type': 'number',
                        'required': True
                    },
                    'player': {
                        'type': 'objectid',
                        'required': True,
                        'excludes': ['unknown_player'],
                        'data_relation': {
                            'resource': 'users',
                            'embeddable': True
                        }
                    },
                    'unknown_player': {
                        'type': 'string',
                        'required': True,
                        'excludes': ['player']
                    }
                }
            }
        }
    }
}
