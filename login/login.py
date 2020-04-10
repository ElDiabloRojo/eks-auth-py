import os
import re
from tools.inquire import inquire
from tools.userAccept import yes_or_no
from pprint import pprint


def select():
    profiles = collectProfiles()
    profiles.append('create new profile')
    selection = inquire("profile", "Select profile", profiles)
    selected = selection['profile']

    return selected

def collectProfiles():
    profiles = [re.findall(r'\[(.*?)\]',line) for line in open(os.path.expanduser("~/.aws/credentials"))]
    profile_list = [item for sublist in profiles for item in sublist]

    return profile_list

def verifySelection():
    selected_profile = select()
    if selected_profile in collectProfiles():
        existing(selected_profile)
    else:
        create()

def existing(profile):
    if yes_or_no('selected profile: %s' % profile):
        print("Lmao :D")
    else:
        verifySelection()

def create():
    if yes_or_no('create new profile?'):
        print('new profile')
    else:
        verifySelection()

def main():
    verifySelection()

if __name__ == '__main__':
    main()
