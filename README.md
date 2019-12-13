# Synchronous Kubernetes Template

This repo serves as a template for creating Kubernetes based prototypes in a 
faster manner.

With `Kubernetes` installed on a system, run

```shell script
kubectl apply -f kube-deployment.yml
```

If you're not running anything else on your installation of Kubernetes, you can run

```shell script
./RESTART_SERVICES.sh
```

But it deletes all existing pods and services, so perhaps not the best way to go about it
in the long run.


### Build Images

Running

```shell script
./DOCKER_IMAGES.sh
```
will build and push the docker images to be used, it is currently setup to push to my personal
repo, which you probably don't have access to.  This should also probably get moved to 
using environment variables.