import boto3
import os
import re

def aws_client(svc, access_key, secret_key):
    client = boto3.client(svc, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    return client

def get_session_token(profile):
    profile_keys = get_aws_keys(profile)
    sts_client = aws_client('sts', profile_keys['aws_access_key_id'], profile_keys['aws_secret_access_key'])
    account_id = sts_client.get_caller_identity()["Account"]

    print(account_id)

def get_account_details(profile):
    profile_keys = get_aws_keys(profile)
    iam_client = aws_client('iam', profile_keys['aws_access_key_id'], profile_keys['aws_secret_access_key'])
    user = iam_client.get_user()
    userGroups = iam_client.list_groups_for_user(UserName=user['User']['UserName'])

    print(userGroups)
    return user

def get_aws_keys(profile):
    with open(os.path.expanduser('~/.aws/credentials')) as credentials_file:
        lines = credentials_file.readlines()
        for index, line in enumerate(lines):
            if '[' + profile + ']' in line:
                keys = [lines[index+1], lines[index+2]]
                profile_keys = {}
                for k in keys:
                    key_list = k.split()
                    key_list.remove('=')
                    profile_keys[key_list[0]] = key_list[1]

    return profile_keys

def main(profile):
    get_session_token(profile)
    get_account_details(profile)

if __name__ == '__main__':
    main(profile)
