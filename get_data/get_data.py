from statsbombpy import sb

def get_competitions():
    return sb.competitions()

def get_matches(c_id, s_id):
    matches = sb.matches(competition_id=c_id, season_id=s_id)
    return matches

def get_events(e_name, m_id):
    events = sb.events(match_id=m_id, split=True, flatten_attrs=False)
    return events[e_name]
