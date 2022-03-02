docker build -t header-echo-service .
kind load docker-image header-echo-service
kubectl apply -f ./manifests.yaml
