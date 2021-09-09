# import msvcrt
import time


high_score = 0
name = "Button Mashing Race"
while True:
    distance = int(0)
    print('\n--------------------------------------------------------------')
    print('\n\nWelcome to the 100m sprint, tap z and x rapidly to move!')
    print('* = 10m')
    print('\nCurrent record:' + str(high_score) + ' by: ' + name)
    print('\nPress enter to start')
    input()
    print('Ready...')
    time.sleep(1)
    print('GO!')

    start_time = time.time()
    while distance < 10:
        k1 = msvcrt.getch().decode('ASCII')
        if k1 == 'z':
            k2 = msvcrt.getch().decode('ASCII')
            if k2 == 'x':
                distance += 1
                if distance == 5:
                    print("* You're halfway there!")
                elif distance % 1 == 0:
                    print('*')

    fin_time = time.time() - start_time
    fin_time = round(fin_time, 2)

    print('Congratulations on successfully completing the race!')
    print('You took', fin_time, 'seconds to reach the finish line')

    if fin_time < high_score:
        print("Well done you've got a new high score ")
        name = input("Please enter your name : ")
        high_score = fin_time


def twilio():
    print("line 44")

def txt(Message, PhoneNumber):
    account_sid = 'ACefa8cf472e13295a5a5e21c7949efde2'
    auth_token = '20a56cceee22e13c4e9b0da6345cf8d3'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGe5012db9fd7766cc8faa28e5e2e03266',
        body="Test2",
        to="+7135577076"
    )

    print(message.sid)


# txt("My Test Message",'+7135577076')

def text2():
    account_sid = 'ACefa8cf472e13295a5a5e21c7949efde2'
    auth_token = '20a56cceee22e13c4e9b0da6345cf8d3'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGe5012db9fd7766cc8faa28e5e2e03266',
        body='Test3',
        to='+17135577076'
    )

    print(message.sid)


