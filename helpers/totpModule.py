import time, pyotp

totp_key = "otp_key"


def fetchTotp():
    time.sleep(1)
    authkey = pyotp.TOTP(totp_key)
    return authkey.now()
