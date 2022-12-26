import telegram
from telegram import user
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import messages as ms
import subprocess
import signal
import os

my_token   = 0
admin_uid  = 0

def bmon_get():
    output = subprocess.check_output("sh mizun.sh", shell=True)
    output2 = output.decode("utf-8")
    #print(output2)
    
    output3 = output2.split("\n")[0].split(" ")
    #print(output3)
    
    RX = output3[0]
    TX = output3[1]
    
    #print(type(RX))
    #print(type(TX))
    
    #print(RX, " ", RX[-3], " ", RX[:-3], float(RX[:-3]))
    #print(TX, " ", TX[-3], " ", TX[:-3], float(TX[:-3]))
    
    try:
        if(RX[-3] == 'K'):
            _RX = float(RX[:-3]) / 1024 / 1024
        elif(RX[-3] == 'M'):
            _RX = float(RX[:-3]) / 1024
        elif(RX[-3] == 'G'):
            _RX = float(RX[:-3])
        elif(RX[-3] == 'T'):
            _RX = float(RX[:-3]) * 1024
    except Exception as e:
        print(e)
    
    try:
        if(TX[-3] == 'K'):
            _TX = float(TX[:-3]) / 1024 / 1024
        elif(TX[-3] == 'M'):
            _TX = float(TX[:-3]) / 1024
        elif(TX[-3] == 'G'):
            _TX = float(TX[:-3])
        elif(TX[-3] == 'T'):
            _TX = float(TX[:-3]) * 1024
    except Exception as e:
        print(e)
    
    #print(_RX)
    #print(_TX)
    
    return RX[:-3] + " " + RX[-3] + "iB", TX[:-3] + " " + TX[-3] + "iB", round(_TX/_RX, 2)

def dd_upload(count, speed, host):
    try:
        #upload_cmd = 'dd if=/dev/urandom bs=1024000 count=$ | pv -q -L @ | nc -u ^ 53'.replace("$", count).replace("@", speed).replace("^", host)
        #output = subprocess.call(upload_cmd, shell=True)
        #print(output)
        output = subprocess.check_output("sh mizun2.sh " + str(count) + " " + str(speed) + " " + str(host), shell=True)
        output2 = output.decode("utf-8")
        print(output2)
        return 1
    except Exception as e:
        print(e)
        return 0

def start(bot, update):
    inCome_uid, inCome_name, inCome_user_id = exctract_info(update.message.from_user)
    try:
        if int(inCome_uid) in allowed_users:
            send_text(int(inCome_uid), ms.start)
        else:
            send_text(int(inCome_uid), ms.not_athorized)
            send_text(admin_uid, ms.fozool_detected + '\n' + inCome_user_id + '\n' + inCome_name)
    except Exception as e:
        print(e)

def get_stat(bot, update, args):
    inCome_uid, inCome_name, inCome_user_id = exctract_info(update.message.from_user)
    try:
        if int(inCome_uid) in allowed_users:
            if args!=[]:
                send_text(int(inCome_uid), ms.no_arg)
            else:
                RX, TX, Rate = bmon_get()
                send_text(int(inCome_uid), ms.traffic.replace("&", str(TX)).replace("%", str(RX)).replace("$", str(Rate)))
        else:
            send_text(int(inCome_uid), ms.not_athorized)
            send_text(admin_uid, ms.fozool_detected + '\n' + inCome_user_id + '\n' + inCome_name)
    except Exception as e:
        print(e)

def upload(bot, update, args):
    inCome_uid, inCome_name, inCome_user_id = exctract_info(update.message.from_user)
    try:
        if int(inCome_uid) in allowed_users:
            if args!=[]:
                count = args[0]
                speed = args[1]
                try:
                    host  = args[2]
                except:
                    host = 'epicgames.com'
                print(count, " ", speed, " ", host)
                if(dd_upload(count, speed, host)==1):
                    print("done")
                    send_text(int(inCome_uid), ms.done)
                else:
                    print("error")
                    send_text(int(inCome_uid), ms.upload_error)
            else:
                send_text(int(inCome_uid), ms.no_arg)
        else:
            send_text(int(inCome_uid), ms.not_athorized)
            send_text(admin_uid, ms.fozool_detected + '\n' + inCome_user_id + '\n' + inCome_name)
    except Exception as e:
        print(e)

def exctract_info(chat_id):
    inCome_uid = str(chat_id['id'])
    inCome_user_id = chat_id['username']
    if inCome_user_id==None:
        inCome_user_id='None'
    first_name = chat_id['first_name']
    last_name = chat_id['last_name']
    if first_name==None:
        first_name = ''
    if last_name==None:
        last_name = ''
    else:
        last_name = ' ' + last_name
    inCome_name = first_name + last_name
    return inCome_uid, inCome_name, inCome_user_id

def send_photo(uid,msg,adrs):
    try:
        bot.sendChatAction(uid, 'UPLOAD_PHOTO')
        bot.sendPhoto(chat_id=uid, photo=open(adrs, 'rb'), caption=msg)
    except Exception as e:
        print(e)

def send_text(uid, msg, keyboard=None):
    try:
        bot.sendChatAction(uid, 'TYPING')
        if keyboard==None:
            bot.send_message(chat_id=uid, text=msg)
        else:
            reply_markup = telegram.ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            bot.send_message(chat_id=uid, text=msg, reply_markup=reply_markup)
    except Exception as e:
        print(e)

def send_document(uid,file_name,caption):
    try:
        document = open(file_name, 'rb')
        bot.sendChatAction(uid, 'UPLOAD_DOCUMENT')
        bot.send_document(uid, document, caption=caption)
        document.close()
    except Exception as e:
        print(e)

def handler(signum, frame):
    print('idle point')
    updater.idle()

if __name__ == "__main__":

    for k,v in os.environ.items():
        if k == 'BOT_TOKEN':
            my_token = v
        if k == 'ADMIN_UID':
            admin_uid = int(v)

    print("goog")
    print(my_token)
    print(admin_uid)

    global bot
    global updater
    global allowed_users

    bot        = telegram.Bot(token=my_token)
    updater    = Updater(my_token)
    allowed_users = [admin_uid]

    signal.signal(signal.SIGINT, handler)
    start_command = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_command)
    get_stat_command = CommandHandler('get_stat', get_stat, pass_args=True)
    updater.dispatcher.add_handler(get_stat_command)
    upload_command = CommandHandler('upload', upload, pass_args=True)
    updater.dispatcher.add_handler(upload_command)
    updater.start_polling()

    send_text(admin_uid, 'Bot started')

