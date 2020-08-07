import ipaddress
from flask_redis import FlaskRedis
from redis.exceptions import LockError
from utils import constant
from api.db_api import DBUtils
import docker

class Redis:
    def __init__(self, app, user_id=0):
        self.redis_client = FlaskRedis(app)
        self.key = 'ctfd_whale_lock-' + str(user_id)
        self.lock = None
        self.global_port_key = "ctfd_whale-port-set"
        self.global_network_key = "ctfd_whale-network-set"

    def init_redis_port_sets(self):
        configs = constant.frp_api()
        self.redis_client.delete(self.global_port_key)
        self.redis_client.delete(self.global_network_key)

        containers = DBUtils.get_all_container()
        used_port_list = []
        for container in containers:
            if container.port != 0:
                used_port_list.append(container.port)
        # for port in range(int(configs.get("frp_direct_port_minimum", 29000)), int(configs.get("frp_direct_port_maximum", 28000)) + 1):
        for port in range(int(configs.frp_direct_port_minimum), int(configs.frp_direct_port_maximum)):
            if port not in used_port_list:
                self.add_available_port(port)

    def add_available_port(self, port):
        self.redis_client.sadd(self.global_port_key, str(port))

    def get_available_port(self):
        return int(self.redis_client.spop(self.global_port_key))

    def acquire_lock(self):
        lock = self.redis_client.lock(name=self.key, timeout=20)
        if not lock.acquire(blocking=True, blocking_timeout=2.0):
            return False
        self.lock = lock
        return True

    def release_lock(self):
        if self.lock is None:
            return False

        try:
            self.lock.release()

            return True
        except LockError:
            return False