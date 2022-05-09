REPLICAS?=1


node-ok:
	DOCKER_BUILDKIT=1 docker build -f node_ok/Dockerfile -t node_ok node_ok

deploy:
	docker stack deploy --compose-file docker-compose.yaml tor

rm:
	docker stack rm tor

scale:
	docker service scale tor_proxy=$(REPLICAS)