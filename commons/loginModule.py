from kiteconnect import KiteConnect
from helpers.seleniumWebDriver import launchbrowser, getcurrenturl, quitselenium
import time


def retriveRequestToken(redirected_url):
    # Extract the request token from the redirected URL
    request_token2 = redirected_url.split('request_token=')[1]

    request_token = request_token2.split('&action')[0]

    print("Request Token:", request_token)
    return request_token


def login(api_key, api_secret):
    # Create KiteConnect instance
    kite = KiteConnect(api_key=api_key)

    # Generate login URL
    login_url = kite.login_url()
    print("Login URL:", login_url)

    driver = launchbrowser(login_url)
    time.sleep(1)
    redirected_url = getcurrenturl(driver)
    quitselenium(driver)

    # Retrieve request token from the login URL
    request_token = retriveRequestToken(redirected_url)

    # Generate access token
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data['access_token']

    # Set access token
    kite.set_access_token(access_token)

    # Print user profile information
    user_profile = kite.profile()
    print("User Profile:")
    print("User ID:", user_profile['user_id'])
    print("Email:", user_profile['email'])
    print("Broker:", user_profile['broker'])

    kite.orders()
    return kite
