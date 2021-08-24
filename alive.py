# Implement By - @anasty17 (https://github.com/SlamDevs/slam-mirrorbot/commit/0bfba523f095ab1dccad431d72561e0e002e7a59)
# (c) https://github.com/SlamDevs/slam-mirrorbot
# All rights reserved

import time
import requests
import os
from bot import HEROKU_APP_NAME 


IS_VPS = os.environ.get('IS_VPS', 'False')
if IS_VPS.lower() == 'true':
    IS_VPS = True
else:
    IS_VPS = False

if not IS_VPS and BASE_URL is not None:
    while True:
        time.sleep(1000)
        status = requests.get(f"http://{HEROKU_APP_NAME}.herokuapp.com").status_code
