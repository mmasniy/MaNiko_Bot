import pymysql
from config import host, user, password, db_name
import json

class BotSQl:
    # create connection
    def __init__(self):
        self.connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    # insert client to bd
    def insert_data(self, user):
        if self.exists(user['id_users']):
            print("Insert")
            insert_data = f"INSERT INTO `client`(id_users, full_name, user_name, phone_number, sales_message) " \
                          f"VALUES ('{user['id_users']}', '{user['full_name']}', '', ''," \
                          f"{bool(user['sales_message'])});"
            # print(insert_data)
            self.cursor.execute(insert_data)
            self.connection.commit()
        else:
            print("User exists!")

    def update_sales_message(self, id_users, flag):
        update = f"UPDATE `client` SET sales_message = {flag} WHERE id_users = {id_users};"
        self.cursor.execute(update)

    # select all data
    def get_all_rows(self):
        select_all_data = "SELECT * FROM `client`"
        self.cursor.execute(select_all_data)
        data = self.cursor.fetchall()
        # for line in data:
        #     print(line)
        return data

    def get_all_users_from_sales_messages(self):
        select_query = f"SELECT id_users FROM `client` WHERE sales_message = TRUE;"
        self.cursor.execute(select_query)
        data = self.cursor.fetchall()
        for _ in data:
            print(_)
        return data

    def exists(self, id_users):
        select_query = f"SELECT * FROM `client` WHERE id_users = '{id_users}';"
        self.cursor.execute(select_query)
        data = self.cursor.fetchall()

        # for _ in data:
        #     print(_)

        if data:
            print('true')
            return False
        else:
            print('false')
            return True

    # close connection
    def close(self):
        self.connection.close()

    def test(self):
        try:
            bot_sql = BotSQl()
            print("-" * 20 + "  Successfully connected!  " + "-" * 20)

            try:
                # create table
                # with connection.cursor() as cursor:
                #     create_table = "CREATE TABLE `client`(id int AUTO_INCREMENT," \
                #                    " id_users varchar(32)," \
                #                    " full_name varchar(32)," \
                #                    " user_name varchar(32)," \
                #                    " phone_number varchar(16)," \
                #                    " sales_message bool, PRIMARY KEY (id));"
                #     cursor.execute(create_table)
                #     print('Table created!')
                admin2 = {
                    'id_users': '530420596',
                    'full_name': 'Павел',
                    'user_name': '',
                    'phone_number': '',
                    'sales_message': ''
                }
                # bot_sql.exists('18854')
                # bot_sql.insert_data(admin2)
                # bot_sql.get_all_rows()
                # bot_sql.update_sales_message('530420596', False)
                # bot_sql.get_all_users_from_sales_messages()
                # bot_sql.update_sales_message('530420596', True)
                # bot_sql.get_all_users_from_sales_messages()
                # bot_sql.update_sales_message('530420596', False)
                # bot_sql.get_all_rows()
                # bot_sql.get_all_users_from_sales_messages()
            finally:
                bot_sql.close()
        except Exception as ex:
            print("-" * 20 + "  Connection refused...  " + "-" * 20)
            print(ex)

# if __name__ == "__main__":
#     bot = BotSQl()
#     bot.test()
    # import sqlite3
    #
    #
    # class SQLighter:
    #
    #     def __init__(self, database):
    #         self.connection = sqlite3.connect(database)
    #         self.cursor = self.connection.cursor()
    #
    #     def select_all(self):
    #         """ Получаем все строки """
    #         with self.connection:
    #             return self.cursor.execute('SELECT * FROM music').fetchall()
    #
    #     def select_single(self, rownum):
    #         """ Получаем одну строку с номером rownum """
    #         with self.connection:
    #             return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]
    #
    #     def count_rows(self):
    #         """ Считаем количество строк """
    #         with self.connection:
    #             result = self.cursor.execute('SELECT * FROM music').fetchall()
    #             return len(result)
    #
    #     def close(self):
    #         """ Закрываем текущее соединение с БД """
    #         self.connection.close()