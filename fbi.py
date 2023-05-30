import json
import sys
import hashlib
import os
import time
import requests
import getpass

W = ''
G = ''
R = ''

if sys.platform in ["linux", "linux2"]:
    W = "\033[0m"
    G = '\033[92m'
    R = '\033[91m'

# I don't know
jml = []
jmlgetdata = []
n = []

# BANNER
def baliho():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me?access_token='+ token)
        a = json.loads(r.text)
        name = a['name']
        n.append(a['name'])
    except (KeyError, IOError):
        print(R + '_     _'.center(44))
        print("o' \.=./ `o".center(44))
        print('(o o)'.center(44))
        print('ooO--(_)--Ooo'.center(44))
        print(' ' + W)
        print('F B I'.center(44))
        print(W + '     [' + G + 'Facebook Information' + W + ']')
        print(' ')

# Print In terminal
def show_program():
    print('''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Hak9
    Name       Facebook Information
    Version    Full Version
    Date       08/04/2019
    Jabber     xhak9x@jabber.de

* if you find any errors or problems, please contact the author
''' % (G, W))

def info_ga():
    print('''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
                      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
''' % (G, W))

def menu_bot():
    print('''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
''' % (G, W))

def menu_reaction():
    print('''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 04 ]      reaction 'HAHA'
   [ 05 ]      reaction 'SAD'
   [ 06 ]      reaction 'ANGRY'

   [ 00 ]      back to menu bot
''' % (G, W))

# GENERATE ACCESS TOKEN
def get(data):
    print('[*] Generate access token ')

    try:
        os.mkdir('cookie')
    except OSError:
        pass

    os.system('clear')

    if data == 'token':
        info()
        print()
        print('Make sure you are connected to the internet\n')
        print('[!] just enter email and password Facebook')
        print('    you can use temporary email\n')
        print('Format input email and password: %semail|pass%s' % (G, W))
        print('    examples: %sxxxxx@gmail.com|123xxx%s' % (G, W))
        print('              %sxxxxx@yahoo.com|123xxx%s' % (G, W))
        print('              %sxxxxx@domain.com|123xxx%s' % (G, W))
        print()
        token = getpass.getpass('[?] Email|Password : ')
        print()
        x = token.split('|')
        payload = {'email': x[0], 'pass': x[1]}
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + payload['email'] + '&password=' + payload['pass'] + '&language=en_US&format=json&generate_machine_id=1&generate_session_cookies=1&locale=en_US&new_login_options=eyJvcmlnaW5fanNvbnN1bWVfbG9jYXRpb25fcXVlcnlfc2VydmljZV9lZGl0b3IiOiJHQUlBIiwib3JpZ2luX3NvbnN1bWVfbG9jYXRpb25fcXVlcnlfdHlwZSI6ImdyYXZhdGUiLCJ0eXBlIjoxMH0%3D&sid=0')
        z = json.loads(data.text)

        try:
            error = z['error']['message']
            print(R + 'Token Error: ' + error + W)
            print()
        except KeyError:
            print(G + 'Status  : ' + W + 'Connected\n')
            print(G + 'Token   : ' + W + z['access_token'] + '\n')
            open('cookie/token.log', 'w').write(z['access_token'])

    elif data == 'cat_token':
        try:
            token = open('cookie/token.log', 'r').read()
            print(G + 'Token: ' + W + token)
        except IOError:
            print(R + 'Token not found' + W)

    elif data == 'rm_token':
        try:
            os.remove('cookie/token.log')
            print(G + 'Token removed' + W)
        except OSError:
            print(R + 'Token not found' + W)

    print('Press enter to continue')
    input()
    main()

# MAIN
def main():
    os.system('clear')
    baliho()
    show_program()
    info_ga()
    try:
        pilih = input(G + 'Facebook-Information > ' + W)

        if pilih == 'help':
            info_ga()
            input('Press enter to continue')
            main()

        elif pilih == 'about':
            show_program()
            input('Press enter to continue')
            main()

        elif pilih == 'token':
            get('token')

        elif pilih == 'cat_token':
            get('cat_token')

        elif pilih == 'rm_token':
            get('rm_token')

        elif pilih == 'get_data':
            get_data()

        elif pilih == 'get_info':
            get_info()

        elif pilih == 'dump_id':
            dump_id()

        elif pilih == 'dump_phone':
            dump_phone()

        elif pilih == 'dump_mail':
            dump_mail()

        elif pilih == 'bot':
            bot()

        elif pilih == 'clear':
            os.system('clear')
            main()

        elif pilih == 'exit':
            os.system('clear')
            sys.exit()

        elif pilih == '':
            main()

        else:
            os.system('clear')
            print(R + 'Command not found' + W)
            input('Press enter to continue')
            main()

    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit()

# FETCHING FRIENDS DATA
def get_data():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)

        for data in a['data']:
            x = data['id'] + '|' + data['name'] + '|' + data['gender'] + '|' + data['relationship_status']
            jmlgetdata.append(x)
            print(x)
        input('Press enter to continue')
        main()
    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        main()

# SHOW INFORMATION FRIENDS
def get_info():
    try:
        token = open('cookie/token.log', 'r').read()
        uid = input('uid : ')
        r = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token)
        a = json.loads(r.text)

        print('')
        print('[!] Name       : ' + a['name'])
        print('[!] ID         : ' + a['id'])
        print('[!] Gender     : ' + a['gender'])
        print('[!] Relationship status : ' + a['relationship_status'])
        print('')

        x = a['id'] + '|' + a['name'] + '|' + a['gender'] + '|' + a['relationship_status']
        jmlgetdata.append(x)

        input('Press enter to continue')
        main()
    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        main()

# FETCHING ALL ID FRIENDS
def dump_id():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)

        for data in a['data']:
            x = data['id']
            jml.append(x)
            print(x)
        input('Press enter to continue')
        main()
    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        main()

# FETCHING ALL PHONE NUMBER FRIENDS
def dump_phone():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)

        for data in a['data']:
            try:
                uid = data['id']
                r = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token)
                a = json.loads(r.text)
                print(a['id'] + ' | ' + a['mobile_phone'])
            except KeyError:
                pass
        input('Press enter to continue')
        main()
    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        main()

# FETCHING ALL EMAIL FRIENDS
def dump_mail():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)

        for data in a['data']:
            try:
                uid = data['id']
                r = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token)
                a = json.loads(r.text)
                print(a['id'] + ' | ' + a['email'])
            except KeyError:
                pass
        input('Press enter to continue')
        main()
    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        main()

# MENU BOT
def bot():
    os.system('clear')
    menu_bot()

    try:
        pilih = input(G + 'Bot Menu > ' + W)

        if pilih == '00':
            main()

        elif pilih == '01':
            auto_reaction()

        elif pilih == '02':
            auto_comment()

        elif pilih == '03':
            auto_poke()

        elif pilih == '04':
            accept_all()

        elif pilih == '05':
            delete_posts()

        elif pilih == '06':
            delete_friends()

        elif pilih == '07':
            stop_following()

        elif pilih == '08':
            delete_album()

        elif pilih == '':
            bot()

        else:
            os.system('clear')
            print(R + 'Command not found' + W)
            input('Press enter to continue')
            bot()

    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit()

# AUTO REACTION
def auto_reaction():
    os.system('clear')
    menu_reaction()

    try:
        pilih = input(G + 'Auto Reaction > ' + W)

        if pilih == '00':
            bot()

        elif pilih == '01':
            reaction('like')

        elif pilih == '02':
            reaction('love')

        elif pilih == '03':
            reaction('wow')

        elif pilih == '04':
            reaction('haha')

        elif pilih == '05':
            reaction('sad')

        elif pilih == '06':
            reaction('angry')

        elif pilih == '':
            auto_reaction()

        else:
            os.system('clear')
            print(R + 'Command not found' + W)
            input('Press enter to continue')
            auto_reaction()

    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit()

# REACTION
def reaction(tipe):
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/home?fields=id&access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                url = 'https://graph.facebook.com/' + i['id'] + '/reactions?type=' + tipe + '&method=post&access_token=' + token
                requests.post(url)
                print(i['id'] + ' [' + tipe + ']')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        auto_reaction()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        auto_reaction()

# AUTO COMMENT
def auto_comment():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/home?fields=id&access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                message = 'Nice post'
                url = 'https://graph.facebook.com/' + i['id'] + '/comments?message=' + message + '&method=post&access_token=' + token
                requests.post(url)
                print(i['id'] + ' [commented]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# AUTO POKE
def auto_poke():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/pokes?access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                poke = i['from']['id']
                url = 'https://graph.facebook.com/me/pokes?target=' + poke + '&method=post&access_token=' + token
                requests.post(url)
                print(i['from']['name'] + ' [' + poke + '] [poke]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# ACCEPT ALL FRIEND REQUESTS
def accept_all():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/friendrequests?limit=9999&access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                poke = i['from']['id']
                url = 'https://graph.facebook.com/me/friends/' + poke + '?method=post&access_token=' + token
                requests.post(url)
                print(i['from']['name'] + ' [' + poke + '] [added]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# DELETE ALL POSTS IN TIMELINE
def delete_posts():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/feed?access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                url = 'https://graph.facebook.com/' + i['id'] + '?method=delete&access_token=' + token
                requests.delete(url)
                print(i['id'] + ' [deleted]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# DELETE ALL FRIENDS
def delete_friends():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/friends?limit=9999&access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                url = 'https://graph.facebook.com/me/friends/' + i['id'] + '?method=delete&access_token=' + token
                requests.delete(url)
                print(i['id'] + ' [unfriended]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# STOP FOLLOWING ALL FRIENDS
def stop_following():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/subscribedto?access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                url = 'https://graph.facebook.com/' + i['id'] + '/subscribedto?method=delete&access_token=' + token
                requests.delete(url)
                print(i['id'] + ' [unfollowed]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# DELETE ALL ALBUMS
def delete_album():
    try:
        token = open('cookie/token.log', 'r').read()
        url = 'https://graph.facebook.com/me/albums?limit=9999&access_token=' + token
        r = requests.get(url)
        x = json.loads(r.text)

        for i in x['data']:
            try:
                url = 'https://graph.facebook.com/' + i['id'] + '?method=delete&access_token=' + token
                requests.delete(url)
                print(i['id'] + ' [deleted]')
            except (KeyError, IOError):
                pass
        input('Press enter to continue')
        bot()

    except (KeyError, IOError):
        print(R + 'Token not found' + W)
        print('Please generate access token first')
        input('Press enter to continue')
        bot()

# SHOW PROGRAM INFO
def show_program():
    print('')
    print('--------------------------------------')
    print('   Facebook Information')
    print('   Version : 1.0')
    print('   Coded by : G-SQUAD')
    print('   Github : https://github.com/G-SQUAD-ID')
    print('--------------------------------------')
    print('')

# SHOW MENU PROGRAM
def menu_bot():
    print('')
    print('--------------------------------------')
    print('   Facebook Information')
    print('   Bot Menu')
    print('--------------------------------------')
    print('   [00] Back to main menu')
    print('   [01] Auto Reaction')
    print('   [02] Auto Comment')
    print('   [03] Auto Poke')
    print('   [04] Accept All Friend Requests')
    print('   [05] Delete All Posts in Timeline')
    print('   [06] Delete All Friends')
    print('   [07] Stop Following All Friends')
    print('   [08] Delete All Albums')
    print('--------------------------------------')

# SHOW MENU AUTO REACTION
def menu_reaction():
    print('')
    print('--------------------------------------')
    print('   Facebook Information')
    print('   Auto Reaction')
    print('--------------------------------------')
    print('   [00] Back to Bot Menu')
    print('   [01] Like')
    print('   [02] Love')
    print('   [03] Wow')
    print('   [04] Haha')
    print('   [05] Sad')
    print('   [06] Angry')
    print('--------------------------------------')

# MAIN PROGRAM
if __name__ == '__main__':
    os.system('clear')
    main()













