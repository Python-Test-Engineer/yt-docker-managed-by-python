# Docker managed by Python

https://docker-py.readthedocs.io/en/stable/

https://github.com/gabrieldemarmiesse/python-on-whales

https://earthly.dev/blog/yaml-in-python/ 

## Docker Postgres Setup


It uses the standard [docker-postgres-pgadmin-adminer-python-sql](https://github.com/Python-Test-Engineer/yt-docker-postgres-pgadmin-adminier-python-sql) project to set up Docker Postgres that has a link to the video on setting it up: [YouTube](https://www.youtube.com/watch?v=mipRKPHwlBk).

<br>

Set up of Docker with Postgress, PgAdmin and Adminer with Python CRUD.

Combines PgAdmin and Adminer for DB viewing.

Don't forget `docker compose up -d` or `docker compose up`.


## Set up Docker-Postgres-PgAdmin-Adminer
[My YouTube Video](https://youtu.be/mipRKPHwlBkI)

https://youtu.be/mipRKPHwlBk

I use a named volume here but video has bind mount volume - used in `docker-compose-bound-mount.yml`

NOTE
```
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal", !!! localhost etc don't seem to work...
)
```

### PgAdmin

<img src="./images/register-server-1.png"  width="500" >

<img src="./images/register-server-2.png"  width="500" >


<!-- ![PAGE](./images/register-server-1.png ) -->


- http://localhost:5050/
- admin@email.com
- admin

register-server

page-1 use any name
page-2:
      - POSTGRES_DB=postgres # optional
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

run docker-compose up in terminal ->

 ✔ Network postgres_default       Created                                                                                 
 ✔ Container postgres-pg-admin-1  Created                                                                                 
 ✔ Container postgres-postgres-1  Created                                                                                 
 ✔ Container postgres-adminer-1   Created     

### Adminer

admininer login on port http://localhost:8080

<img src="./images/adminer-login.png"  width="500" >
