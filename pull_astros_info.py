import mlbgame as mlb
import datetime
from collections import namedtuple


def pull_score():
    today = datetime.datetime.now() - datetime.timedelta(hours=5)
    year = today.year
    month = today.month
    day = today.day
    games = mlb.game.scoreboard(year, month, day, home="Astros", away="Astros")

    if games:
        id = list(games.keys())[0]
        game=games[id]
        game_time = datetime.datetime.strptime(
            game['game_start_time'], '%I:%M%p')-datetime.timedelta(hours=1)
        if today.hour > game_time.hour or(game_time.hour == today.hour and today.minute >= game_time.minute):
            try:
                overview = mlb.game.overview(list(games.keys())[0])
                inning = overview['inning']
                if overview['top_inning']=='Y':
                    half = 'Top '
                else:
                    half = 'Bottom '
                game_status = half + inning
            except:
                game_status = game['game_status']
            return {
                'home': game['home_team'],
                'away': game['away_team'],
                'h_score': game['home_team_runs'],
                'a_score': game['away_team_runs'],
                'game_status': game['game_status']}
        else:
            return {
                'game_time': game_time.strftime('%I:%M%p'),
                'home': game['home_team'],
                'away': game['away_team']}
    else:
        while not games:
            today = today+datetime.timedelta(days=1)
            year  = today.year
            month = today.month
            day   = today.day
            games = mlb.game.scoreboard(
                year, month, day, home="Astros", away="Astros")

        game = games[list(games.keys())[0]]
        l = game['game_id'].split('_')[:3]
        game_date = '/'.join(l+(l.pop(0)))
        game_time = datetime.datetime.strptime(
            game['game_start_time'], '%I:%M%p')-datetime.timedelta(hours=1)
        return {
            'game_date': game_date,
            'game_time': game_time.strftime('%I:%M%p'),
            'home': game['home_team'],
            'away': game['away_team']}

#H# - A#
def interpret_score(pulled_score):
    game_info = namedtuple(
        'game_info',
        ['is_today', 'date_or_inning', 'home_team', 'away_team', 'score'])
    game_info.home_team = pulled_score['home']
    game_info.away_team = pulled_score['away']
    game_info.score = str(pulled_score.get('h_score', '0')
                          )+'-'+str(pulled_score.get('a_score', '0'))
    if pulled_score.get('game_date'):
        print("The game isn't today")
        game_info.is_today = 0
        game_info.date_or_inning = pulled_score.get('game_date')
    else:
        game_info.is_today = 1
        game_info.date_or_inning = pulled_score.get(
            'game_status')
        if game_info.date_or_inning == None:
            game_info.date_or_inning = pulled_score.get('game_time')
    print(game_info.date_or_inning)
    return game_info
