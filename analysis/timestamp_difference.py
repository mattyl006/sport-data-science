from datetime import datetime

def timestamp_difference(tstamp1, tstamp2):
    tstamp1, tstamp2 = datetime.strptime(tstamp1, '%H:%M:%S.%f'), datetime.strptime(tstamp2, '%H:%M:%S.%f') 
    return (tstamp2 - tstamp1).total_seconds() * 1000