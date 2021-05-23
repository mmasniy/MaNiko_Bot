class ClientUser:
    def __init__(self, id, name, phone, email):
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__mailing = False
        self.__sale = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_sale(self):
        return self.__sale

    def set_mailing(self, mailing):
        self.__mailing = mailing

    def set_sale(self, sale):
        self.__sale = sale

    def send_data_to_site(self):
        pass
