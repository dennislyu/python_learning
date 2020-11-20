import time
from datetime import datetime

ts = time.time() # AWS Lightsail uses UTC timezone
dt = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
filename = "{}.txt".format(dt)
with open('/home/dennis/crontab_test/{}'.format(filename), 'w', encoding='UTF-8') as file:
  file.write('Created at {}'.format(dt))
