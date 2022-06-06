def validate_name(name, max_length):
    if len(name) > max_length:
        name = name[:max_length]
    return name
