import os

api_id = int(os.environ.get("API_ID", '27862677'))
api_hash = os.environ.get("API_HASH", '4b11dd648188731fb7c9bc8083e8791c')
bot_token = os.environ.get("BOT_TOKEN", '7129448604:AAHBtE1PZG2YGutDVNZ_pgH5E_1UNW9BsDo')




OWNER = int(os.environ.get("OWNER", '6594402123'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '5186250641,6436809802,7183515722,6959409818,6233170765').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
