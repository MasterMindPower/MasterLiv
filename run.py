import os
from cryptography.fernet import Fernet

key = os.environ.get("FERNET_KEY")
if not key:
    raise SystemExit("FERNET_KEY missing")

blob = open("script.enc", "rb").read()
code = Fernet(key.encode()).decrypt(blob)

exec(compile(code, "secure.py", "exec"))
