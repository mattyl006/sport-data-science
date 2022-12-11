def timestamp_difference(tstamp1, tstamp2):
    tstamp1, tstamp2 = tstamp1.replace(':', ''), tstamp2.replace(':', '')
    tstamp1, tstamp2 = tstamp1.replace('.', ''), tstamp2.replace('.', '')
    return abs(int(tstamp2) - int(tstamp1))