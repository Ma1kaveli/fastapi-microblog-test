# FastAPI microblog

## Install the dependencies

---

python -m venv venv
venv\Scripts\activate.bat
pip install -r .\requirements.txt 

---

## Generate secret key

---

python
>>>import os
>>>import binascii
>>>binascii.hexlify(os.urandom(24))

---

## Start the app

---

uvicorn main:app --reload --port=8080

---