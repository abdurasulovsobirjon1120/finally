**Linux yoki mac operatsion tizimida**

* *Yangi folder ochish: mkdir **test***

* *cd **test** *

* *Loyihani klonlash:*

   git clone git@github.com:abdurasulovsobirjon1120/finally.git

---

**1\. Virtual environment va kutubxonalarni o‘rnatish:** 

* *Virtual environmentni o‘rnatish:*

pip3 install virtualenv

* *Virtual environment yaratish:*

   python3 \-m venv venv  
    
* *Virtual environmentni faollashtirish:*

   source venv/bin/activate

---

**2\. Loyihaga o‘tish va kutubxonalarni o‘rnatish:** 

* ***finally** papkasiga kirish:*

cd finally

* *Kutubxonalarni o‘rnatish:*

   pip install \-r requirements.txt

---

**3\. Django migratsiyalarini bajarish:** 

* *Migratsiyalar yaratish:*

python3 manage.py makemigrations

---

* *Migratsiyalarni amalga oshirish:*  
  python3 manage.py migrate

---

**4\. Serverni ishga tushirish:** 

* Django serverni ishga tushirish:

python3 manage.py runserver

**5\. Gunicorn orqali ishga tushirish:** 

* *Gunicornni o’rnatish:*  
  pip3 install gunicorn  
* Gunicornda run qilish  
  gunicorn \--bind 0.0.0.0:8000 myp.wsgi:application

---

**Windows operatsion tizimida**

* *Yangi folder ochish: mkdir **test***

* *cd **test** *
  
* Loyihani klonlash:

   git clone git@github.com:abdurasulovsobirjon1120/finally.git

---

**1\. Virtual environment va kutubxonalarni o‘rnatish:** 

* *Virtual environmentni o‘rnatish:*

pip install virtualenv

* *Virtual environment yaratish:*  
   

python \-m venv venv

* Virtual environmentni faollashtirish:

   venv\\Scripts\\activate

---

**2\. Loyihaga o‘tish va kutubxonalarni o‘rnatish:** 7\. 

* ***finally** papkasiga kirish:*

cd finally

* *Kutubxonalarni o‘rnatish:*

   pip install \-r requirements.txt

---

**3\. Django migratsiyalarini bajarish:** 

* *Migratsiyalar yaratish:*

python manage.py makemigrations

* *Migratsiyalarni amalga oshirish:*

python manage.py migrate  
---

**4\. Serverni ishga tushirish:** 

* *Django serverni ishga tushirish:*

python manage.py runserver  
---

**5\. Gunicorn orqali ishga tushirish:** 

* *Gunicornni o’rnatish:*  
  pip install gunicorn  
* Gunicornda run qilish  
  gunicorn \--bind 0.0.0.0:8000 myp.wsgi:application
