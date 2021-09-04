@echo off
taskkill /f /im explorer.exe
rd/s/q S:\網通部\◎資訊\test\Thumbs.db
rd/s/q test
md test
start explorer.exe
git clone git@github.com:abel108714/test.git

pause
