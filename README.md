# TOR PROXY
This repository allows to deploy a tor proxy with n different public IP's using an
auxiliar service that kills containers with duplicated IP's

Proxy ports:

| PORT | Meaning      |
|------|-------------:|
| 8118 | HTTP proxy   |
| 9050 | SOCKS proxy  |


🔨 Build Node-ok

Node-OK checks that every proxy replica has a different public IP
```
make node-ok
```
🚀 Deploy

* Using docker  
    ```
    docker stack deploy --compose-file docker-compose.yaml tor
    ```
* Using makefile
    ```
    make deploy
    ```

⚖ Scale

* Update number of proxy replicas
    ```
    docker service scale tor_proxy=100
    ```

😭 Remove
* Remove docker stack using docker
    ```
    docker stack rm tor 
    ```

* Remove docker stack makefile
    ```
    make rm
    ```
