
C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate pyinstaller -F -w .\WebCrawler.py & xcopy /y dist\WebCrawler.exe WebCrawler.exe & rd /q/s dist & rd /q/s build & del /q/s WebCrawler.spec & rd /q/s __pycache__


pip install selenium
pip install openpyxl
pip install xlwings
\








pyinstaller -F -w .\GetSQ.py & xcopy /y dist\GetSQ.exe GetSQ.exe & rd /q/s dist & rd /q/s build & del /q/s GetSQ.spec & rd /q/s __pycache__