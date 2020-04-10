import os
from login import login
from tools.userAccept import yes_or_no, request_value
from pprint import pprint


def configure():
    saved = False
    while not saved:
        profile_keys = ['profile name', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']
        profile = {}
        print('please enter the details for your new profile:\n')
        for k in profile_keys:
            profile[k] = request_value(k)

        confirm_profile(profile)

def confirm_profile(profile):
    if yes_or_no('\nare these details correct?:\n%s' % profile):
        verify_profile_exists(profile)
        saved = True
        
    else:
        print('\nrestarting profile input:\n')
        saved = False

def save_profile(profile):
    with open(os.path.expanduser('~/.aws/credentials'), 'a') as credentials_file:
        credentials_file.write('\n[%s]\n' % str(profile['profile name']))
        credentials_file.write('aws_access_key_id = %s\n' % str(profile['AWS_ACCESS_KEY_ID']))
        credentials_file.write('aws_secret_access_key = %s\n' % str(profile['AWS_SECRET_ACCESS_KEY']))

def verify_profile_exists(profile):
    while profile['profile name'] in login.collect_profiles():
        print('profile already exists, please change:')
        profile['profile name'] = request_value('profile name')
    print('saving profile...')
    save_profile(profile)
