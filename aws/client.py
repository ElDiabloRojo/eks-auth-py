

class AWSCLient:
    def __init__(self, service, access_key, secret_key, region, session_token=None):
        self.service = service
        self.access_key = access_key
        self.secret_access_key = secret_key
        self.session_token = session_token
        self.region = region

    def show_object(self):
        print(self.__dict__)