## Description

This project runs a Django/REST and Next.js applications in Docker, ready to deploy.

## Run all project

Create a new folder and cd in, then:

```bash
git clone https://github.com/yoandresaav/reto-tecnico-md.git .
docker compose up --force-recreate --build -d
```

After wait few seconds, open web browser and go to http://localhost:3000 

[open frontend link](http://localhost:3000)

Open backend swagger in http://localhost:8000

[open backend link](http://localhost:8000)

The process of build images takes some seconds in order to download all packages, run migrations, load test data and run tests.

## Terminate
In the same folder of the project run:

```bash
docker compose down
```

## Only for Build docker image

```bash
docker compose build
```

## Some probables errors

In window is possible docker don't detect in backend the start file. Open start.sh file in VSCode and change Select End of Line Sequence from CRLF to LF.

Important Note: Check don't have anothers apps running in ports 3000 and 8000.

In case of others error please open a fix in this ripository.


## Images

![Backend API](./images/screencapture-1.png)


![Frontend](./images/screencapture-2.png)
