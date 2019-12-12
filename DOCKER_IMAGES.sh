#!/usr/bin/env bash


docker-compose build

docker push gengler1123/template_psql
docker push gengler1123/template_orchestrator
docker push gengler1123/template_service_01
docker push gengler1123/template_service_02
docker push gengler1123/template_redis