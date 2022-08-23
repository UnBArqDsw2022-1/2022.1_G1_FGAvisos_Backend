run:
	echo "Iniciando banco"
	sudo docker-compose up -d fgaaviso_db
	
	sleep 7
	echo "Iniciando app"
	sudo docker-compose up -d app
	echo "aplicando migracoes"
	sudo docker-compose exec app alembic upgrade head