**linux yoki mac operatsion tizimida**
1. yangi folder ochish (test)
2. terminalda test papkasini ochish
3. git  clone https://github.com/abdurasulovsobirjon1120/finally.git  # loyihani clonlash

**1. Virtual environment va kutubxonalarni o‘rnatish:**
4. pip3 install virtualenv virtual env ni install qilish
5. python3 -m venv venv # virtual env ni yaratish
6. source venv/bin/activate

**2. Loyihaga o‘tish va kutubxonalarni o‘rnatish:**
7. cd finally  # finally papkasiga kirish
8. pip install -r requirements.txt  # kutubxonalarni install qilish

**3. Django migratsiyalarini bajarish:**
10. python3 manage.py makemigrations
11. python3 manage.py migrate  # migratsiyalarni amalga oshirish

**4. Serverni ishga tushirish:**
12. python3 manage.py runserver


**Windows operatsion timida**
1. yangi folder ochish (test)
2. terminalda test papkasini ochish
3. git  clone https://github.com/abdurasulovsobirjon1120/finally.git  # loyihani clonlash

**1. Virtual environment va kutubxonalarni o‘rnatish:**
pip install virtualenv  # virtualenv ni o‘rnatish
python -m venv venv  # virtual environment yaratish
venv\Scripts\activate  # virtual environmentni faollashtirish

**2. Loyihaga o‘tish va kutubxonalarni o‘rnatish:**
cd finally  # finally papkasiga kirish
pip install -r requirements.txt  # kutubxonalarni install qilish


**3. Django migratsiyalarini bajarish:**
python manage.py makemigrations
python manage.py migrate  # migratsiyalarni amalga oshirish

**4. Serverni ishga tushirish:**
python manage.py runserver
