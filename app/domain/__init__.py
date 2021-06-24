from app.domain.access_groups.access_group import access_groups
from app.domain.games.game import games
from app.domain.games.game_leaderboard import game_leaderboards
from app.domain.games.game_settings import game_settings
from app.domain.users.user import users

DOMAIN = {
    'users': users,

    'access--groups': access_groups,

    'games': games,
    'game--leaderboard': game_leaderboards,
    'game--settings': game_settings
}
