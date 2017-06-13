#!/bin/bash

git pull
docker build -t pythonweb  .
docker run -d -it  -p 8080:80 -p 8000:8000 --name pythontest pythonweb
##docker run -ti -p 8080:80 -p 8000:8000 --name pythontest pythonweb /bin/bash

docker run -d -it -p 8800:8800 --name test spectre.sirinmobile.local/pythontest:19
