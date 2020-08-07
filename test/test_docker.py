import docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# with open("/home/ctf_docker_supply/test/test.tar", 'rb') as f:
#     content = f.read()
# try:
#     res = client.images.load(content)
    
# except Exception as e:
#     print(e)


# res = client.images.remove("busybox:latest")
# def del_service():
#     client = docker.DockerClient(base_url='unix://var/run/docker.sock')
#     services = client.services.list(filters={"label":"1"})
#     for s in services:
#         print s
#         s.remove()

# res = del_service()
res = client.containers.list(filters={"label":"1-7f74efb3-72f9-42a0-96d3-4a221e07e9e3"})
if res:
    print("dd")
