#Programming Project 3 - OTP

**Purpose of code:** The code files contained in this directory can be used to generate a QR code for the Google Authenticator app and can be used to calculate a OTP within a terminal which if configured with the same parameters will match the OTP generated in the Google Authenticator app.

###Usage Directions (aka How to Run Project)
1. pip install PyQRCode==1.2.1 pyotp==2.6.0
2. python3 generate_qr.py
3. python3 get_otp.py

###OTP Configuration Options
- To adjust any of the parameters used by Google Authenticator open the generate_qr.py file and change any of the 5 variables set just below the __main__ procedure.
- To adjust the parameters used by the OTP calculator open the get_otp.py file and adjust the secret and otp_len variables below the __main__ procedure.

###Implementation Notes
My implementation is built in two separate files, generate_qr.py and get_otp.py. The reason for separating these two files is that I wanted to clearly differentiate the implementation of the otp generator and the qr generator. While building both of these I found a lot of enjoyment in adjusting the parameters of both the google authenticator qr generator and the get_otp generator to see what was possible when it came to configuring otp. One element I found reassuring is that no matter how much I tried I couldn't break the google auth and otp generator. Since they always matched it left me convinced of the reliability of this system. 

One other element I found interesting was that although I was able to configure otp to use both 7 and 8 characters I realized that I have never seen an otp system that leverages 7 or 8 digits used in a moder system. After thinking about this I'm pretty sure that it is because six digits is plenty for security and companies have found that adding additional characters may make it confusing for users who are used to a 6 character otp system. 

Lastly, when implementing both the qr generator and the otp generator I was amazed at just how simple it was to configure both of the systems using packages found on Pypi that are dedicated to these operations. I honestly see this as a huge benefit to using python for development. It makes the testing of new frameworks and approaches incredibly efficient and allows quick iteration of a given project. 