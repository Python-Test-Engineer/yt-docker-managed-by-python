import docker
import pyboxen
from rich.console import Console

console = Console()
client = docker.from_env()

output = client.containers.run("ubuntu", "echo hello world")
output = output.decode("utf-8")
print(str(output))

containers = client.containers.list()
for container in containers:
    print(container.name)

container = client.containers.run("nginx:latest", detach=True, ports={"80/tcp": 8200})

for image in client.images.list():
    print(image.id)


var1 = "..."
var2 = ["...", "123"]
var3 = "..."
# client = docker.from_env()
# client.containers.run("postgres", name=var1, environment=var2, mounts=var3, detach=True)
# client = docker.from_env()
# container = client.containers.run("ubuntu", detach=True)

# c.create_container(
#     image,
#     command=None,
#     hostname=None,
#     user=None,
#     detach=False,
#     stdin_open=False,
#     tty=False,
#     mem_limit=0,
#     ports=None,
#     environment=None,
#     dns=None,
#     volumes=None,
#     volumes_from=None,
#     network_disabled=False,
#     name=None,
#     entrypoint=None,
#     cpu_shares=None,
#     working_dir=None,
#     memswap_limit=0,
# )
