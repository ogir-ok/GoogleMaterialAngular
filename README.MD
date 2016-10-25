## Description

Django + angular + material design example of integration with google APIs
TODO:
* Add more functions to make it bigger
* Cover with unit tests
* ????

## Run on linux
1. Install docker and docker-compose.
2. Run
```bash
docker-compose up 
```

## Run on mac
###### Macbooks have problems with npm in docker

1. Start docker machine (use https://github.com/adlogix/docker-machine-nfs to increase performance)
2. Start docker containers with django+api+nginx 
```bash 
docker-compose -f docker-osx.yml up
```
3. To build client run on local machine
```bash
npm install -g gulp
cd client/
npm install
gulp watch
```

## How to test

1. Go to localhost:8000
2. Log in via google
3. You should see your emails loaded
4. You can log out from left menu