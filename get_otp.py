import hashlib
import pyotp
import base64
import time

"""
Author: Travis Lange
Date: 5/8/2022
Description: This file contains the code to generate a OTP that will match the Google authenticator OTP. The variables
    set at the top of the main proc can be configured and adjusted to attempt various opt configurations. Additionally 
    after running the program will print a new otp every 30 seconds until "ctrl" + "z" or "ctrl" + "c" is entered on 
    the keyboard.
Citations:
    - PyOTP Docs: https://pyauth.github.io/pyotp/
    - Course Content: https://canvas.oregonstate.edu/courses/1870102/pages/week-7-exploration-one-time-passwords-otp
"""

if __name__ == "__main__":
    while True:
        secret = "HelloWorld"
        otp_len = 8

        # Prior to otp creation encode the secret in b32 and remove the padding
        enc_secret = str(base64.b32encode(bytearray(secret, "ascii")), "ascii").strip("=")

        # Create the otp using the TOTP module from pyotp
        totp = pyotp.TOTP(s=enc_secret, digits=otp_len, digest=hashlib.sha1)

        # Print the resulting totp the terminal
        print(totp.now())
        time.sleep(30)
