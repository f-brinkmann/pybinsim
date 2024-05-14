from pathlib import Path


def parse_soundfile_list(soundfile_list: str) -> list[Path]:
    """Parse a soundfile list separated by '#' to a list of paths"""
    if soundfile_list:
        return list(map(Path, soundfile_list.split('#')))
    else:
        return list()


def parse_boolean(input):
    if type(input) == str:
        if input.lower() == 'true':
            return True
        if input.lower() == 'false':
            return False
    elif type(input) == bool:
        return input
    elif type(input) == int:
        return input != 0 # same as bool(input)
    else:
        return None

def parse_channel_list(channel_list: str) -> list[int]:
    """Parse a string of integers separated by ',' to a list of ints"""
    if channel_list:
        return list(map(int, channel_list.split(',')))
    else:
        return list()