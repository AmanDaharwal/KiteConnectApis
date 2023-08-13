import time, pyotp

totp_key = "H3K2ZSZQT3W3BZBF7SZVSYS7Y6PMXYQX"


def fetchTotp():
    time.sleep(1)
    authkey = pyotp.TOTP(totp_key)
    return authkey.now()
