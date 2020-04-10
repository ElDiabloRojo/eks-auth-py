import os
import re
from tools.inquire import inquire
from tools.userAccept import yes_or_no
from tools.configure import configure
from pprint import pprint


def select():
    profiles = collect_profiles()
    profiles.append('create new profile')
    selection = inquire("profile", "select profile or create new", profiles)
    selected = selection['profile']

    return selected

def collect_profiles():
    profiles = [re.findall(r'\[(.*?)\]',line) for line in open(os.path.expanduser("~/.aws/credentials"))]
    profile_list = [item for sublist in profiles for item in sublist]

    return profile_list

def verify_selection():
    selected_profile = select()
    if selected_profile in collect_profiles():
        existing(selected_profile)
    else:
        create()

def existing(profile):
    if yes_or_no('selected profile: %s' % profile):
        print("Lmao :D")
    else:
        verify_selection()

def create():
    if yes_or_no('create new profile?'):
        print('new profile')
        configure()
    else:
        verify_selection()

def main():
    verify_selection()

if __name__ == '__main__':
    main()
