import requests
from utils.constant import frp_api
from api.db_api import DBUtils

class FrpUtils:
    @staticmethod
    def update_frp_redirect():
        containers = DBUtils.get_all_alive_container()
        print(containers)
        output = frp_api.frp_api_config_template
        direct_template = "\n\n[direct_%s]\n" + \
                          "type = tcp\n" + \
                          "local_ip = %s\n" + \
                          "local_port = %s\n" + \
                          "remote_port = %s\n" + \
                          "use_compression = true" + \
                          "\n\n[direct_%s_udp]\n" + \
                          "type = udp\n" + \
                          "local_ip = %s\n" + \
                          "local_port = %s\n" + \
                          "remote_port = %s\n" + \
                          "use_compression = true"
        for c in containers:
            output += direct_template % (
                str(c.user_id) + '-' + c.id, 
                str(c.user_id) + '-' + c.id,
                frp_api.redirect_port, 
                c.port,
                str(c.user_id) + '-' + c.id, 
                str(c.user_id) + '-' + c.id,
                frp_api.redirect_port,  
                c.port)

            requests.put("http://" + frp_api.frp_api_ip + ":" + frp_api.frp_api_port + "/api/config", output,
                     timeout=5)
            requests.get("http://" + frp_api.frp_api_ip + ":" + frp_api.frp_api_port + "/api/reload", timeout=5)
            print (output)
