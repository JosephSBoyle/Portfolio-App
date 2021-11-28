### Setting up the dockerfile
```$ docker build -t portfolio-app .```

### Running the dockerfile and app
```$ docker run -d --name portfolio-app -p 9999:80 portfolio-app```

### Removing the docker container
```$ docker rm -f portfolio-app```