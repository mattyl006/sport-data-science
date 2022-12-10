def add_context(events, frames):
    newEvents = events
    context_locations = [frames.loc[frames['id'] == event[0]]['location'].values for event in events.values]
    teammate_locations = [frames.loc[frames['id'] == event[0]]['teammate'].values for event in events.values]
    actor_locations = [frames.loc[frames['id'] == event[0]]['actor'].values for event in events.values]
    newEvents['context_locations'] = context_locations
    newEvents['teammate_locations'] = teammate_locations
    newEvents['actor_locations'] = actor_locations
    return newEvents