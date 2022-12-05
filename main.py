#!/usr/bin/env python

__author__ = "Nils Osswald"

from dotenv import load_dotenv
import os
from instagrapi import Client

load_dotenv()

instagram = Client()

def instagram_login():
    print("Logging in to Instagram..")
    instagram.login(
        os.environ.get('INSTAGRAM_USER'),
        os.environ.get('INSTAGRAM_PASS')
    )
    print("Successfully logged in!")

def instagram_post(image, description, hashtags):
    print(f"Uploading {image} to Instagram..")
    media = instagram.photo_upload(
        image,
        f"{description}\n\n{hashtags}"
    )
    print(f"Successfully uploaded to https://www.instagram.com/p/{media.code}")

with open("instagram_hashtags.txt", "r") as file:
    hashtags = " ".join(file.read().splitlines())
description = "Uploaded using instagrapi for python to @nft_alert_"

instagram_login()
instagram_post("./image.jpg", description, hashtags)
