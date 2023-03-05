import pandas as pd

def evaluate_corner(corner):
    """Evaluate the corner and return a score."""
    score = 0

    corner = corner.apply(evaluate_event, axis=1)
    
    # TODO: consider corner length    
    # Divide the sum of the scores by the number of passes
    score = corner['corner_score'].sum() / len(corner[corner['type'] == 'Pass'])
    
    #Print the score
    print(f'Corner score: {score:.2f}')
    return corner


def evaluate_event(event):
    """Evaluate the event and return a score."""
    if event['type'] == 'Pass':
        event['corner_score'] = evaluate_pass(event)

    elif event['type'] == 'Shot':
        event['corner_score'] = evaluate_shot(event)

    else:
        event['corner_score'] = 0
    return event

def evaluate_pass(pass_):
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
            score -= 0.8
        elif zone == "II":
            score += diff * 0.1
        else:
            score += diff * 0.2
    
        """Consider the outcome of the pass."""
        if pass_['event'].get('outcome') != None:
            if pass_['event'].get('outcome', {}).get('name') == 'Incomplete' or pass_['event'].get('outcome', {}).get('name') == 'Pass Offside':
                score -= 0.5
    
        """Consider whether the pass is a shot assist."""
        if pass_['event'].get('shot_assist') != None:
            score += 0.4
        elif pass_['event'].get('goal_assist') != None:
            score += 0.6

        """Consider whether the pass is a cross."""
        if pass_['event'].get('cross') != None:
            score += 0.2
    
    
    elif pass_['team'] != pass_['possession_team']:
        score -= 0.5
        
    
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


def evaluate_shot(shot):
    """Evaluate the shot and return a score."""
    score = 0
    """Consider the outcome of the shot."""
   
    if shot['event'].get('outcome') != None:
        outcome = shot['event'].get('outcome', {}).get('name') 
        if outcome == 'Goal':
            score += 2
        elif outcome == 'Saved':
            score += 1
        elif outcome == 'Blocked':
            score += 0.5
        elif outcome == 'Off T':
            score += 0.5
        elif outcome == 'Post':
            score += 1
        elif outcome == 'Saved To Post':
            score += 1
        elif outcome == 'Saved Off T':
            score += 0.5
    return score

# TODO: consider faul commited (with penalty), clearance, ball recovery, duel, dribbles

# TODO: consider carry?

