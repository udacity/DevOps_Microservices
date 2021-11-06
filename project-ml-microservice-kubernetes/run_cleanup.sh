# Resource: https://kubernetes.io/docs/tutorials/hello-minikube/
# Resource 2: https://kubernetes.io/docs/reference/kubectl/overview/

# Step 1: Stop Minicube virtual machine
minikube stop

# Step 3: Delete Minicube virtual machine
minikube delete

# Other cool commands
# Enable metrics: minikube addons enable metrics-server
# List other minikube addons: minikube addons list
# Disable metrics: minikube addons disable metrics-server