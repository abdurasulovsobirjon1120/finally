**Linux yoki mac operatsion tizimida**
1. yangi folder ochish (test)
2. terminalda test papkasini ochish
3. git  clone https://github.com/abdurasulovsobirjon1120/finally.git   _ # loyihani clonlash_
_
**1. Virtual environment va kutubxonalarni o‘rnatish:**
4. pip3 install virtualenv    #_ virtual env ni install qilish_
5. python3 -m venv venv    # _virtual env ni yaratish_
6. source venv/bin/activate

**2. Loyihaga o‘tish va kutubxonalarni o‘rnatish:**
7. cd finally      _# finally papkasiga kirish_
8. pip install -r requirements.txt    _# kutubxonalarni install qilish_

**3. Django migratsiyalarini bajarish:**
10. python3 manage.py makemigrations
11. python3 manage.py migrate    _# migratsiyalarni amalga oshirish_

**4. Serverni ishga tushirish:**
12. python3 manage.py runserver


**Windows operatsion timida**
1. yangi folder ochish (test)
2. terminalda test papkasini ochish
3. git  clone https://github.com/abdurasulovsobirjon1120/finally.git  # loyihani clonlash

**1. Virtual environment va kutubxonalarni o‘rnatish:**
pip install virtualenv    _# virtualenv ni o‘rnatish_
python -m venv venv   _ # virtual environment yaratish_
venv\Scripts\activate    _# virtual environmentni faollashtirish_

**2. Loyihaga o‘tish va kutubxonalarni o‘rnatish:**
cd finally  # finally papkasiga kirish
pip install -r requirements.txt   _ # kutubxonalarni install qilish_


**3. Django migratsiyalarini bajarish:**
python manage.py makemigrations
python manage.py migrate    _# migratsiyalarni amalga oshirish_

**4. Serverni ishga tushirish:**
python manage.py runserver
