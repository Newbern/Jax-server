class Device:

    def __init__(
        self,
        user_id,
        device_id,
        api_key,
        device_name,
        device_type
    ):
        self.user_id = user_id
        self.device_id = device_id
        self.api_key = api_key
        self.device_name = device_name
        self.device_type = device_type


    def authenticate(self, key):
        return self.api_key == key


    def status(self):
        return {
            "user_id" : self.user_id,
            "device_id": self.device_id,
            "name": self.device_name,
            "type": self.device_type
        }

