def get_none():
    return None

def flatten_dict(thing):
    if type(thing) == dict:
        return list(thing)

