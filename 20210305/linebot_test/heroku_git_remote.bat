@echo off
::將 heroku 新增到 git remote 當中
::heroku git:remote -a test200629-linebot
git init
heroku git:remote -a linebot-test-20201020
