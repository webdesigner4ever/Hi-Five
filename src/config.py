from os import getenv

key = iv = "65ea2fdd64feb80476268568a2c14613"
PORT = int(getenv("PORT", 8086 ))
DEBUG = bool(getenv("DEBUG", True))

