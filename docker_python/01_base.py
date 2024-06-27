import random
import docker
import pyboxen
from rich.console import Console

console = Console()
client = docker.from_env()
image = client.images.pull("redis")
output = client.containers.run("ubuntu", "echo hello world")
output = output.decode("utf-8")
print(str(output))

containers = client.containers.list()
for container in containers:
    print(container.name)
PORT = random.randint(8000, 9000)
container = client.containers.run("nginx:latest", detach=True, ports={"80/tcp": PORT})


for image in client.images.list():
    print(image.id)


print(f"NGINX running on port {PORT}")
