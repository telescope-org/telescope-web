from common.logger import Logger
from common.mysql import MySQLConnection


db = MySQLConnection()


class PhoneService(object):

    @staticmethod
    def register(val: dict):
        phone = val.get('phone')[3:]
        update_sql = f'''
            update care_helper.user
            set status=1
            where phone_number = '{phone}'
        '''
        Logger.info(f'exec sql {update_sql}.')
        res_val = db.exec_sql(update_sql)
        if res_val == -1:
            return False
        return True

       

    @staticmethod
    def location(val: dict):
        phone = val.get('phone')
        address = val.get('address')
        update_sql = f'''
            update care_helper.user
            set location = '{address}'
            where phone_number = '{phone}'
        '''
        Logger.info(f'exec sql {update_sql}.')
        res_val = db.exec_sql(update_sql)
        if res_val == -1:
            return False
        return True