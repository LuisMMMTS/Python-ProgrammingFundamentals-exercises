"""'

Define a function `alarm(hour, minutes)', ' that returns at what time the
alarm clock will ring, knowing that the current hour is `hour', ' and the
current minutes are `minutes', '. The clock goes off after 6 hour and 51
minutes.

'

"""

def alarm(hour,minutes):
    minutes=minutes+51
    if minutes>=60!=0:
        minutes-=60
        hour+=1
    hour+=6
    if hour>=24:
        hour-=24
    hour,minutes=str(hour),str(minutes)
    if len(hour)<2:
        hour="0"+hour
    if len(minutes)<2:
        minutes="0"+minutes
    return hour+":"+minutes