from profile import selector, profile
from mfa import mfa


def main():
    current_profile = profile.Profile(selector.main())
    current_profile.get_aws_keys()
    mfa


if __name__ == '__main__':
    main()
