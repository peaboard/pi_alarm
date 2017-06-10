import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
PIN = 10                       # Pin to which the PowerSwitch Tail is connected
ALARM_DURATION = 1            # Light duration in minutes
PIR = 4 					   # Pin to which PIR sensor or Switch is connected

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = False
BASIC_AUTH_USERNAME = 'alarm'
BASIC_AUTH_PASSWORD = 'password'

'''
This throws an error as the pir_alarm(Actual file that runs the alarm)
searches for it in its own directory (app)
For now copied fortunes to both this directory and the app directory,
but it is a very cheap workaround.
The fortunes function should be in a separate file. Not config.
'''
currdir = os.getcwd()
print(currdir)
msg = open("fortunes", "r")
MESSAGES = []
fortunes = msg.read()
# Convert text to utf, something to do with the fortunes file we use
for line in fortunes.decode('utf-8').split('%'):
	MESSAGES.append(line)


# -- Custom Happy Messages
# MESSAGES = [
#     "Love you!",
#     "You're smart AND pretty!",
#     "You have a winning smile!",
#     "You're home now; kick back and relax!",
#     "Don't forget: Andrew loves you!",
#     "What's for breakfast?",
#     "Show those kids who's boss!",
#     "Grab a stuffed animal or husband, because it's time to cuddle!",
#     "Honey, did you just fart?",
#     "Did you lock the front door?",
#     "I'm glad we got married!",
#     "Thanks for putting up with me <3",
#     "Violets are blue, roses are red. Turn off that light because it's time for bed!",
#     "If you're happy and you know it go to sleep!",
#     "Poo Poo on the Motley Crew",
#     "A hug! A hug! My kingdom for a hug!",
#     "Did you get your bedtime kiss yet?",
#     "You have a lovely voice! But be quiet now because it's time for bed.",
#     "A penny saved is a penny earned. Too bad Andrew's spending all your pennies on his startup!",
#     "Do you think Tinkerbell can cast Wingardium Leviosa?",
#     "Country fried steak or Chicken fried steak. What's the difference?",
#     "I want a Tesla. Too bad I don't drive much anymore. Or have any money.",
#     "Andrew loves you!",
#     "Ziggy loves you, too!"
# ]
