import pandas as pd

def evaluate_corner(corner):
    """Evaluate the corner and return a score."""
    # TODO: consider corner length
    # TODO: iterate over events and evaluate each one
    pass


def evaluate_event(event):
    """Evaluate the event and return a score."""
    if event['Type'] == 'pass':
        return evaluate_pass(event)
    # elif event['Type'] == 'shot':
    #     return evaluate_shot(event)


def evaluate_pass(pass_):
    """Evaluate the pass and return a score."""
    value = 0

    num_of_teammates_in_zone = 0
    num_of_opponents_in_zone = 0
    zone = get_end_zone(pass_['end_x'], pass_['end_y'])
    for location, teammate, actor in zip(pass_['context_locations'], pass_['teammate_locations'], pass_['actor_locations']):
        if not actor and teammate and get_end_zone(location[0], location[1]) == zone:
            num_of_teammates_in_zone += 1
        elif not actor and not teammate and get_end_zone(location[0], location[1]) == zone:
            num_of_opponents_in_zone += 1
    
    diff = num_of_teammates_in_zone - num_of_opponents_in_zone
    value += diff * 0.5

    # TODO: consider the outcome of the pass (ball receipt, shot, etc.)
    # TODO: consider other factors of the pass

            
    print(f"num_of_teammates_in_zone: {num_of_teammates_in_zone}")
    print(f"num_of_opponents_in_zone: {num_of_opponents_in_zone}")
    return value

def get_end_zone(x, y):
    """Return the end zone of the pass."""
    zone = ""
    match x, y:
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
    pass


