import json
from datetime import datetime, timedelta
import calendar

hora=datetime.now()
hoy=datetime.today().strftime('%A')
horario=json.loads(open("horario.json","r").read())

print(hora+hora)