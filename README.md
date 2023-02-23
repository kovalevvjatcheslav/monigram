# monigram

### Building

```docker build --rm -f docker/monigram.docker -t monigram .```

### Deploy
You should create a file docker/private.env with contents
```commandline
HEC_TOKEN=<HTTP Event Collector token>
TELEGRAM_APP_ID=<telegram_app_id>
TELEGRAM_APP_HASH=<telegrma_app_hash>
TELEGRAM_BOT_TOKEN=<telegram_bot_token>
CHAT_ID=<channel_id>
```
then run
```docker-compose -f docker/docker_compose.yml up```

splunk service will be available at http://localhost:8000  
login: admin  
password: very_strong_password

### Additional info

The collected data can help in the following cases:
 - someone malicious may get access to an administrator's account 
   and perform some actions, collected data can help us rollback 
   those actions and prevent any other actions
 - we can prepare an alert that will be triggered when a lot of
   subscribers leave the channel and collected data help us figure 
   out why it happens
 - we can analyze how often a channel member posts or how much his 
   message is and trigger a spam alert
 - we can use sentiment analysis to detect offensive messages and delete them