# 2022.1_G1_fgavisos_Backend

Pré-requisito para rodar o projeto: Docker e Docker Compose

### Para rodar

#### Opção 1 (só funciona no linux):

```
make
```

Após rodar o comando espere um pouco e a aplicação já estara no ar.

#### Opção 2 (funciona para windows, linux e macOS):

Rodando a primeira fez:

```
docker-compose build
```

```
docker-compose up 
```

```
docker-compose exec app alembic upgrade head
```

Nas demais vezes: 

```
docker-compose up
```