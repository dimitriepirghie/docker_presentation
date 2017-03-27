#Demo twitter.

1. Docker container fetches tweets from twitter by a tag. `#trump` in our case and insert tweets in a MongoDB data base.
2. Docker container fetch tweets from MongoDB database and list those tweets in a web page.
3. Docker container which runs a MongoDB data base.

##Build images

`cd tweets_fetcher`

`sudo docker build -t tweets_fetcher_img .`

`cd tweets_viewer`

`sudo docker build -t tweets_viewer_img .`


## Run mongo
`docker run -d --name mongo`

## Run fetcher
`docker run -e PYTHONUNBUFFERED=0 -d --name tweets_fetcher --link mongo:mongo --env-file ./env.list tweets_fetcher_imgsteps`

## Run viewer
`docker run -d --name tweets_viewer --link mongo:mongo -p 5000:5000 tweets_viewer_img`

#### Parameters:
1. -d  - run container as a daemon, detached from console.
2. --name - manager container by name after. <br>
  `docker start tweets_fetcher`
3. --env-file set environment variables on docker container.
4. --link - attach containers, so `tweets_fetcher` and `tweets_viewer` connect to mongo using "hostname" `mongo`
