@echo off
cd /d S:\網通部\◎資訊\test\
move S:\網通部\◎資訊\test\0901_0918網通目標達成比*.jpg S:\網通部\◎資訊\test\0901_0918網通目標達成比%1.jpg
git init
git add .
git commit -m "New file"
git push

exit



