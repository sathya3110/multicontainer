echo "Pulling the docker image of python web application"
docker pull kuthubshavali/pythondock:latest
echo "Starting the container"
docker run --name WebAppCont -it kuthubshavali/pythondock:latest
docker ps -a
echo "Completed"
exit 0
