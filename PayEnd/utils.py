from config import GLOBAL_API_KEYS


# API keys quota overhaul
current_key_idx = 0


def get_API_key():
    return GLOBAL_API_KEYS[current_key_idx]


# iterate list in a circular fashion
def generate_new_API_key():
    global current_key_idx
    current_key_idx = (current_key_idx + 1) % len(GLOBAL_API_KEYS)
    return GLOBAL_API_KEYS[current_key_idx]
