"""
Author: Travis Lange
Date: 5/8/2022
Description: This file contains code to generate a qr code that will encode the URI google authenticator expects.
             When this file is executed the QR code will be printed to the terminal and saved to the file "GA_URI.svg".
             To adjust the parameters of the URI that is encoded the paramaters can be set immediately below the main
             function that triggers the generator.
Citations:
    - QR Code Generator Documentation: https://pythonhosted.org/PyQRCode/
    - Google OTP URI Documentation: https://github.com/google/google-authenticator/wiki/Key-Uri-Format
"""
import base64
import pyqrcode

if __name__ == "__main__":
    # Set parameters for URI creation
    secret = "HelloWorld"
    user_id = "langet@oregonstate.edu"
    issuer = "langet_otp"
    otp_len = "8"
    algo = "SHA1"

    # Prior to URI creation encode the secret in b32 and remove the padding
    enc_secret = str(base64.b32encode(bytearray(secret, "ascii")), "ascii").strip("=")

    # Transforms our URI into an object that represents the qr code
    url = pyqrcode.create(f"otpauth://totp/{issuer}:{user_id}?secret={enc_secret}&issuer={issuer}&algorithm={algo}&digits={otp_len}")

    # Turn the qr code object into a .svg type image file with the given name in the same folder as this python script
    url.svg('GA_URI.svg', scale=8)

    # Print the image to the terminal
    print(url.terminal(quiet_zone=1))
