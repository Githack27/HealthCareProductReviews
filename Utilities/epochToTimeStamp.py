import datetime

def convert_epoch_to_datetime(epoch_timestamp):
    try:
        if isinstance(epoch_timestamp, (int)):
            if epoch_timestamp > 1000000000000:
                epoch_timestamp /= 1000
            return datetime.datetime.fromtimestamp(epoch_timestamp, tz=datetime.timezone.utc).isoformat()
        return epoch_timestamp
    except Exception as e:
        return epoch_timestamp