# Yelp Button

> Press a button, and Yelp will tell you where to eat lunch

## To run:

First, create a file in the root of the project called `.env`. The contents of the file should be:

```
export YELP_CONSUMER_KEY=<your Yelp API v2 consumer key>
export YELP_CONSUMER_SECRET=<your Yelp API v2 consumer secret>
export YELP_TOKEN=<your Yelp API v2 token>
export YELP_TOKEN_SECRET=<your Yelp API v2 token secret>
```

Then, just:

```bash
./run.sh
```