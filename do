docker rm -f portfolio-app
docker build -t portfolio-app .
docker run --name portfolio-app -p 9999:80 portfolio-app
