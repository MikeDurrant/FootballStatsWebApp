import pandas as pd
import plotly.graph_objs as go
from statsbombpy import sb

    
def return_figures():
    # create dataframe of events from the specific match (England v Croatia semi-final of 2018 World cup - id 8656)
    events = sb.events(match_id=8656)

    # create sub dataframe for player events
    player_events = events[['player', 'type', 'team', 'position']]

    # further subfilter to show only type == 'Pass'
    player_passes = player_events[player_events['type'] == 'Pass']

    # split into two dataframes - one for each team
    player_passes_eng = player_passes[player_passes['team'] == "England"]
    player_passes_cro = player_passes[player_passes['team'] == "Croatia"]

    # create groupby dataframe for each team to ready data for graphs
    df_eng = player_passes_eng.groupby(['player', 'team', 'position']).count().sort_values('type', ascending=False).reset_index()
    df_cro = player_passes_cro.groupby(['player', 'team', 'position']).count().sort_values('type', ascending=False).reset_index()

    # prepare data for graph_one
    graph_one = []

    graph_one.append(
        go.Bar(
        x = df_eng.player.to_list(),
        y = df_eng.type.to_list(),
        ) 
        )

    layout_one = dict(title = 'England team Passes attempted by Player',
                    xaxis = dict(title = 'Player',),
                    yaxis = dict(title = 'Passes attempted by Player'),
                    margin = dict(b=200)
                    )

    # prepare data for graph_two
    graph_two = []

    graph_two.append(
        go.Bar(
        x = df_cro.player.to_list(),
        y = df_cro.type.to_list(),
        ) 
        )

    layout_two = dict(title = 'Croatia team Passes attempted by Player',
                    xaxis = dict(title = 'Player'),
                    yaxis = dict(title = 'Passes attempted by Player'),
                    margin = dict(b=200)
                    )

    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))

    return figures