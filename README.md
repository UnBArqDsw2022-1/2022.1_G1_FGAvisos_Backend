# 2022.1_G1_fgavisos_Backend

Para rodar o backend atualmente:

```
docker-compose build
```

```
docker-compose up
```


Procurar o ID do container com name igual a fgavisos-api

```
docker ps
```

Entrar no container usando:

```
docker exec -it <container_id> bash
```

Dentro do container executar o seguinte comando:

```
python3 create_tables.py
```

Para sair do container:

```
exit
```