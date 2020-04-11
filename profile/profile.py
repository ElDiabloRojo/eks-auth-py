import os


class Profile:
    def __init__(self, name, access_key=None, secret_key=None):
        self.name = name
        self.access_key = access_key
        self.secret_key = secret_key

    def get_aws_keys(self):
        with open(os.path.expanduser('~/.aws/credentials')) as credentials_file:
            lines = credentials_file.readlines()
            for index, line in enumerate(lines):
                if '[' + self.name + ']' in line:
                    keys = [lines[index+1], lines[index+2]]
                    profile_keys = {}
                    for k in keys:
                        key_list = k.split()
                        key_list.remove('=')
                        profile_keys[key_list[0]] = key_list[1]
                    self.access_key = profile_keys['aws_access_key_id']
                    self.secret_key = profile_keys['aws_secret_access_key']

                    return self.access_key, self.secret_key

    def show_object(self):
        print(self.__dict__)
