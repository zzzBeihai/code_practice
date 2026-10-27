class Phone:
    IMEI = None
    producer = "zzz"

    def call_by_5G(self):
        print("使用5G网络通话")

class Myphone(Phone):
    producer = "张北海"

    def call_by_5G(self):
        print("开启省流模式")
    # 方式一
    # print(f"父类的厂商是：{Phone.producer}")
    # Phone.call_by_5G(self)
    # 方式二
        print(f"父类的厂商是：{self.producer}")
        super().call_by_5G()
        print("开启自毁，世界再见")

phone = Myphone()
phone.call_by_5G()
print(phone.producer)
