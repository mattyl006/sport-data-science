def add_context(events, frames):
    newEvents = events
    context_locations = [frames.loc[frames['id'] == event_id]['location'].values for event_id in events.values]
    newEvents['context_locations'] = context_locations
    return newEvents