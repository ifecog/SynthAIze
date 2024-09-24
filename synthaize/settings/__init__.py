import os
from decouple import config

ENVIRONMENT = config('ENVIRONMENT', default='dev')

if ENVIRONMENT == 'dev':
    from .dev import *
else:
    from .prod import *