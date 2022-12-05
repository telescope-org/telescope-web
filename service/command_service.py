import uuid
from common.logger import Logger
from common.mysql import MySQLConnection
from common.redis import RedisConnection


db = MySQLConnection()
redis = RedisConnection().redis

class CommandService(object):


    @staticmethod
    def __get_key(phone):
        return f"command:{phone}"

    @staticmethod
    def get_commands(phone: str) -> dict:
        try:
            return redis.hgetall(CommandService.__get_key(phone))
        except:
            return dict()

    @staticmethod
    def add_commands(phone: str, command_key: str):
        command_id = str(uuid.uuid4())
        redis.hset(CommandService.__get_key(phone), command_id, command_key)
        return redis.hexists(CommandService.__get_key(phone), command_id)

    @staticmethod
    def del_command(phone: str, cmd_id):
        redis.hdel(CommandService.__get_key(phone), cmd_id)
        return redis.hexists(CommandService.__get_key(phone), cmd_id) is False

    
    @staticmethod
    def receive(data):
        print(data)


    @staticmethod
    def clear_all_key(phone: str):
        # 设置马上过期
        return redis.expire(CommandService.__get_key(phone), 1)



    
