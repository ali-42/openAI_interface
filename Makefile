services = backend frontend
all:
	docker-compose up --build --detach

%_stop:
	docker-compose stop $*

%_clean: %_stop
	docker-compose rm $* --force

stop: $(foreach service, $(services), $(service)_stop)
clean: $(foreach service, $(services), $(service)_clean)

fclean: clean
	docker system prune --force

re: fclean all
