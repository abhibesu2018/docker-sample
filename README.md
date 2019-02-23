# docker-sample
build - push - pull -run


Hub user: abhibesu.
Repository name: abhibesu2018
Image Tag Name: my-python-app

1. sudo docker build --tag abhibesu/abhibesu2018:my-python-app .

check with: sudo docker images

2. sudo docker push abhibesu/abhibesu2018:my-python-app

3. Optionally remove docker images in local:
  Command: sudo docker rmi -f <ImageID> <ImageID>
  e.g: sudo docker rmi -f a94f1b57a462 a94f1b57a462 

4. sudo docker pull abhibesu/abhibesu2018:my-python-app
check with: sudo docker images

5. Run the pull container with below sample command. (container tag name python-app, the conatiner name cannot be duplicate so give different name while running it) 
   e.g.: sudo nohup docker run --name python-app -p 5000:5000 abhibesu/abhibesu2018:my-python-app &

Check if the process running: sudo docker ps

Here, in the docker sample application check if 'Hello world' is printing at http://127.0.0.1:5000/


6. Go inside the running container:
   i. Get the container id from:  sudo docker ps
   ii.  execute the command: udo docker exec -it <container_id> /bin/sh
   [P.S.: the shell command can be different /bin/sh or /bin/bash - based on the image type]


Some useful commands:
1. To remove all usused/stopped stuff from local machine: sudo docker system prune
2. Get all the container id: sudo docker container ls -a
3. Get docker statistics: sudo docker stats
