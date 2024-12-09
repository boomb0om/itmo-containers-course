kubectl apply -f manifests/configmap.yaml
kubectl apply -f manifests/postgres_secret.yaml
kubectl apply -f manifests/postgres_pvc.yaml
kubectl apply -f manifests/postgres_deployment.yaml
kubectl apply -f manifests/postgres_service.yaml
kubectl apply -f manifests/backend_deployment.yaml
kubectl apply -f manifests/backend_service.yaml