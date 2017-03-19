from slackbot.bot import listen_to

@listen_to('lock')
def lock_door(message):
    message.reply('The door is locked.')

@listen_to('open')
def lock_door(message):
    message.reply('The door is opened.')
