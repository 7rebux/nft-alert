#!/usr/bin/env python

__author__ = "Nils Osswald"

from dotenv import load_dotenv
import os
from instagrapi import Client
import tweepy

load_dotenv()

instagram = Client()
twitterv1 = None
twitterv2 = None


def instagram_login():
    print("Logging in to Instagram..")
    instagram.login(os.environ.get("INSTAGRAM_USER"), os.environ.get("INSTAGRAM_PASS"))
    print("Successfully logged in!")


def instagram_post(image, description, hashtags):
    print(f"Uploading {image} to Instagram..")
    post = instagram.photo_upload(image, f"{description}\n\n{hashtags}")
    print(f"Successfully uploaded to https://www.instagram.com/p/{post.code}")


def twitter_login():
    global twitterv1
    global twitterv2

    print("Logging in to Twitter..")
    twitterv2 = tweepy.Client(
        bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
        consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
        consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
        access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
        return_type=tweepy.Response,
        wait_on_rate_limit=True,
    )
    auth = tweepy.OAuthHandler(
        os.environ.get("TWITTER_CONSUMER_KEY"),
        os.environ.get("TWITTER_CONSUMER_SECRET"),
    )
    auth.set_access_token(
        os.environ.get("TWITTER_ACCESS_TOKEN"),
        os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
    )
    twitterv1 = tweepy.API(auth)
    print(f"Successfully logged in!")


def twitter_post(image, description):
    print(f"Uploading {image} to Twitter..")
    media_id = twitterv1.media_upload(image).media_id
    id = twitterv2.create_tweet(text=description, media_ids=[media_id]).data["id"]
    print(f"Successfully uploaded to https://twitter.com/_NFTalert_/status/{id}")


description = "Uploaded using nft-alert"
with open("instagram_hashtags.txt", "r") as file:
    hashtags = " ".join(file.read().splitlines())

instagram_login()
instagram_post("./image.jpg", description, hashtags)

twitter_login()
twitter_post("./image.jpg", description)
