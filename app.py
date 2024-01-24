import requests
import argparse

def send_slack_message(message: str):
    '''
    Send a message to our slack channel.
    '''
    payload = '{"text": "%s"}' % message

    response = requests.post(
        'YOUR WEBHOOK URL',
        data=payload
    )
    print(response.text)

def chat_with_user():
    '''
    Function to chat with the user and get a message.
    '''
    user_message = input('Enter your message: ')
    return user_message

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and receive messages with ChatGPT')
    args = parser.parse_args()

    user_input = chat_with_user()

    if len(user_input) > 0:
        send_slack_message(message=user_input)  # Fix the argument name here
    else:
        print('Please enter a message!')
