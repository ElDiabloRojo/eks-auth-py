from profile import selector, profile
from aws import client


def main():
    current_profile = profile.Profile(selector.main())
    current_profile.get_aws_keys()
    iam_client = client.AWSCLient(service='iam', access_key=current_profile.access_key, secret_key=current_profile.secret_key)
    client.AWSCLient.show_object(iam_client)

if __name__ == '__main__':
    main()
