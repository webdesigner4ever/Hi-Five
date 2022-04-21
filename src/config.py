from os import getenv

PORT = int(getenv("PORT", 8086 ))
DEBUG = bool(getenv("DEBUG", True))

