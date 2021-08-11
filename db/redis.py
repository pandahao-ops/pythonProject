import redis


class HighPipRedis:

    def __init__(self):
        # noinspection PyBroadException
        try:
            pool = redis.ConnectionPool(host='192.168.100.3', port=6379, decode_responses=True)
            self.r = redis.Redis(connection_pool=pool)
        except Exception as e:
            print("redis connection fail, please check your redis config param.")

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        return self.r.set(key, value)

    def set_v_ttl(self, key, value, ttl):
        tmp = self.r.set(key, value)
        self.r.expire(key, ttl)
        return tmp

    def ttl(self, key):
        return self.r.ttl(key)

