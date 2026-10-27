class phone :
    IMEI = None
    producer = None

    def call_by_5g(self):
        print("5G通话")

class RemoteControl :
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")

class Myphone(phone, RemoteControl):
    pass
