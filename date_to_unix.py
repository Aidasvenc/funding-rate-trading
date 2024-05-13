import datetime



def date_to_unix(date_str, date_format='%Y-%m-%d %H:%M:%S'):
    """
    Converts a date string with time into a UNIX timestamp.

    Args:
        date_str (str): The date and time in string format.
        date_format (str): The format of the date string, default is '%Y-%m-%d %H:%M:%S'.

    Returns:
        int: UNIX timestamp representing the given date and time.
    """
    # Convert the date string to a datetime object
    date_obj = datetime.datetime.strptime(date_str, date_format)
    # Convert the datetime object to a UNIX timestamp
    unix_timestamp = int(date_obj.timestamp())

    return unix_timestamp

def unix_to_date(unix_timestamp):
    # UNIX timestamp
    timestamp = int(unix_timestamp)

    # Convert UNIX timestamp to a datetime object
    date_time = datetime.datetime.fromtimestamp(timestamp)

    # Format the datetime object as a string in a human-readable format
    formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date