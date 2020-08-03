import docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# with open("/home/ctf_docker_supply/test/test.tar", 'rb') as f:
#     content = f.read()
# try:
#     res = client.images.load(content)
    
# except Exception as e:
#     print(e)

res = client.images.remove("busybox:latest")
print res
