import pandas as pd

def evaluate_corner(corner, params):
    """Evaluate the corner and return a score."""
    score = 0
    corner = corner.apply(evaluate_event, axis=1, args=(params,))
      
    # Divide the sum of the scores by the number of passes
    if len(corner[corner['type'] == 'Pass']) == 0:
        score = corner['corner_score'].sum() * 2
    else:
        score = corner['corner_score'].sum() / len(corner[corner['type'] == 'Pass'])
    
    corner['score'] = score

    print(f'Corner score: {score:.2f} Period: {corner["period"].iloc[0]}, Time: {corner["minute"].iloc[0]}:{corner["second"].iloc[0]}, Team: {corner["team"].iloc[0]}')
    # TODO: consider corner length
    # TODO: iterate over events and evaluate each one

    return corner


def evaluate_event(event, params):
    """Evaluate the event and return a score."""
    if event['type'] == 'Pass':
        event['corner_score'] = evaluate_pass(event, params)
    elif event['type'] == 'Shot':
        event['corner_score'] = evaluate_shot(event, params)
    elif event['type'] == 'Clearance':
        event['corner_score'] = evaluate_clearance(event, params)
    elif event['type'] == 'Ball Recovery':
        event['corner_score'] = evaluate_ball_recovery(event, params)
    elif event['type'] == 'Foul Committed':
        event['corner_score'] = evaluate_foul_committed(event, params)
    else:
        event['corner_score'] = 0
    return event


def evaluate_pass(pass_, params):
    """Evaluate the pass and return a score."""
    score = 0
    """Consider the number of teammates and opponents in the end zone of the pass."""
    num_of_teammates_in_zone = 0
    num_of_opponents_in_zone = 0
    zone = get_end_zone(pass_['end_x'], pass_['end_y'])
    for location, teammate, actor in zip(pass_['context_locations'], pass_['teammate_locations'], pass_['actor_locations']):
        if not actor and teammate and get_end_zone(location[0], location[1]) == zone:
            num_of_teammates_in_zone += 1
        elif not actor and not teammate and get_end_zone(location[0], location[1]) == zone:
            num_of_opponents_in_zone += 1
    
    diff = num_of_teammates_in_zone - num_of_opponents_in_zone

    """Check if the pass is from the attacking team or the defending team."""
    if pass_['team'] == pass_['possession_team']:   
        if zone == "I":
            score += params['pass_to_zone_I']
        elif zone == "II":
            score += diff * params['pass_to_zone_II']
        else:
            score += diff * params['pass_to_zone_III']
    
        """Consider the outcome of the pass."""
        if pass_['event'].get('outcome') != None:
            if pass_['event'].get('outcome', {}).get('name') == 'Incomplete' or pass_['event'].get('outcome', {}).get('name') == 'Pass Offside':
                score += params['pass_incomplete']
    
        """Consider whether the pass is a shot assist."""
        if pass_['event'].get('shot_assist') != None:
            score += params['pass_shot_assist']
        elif pass_['event'].get('goal_assist') != None:
            score += params['pass_goal_assist']

        """Consider whether the pass is a cross."""
        if pass_['event'].get('cross') != None:
            score += params['pass_cross']
    
    
    elif pass_['team'] != pass_['possession_team']:
        score += params['pass_by_opponent']
            
    return score


def get_end_zone(x, y):
    """Return the end zone of the pass."""
    zone = ""
    match x, y:
        case _ if x < 48:
            zone = "I"
        case _ if 48 <= x < 84:
            zone = "II"
        case _ if y <= 16 and 84 <= x:
            zone = "LZ"
        case _ if y > 64 and 84 <= x:
            zone = "RZ"
        case _ if 16 <= y < 30 and 84 <= x < 102:
            zone = "LO"
        case _ if 30 <= y < 50 and 84 <= x < 102:
            zone = "CO"
        case _ if 50 <= y <= 64 and 84 <= x < 102:
            zone = "RO"
        case _ if 16 <= y < 30 and 102 <= x:
            zone = "LP"
        case _ if 50 <= y <= 64 and 102 <= x:
            zone = "RP"
        case _ if 30 <= y < 50 and 102 <= x:
            zone = "CP"
    return zone


def evaluate_shot(shot, params):
    """Evaluate the shot and return a score."""
    score = 0
    """Consider the outcome of the shot."""   
    if shot['event'].get('outcome') != None:
        outcome = shot['event'].get('outcome', {}).get('name') 
        if outcome == 'Goal':
            score += params['shot_goal']
        elif outcome == 'Saved':
            score += params['shot_saved']
        elif outcome == 'Blocked':
            score += params['shot_blocked']
        elif outcome == 'Off T':
            score += params['shot_off_target']
        elif outcome == 'Post':
            score += params['shot_post']
        elif outcome == 'Saved To Post':
            score += params['shot_saved_to_post']
        elif outcome == 'Saved Off T':
            score += params['shot_saved_off_target']
    return score

def evaluate_clearance(clearance, params):
    """Evaluate the clearance and return a score."""
    score = 0
    if clearance['team'] != clearance['possession_team']:
        score += params['clearance_by_opponent']
    return score


def evaluate_ball_recovery(ball_recovery, params):
    """Evaluate the ball recovery and return a score."""
    score = 0
    if ball_recovery['team'] == ball_recovery['possession_team']:
        score += params['ball_recovery_by_own_team']
    elif ball_recovery['team'] != ball_recovery['possession_team']:
        score += params['ball_recovery_by_opponent']
    return score

def evaluate_foul_committed(foul, params):
    """Evaluate the foul committed and return a score."""
    score = 0
    if foul['team'] == foul['possession_team']:
        score += params['foul_committed_by_own_team']

    elif foul['team'] != foul['possession_team']:
        score += params['foul_committed_by_opponent']
    return score


# TODO: dribbles, outcome of foul_committed (penalty, cards)

# TODO: consider carry, duel?

