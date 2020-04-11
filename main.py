from profile import selector, profile
from aws import client
import configparser


def config():
    config = configparser.ConfigParser()
    config.read('./config.ini')

    return config


def main():
    project_config = config()
    region = project_config.get('general', 'REGION')
    current_profile = profile.Profile(selector.main())
    current_profile.get_aws_keys()
    iam_client = client.AWSCLient(service='iam', access_key=current_profile.access_key, secret_key=current_profile.secret_key, region=region)
    client.AWSCLient.show_object(iam_client)


if __name__ == '__main__':
    main()