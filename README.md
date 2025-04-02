### **Loyihaning dokumentatsiya faylini havola orqali olishingiz mumkin!** 
###
| [![][HAVOLA]](https://docs.google.com/document/d/1Jf8eEsm5eoFNnW4smyYu-VLFz9wyPs9JaMJEUEFTXc8/edit?usp=sharing) |

### **Django xizmatini Nginx va HTTPS bilan ishga tushirish bo‘yicha qo‘llanma**

#### **1\. Virtual mashinani ishga tushirish**

VirtualBox/VMware yuklab oling va o‘rnating yoki Windows bo‘lsa, WSL2 dan foydalaning.  
 Ubuntu 22.04 bilan yangi virtual mashina yarating.  
 Kamida 4 GB RAM, 4 ta protsessor (CPU) va 40 GB disk hajmi ajrating.  
 Virtual mashinani ishga tushiring va Ubuntu o‘rnating.


| Birinchi topshiriq uchun linux ubuntu 22.04 operatsion tizimini ishga tushirish kerak. |
| :---- |
| https://drive.google.com/uc?id=1Dia9tenft5wTeebvYQIZLJfHVdmI_s8E |

#### 

#### **2\. Kerakli paketlarni o‘rnatish**
| sudo apt update && sudo apt upgrade \-y |
| ----- |
| https://drive.google.com/uc?id=11O1j3N0tQPDH77JyrisGsQUpRtKzPZsp |

| sudo apt install \-y git nginx python3 python3-venv python3-pip openssl |
| ----- |
| [![][image3]](https://drive.google.com/file/d/1wZFapC8R69FMCfB9CGG1yrWLoI-3B-yV/view?usp=drive_link) |
|  |

#### 

#### **3\. SSH sozlash va repozitoriy klonlash**

Agar SSH kalitlaringiz bo‘lmasa, yangi kalit yarating:

| ssh-keygen \-t rsa \-b 4096 \-C "[your\_email@example.com](mailto:your_email@example.com)"(3 marta enterni bosing) |
| :---- |
| cat /home/your\_pc\_name/.ssh/id\_rsa.pub |
| [![][image4]](https://drive.google.com/file/d/10XdFoZE6U0h38nIueosmQzo8xAV6G3Jr/view?usp=drive_link) |

| Ommaviy kalitni GitHub/GitLab/Bitbucket repozitoriyingizga qo‘shing. |
| ----- |
| [![][image5]](https://drive.google.com/file/d/1cJcEHZtjbytKv6AH_7XitV7_Ix4p3x75/view?usp=drive_link) |

| git clone git@github.com:abdurasulovsobirjon1120/finally.git |
| ----- |
| [![][image6]](https://drive.google.com/file/d/1YI0xdcepDUl1GfHpVOebEKwuvlc1i0YW/view?usp=drive_link) |

**4\. Django o‘rnatish va ishga tushirish**  
cd finally  
python3 \-m venv venv  
source venv/bin/activate  
pip install \-r requirements.txt  
python3 manage.py makemigratitons
python3 manage.py migrate 
python3 manage.py collectstatic \--noinput


Gunicorn bilan Django serverini ishga tushirish:  
pip install gunicorn

| gunicorn \--bind 0.0.0.0:8000 myp.wsgi:application |
| ----- |
| [![][image7]](https://drive.google.com/file/d/1K_kWzG7rU8IyATAkMNq8GGaG6orq5FhB/view?usp=drive_link) |
| [![][image8]](https://drive.google.com/file/d/1VyyruEKVq-eZZx8OVzOJBtznHuXSpSrj/view?usp=drive_link) |
| [![][image9]](https://drive.google.com/file/d/1aRP3a9jrcLkd69OoHlbeEoVOGQsM-M0q/view?usp=drive_link) |

#### 

#### 

#### **5\. Nginx sozlash (HTTP)**

Konfiguratsiya faylini ochamiz:

sudo nano /etc/nginx/sites-available/django

Quyidagi konfiguratsiyani qo‘shamiz:

server {  
	listen 80;  
	server\_name your\_domain\_or\_ip;

	location / {  
    	proxy\_pass http://127.0.0.1:8000;  
    	proxy\_set\_header Host $host;  
    	proxy\_set\_header X-Real-IP $remote\_addr;  
    	proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;  
	}  
}

| Nginx sozlash (HTTP) |
| ----- |
| [![][image10]](https://drive.google.com/file/d/1fv5VU54ofOCVHu7rxsuBW30Xtg8cHiLT/view?usp=drive_link) |

Sozlamalarni qo‘llash va Nginx-ni qayta ishga tushirish:  
sudo ln \-s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/

| sudo systemctl restart nginx |
| ----- |
| [![][image11]](https://drive.google.com/file/d/1Haexfvvu5coRvoSmf-1TbqsX_ZV6QQFH/view?usp=drive_link) |

6\. HTTPS sozlash (o‘z-o‘zini imzolagan sertifikat)

sudo openssl req \-x509 \-nodes \-days 365 \-newkey rsa:2048 \\  
  \-keyout /etc/ssl/private/nginx-selfsigned.key \\  
  \-out /etc/ssl/certs/nginx-selfsigned.crt

Nginx konfiguratsiyasini yangilaymiz:  
server {  
	listen 443 ssl;  
	server\_name your\_domain\_or\_ip;

	ssl\_certificate /etc/ssl/certs/nginx-selfsigned.crt;  
	ssl\_certificate\_key /etc/ssl/private/nginx-selfsigned.key;

	location / {  
    	proxy\_pass http://127.0.0.1:8000;  
    	proxy\_set\_header Host $host;  
    	proxy\_set\_header X-Real-IP $remote\_addr;  
    	proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;  
	}  
}

| HTTPS sozlash (o‘z-o‘zini imzolagan sertifikat) |
| ----- |
| [![][image12]](https://drive.google.com/file/d/1ywRSkI-FqGmM-yBBT057pCC0xRIzgaeM/view?usp=drive_link) |

Nginx-ni qayta ishga tushiramiz:  
sudo systemctl restart nginx

| Loyihani HTTPS orqali ishga tushirish |
| ----- |
| [![][image13]](https://drive.google.com/file/d/1DPeR5NFAIIMuL6Y7f5fzfsWzrujvKoVf/view?usp=drive_link) |
| [![][image14]](https://drive.google.com/file/d/1MIlGuZ7ipVaTjsz33hmReMiD3nXgSOqw/view?usp=drive_link) |

Endi xizmatga HTTPS orqali ulanishingiz mumkin\! 

###
###
###
###
###
###
###
###
**Loyihani ishga tushirish uchun qo'llanma(_4-topshiriq uchun_)**
###
###
**Linux yoki mac operatsion tizimida**

* *Yangi folder ochish: mkdir **test***

cd **test** 

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
control + C

**5\. Gunicorn orqali ishga tushirish:** 

* *Gunicornni o’rnatish:*  
  pip3 install gunicorn  
* Gunicornda run qilish  
  gunicorn \--bind 0.0.0.0:8000 myp.wsgi:application

---

**Windows operatsion tizimida**

* *Yangi folder ochish: mkdir **test***

 *cd **test** 
  
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
