import redis

class RedisConnection(object):


    def __init__(self):
        self.redis = redis.Redis(host='', port=6379, decode_responses=True, password='')  

    
    def get_redis(self):
       return self.redis