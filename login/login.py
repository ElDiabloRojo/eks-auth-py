import os
import re
import tools.inquire
import tools.userAccept
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
    print('selected profile: %s' % profile)
    userAccept(profile)

def create():
    print('you have selected to input a new profile')

def main():
    verifySelection()

if __name__ == '__main__':
    main()
