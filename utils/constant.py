DOCKER_BASE_URL = r'unix://var/run/docker.sock'
LOG_PATH = r'./ctf_docker_supply_log'
SUCESS_RETURN_VALUE = 0
ERROR_RETURN_VALUE = 1
ERROR_PARA = 100
ERROR_UPLOAD_IMAGE = 101
ERROR_STARTUP_CONTAINER =102




class frp_api(object):
    frp_api_ip = '172.20.0.2'
    frp_api_port = '7400'
    frp_api_config_template = '''[common]\ntoken = AJ89@Hkqq\nserver_addr = 192.168.159.130\nserver_port = 6490 \
    \npool_count = 1000\ntls_enable = true\nadmin_addr = 172.20.0.2\nadmin_port = 7400\n\n'''
    frp_direct_ip_address = '192.168.159.130'
    frp_direct_port_maximum = 28110
    frp_direct_port_minimum = 28100
    redirect_port = 80
    docker_api_url = "172.1.0.3"