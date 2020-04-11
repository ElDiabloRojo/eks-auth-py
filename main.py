from login import login
from mfa import mfa

def main():
    profile = login.main()
    mfa.main(profile)


if __name__ == '__main__':
    main()
