@echo off
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
cd prj
python manage.py migrate
python manage.py runserver 8989