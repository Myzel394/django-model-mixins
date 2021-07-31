import string

__all__ = [
    "DEFAULT_RANDOM_ID_MAX_LENGTH", "DEFAULT_RANDOM_ID_CHARS"
]

DEFAULT_RANDOM_ID_MAX_LENGTH = 1023
DEFAULT_RANDOM_ID_CHARS = string.ascii_letters + string.digits
