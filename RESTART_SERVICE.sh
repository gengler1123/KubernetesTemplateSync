#!/usr/bin/env bash

echo "Deleting Pods and Services"
kubectl delete pod,svc --all

echo "Loading New Deployment.yml"
kubectl apply -f kube-deployment.yml

echo "Sending Test CURL"
curl -X GET http://localhost:8082

