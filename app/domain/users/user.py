from app.helpers.regex_helper import RegexHelper

users = {
    'item_title': 'User',
    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            'regex': RegexHelper.USERNAME
        },
        'email': {
            'type': 'string',
            'unique': True,
            'regex': RegexHelper.EMAIL_ADDRESS
        },
        'password': {
            'type': 'string',
        },
        'role': {
            'type': 'string',
            'allowed': ['admin', 'player']
        },
        'access_right': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'access--rights',
                'embeddable': True
            }
        }
    }
}
