# import smtplib
#
#
# # def send_email(send_email ,code):
# #     try:
# #         server = smtplib.SMTP('smtp.gmail.com', 587)
# #         server.starttls()
# #         server.login(user='abdurasulovsobirjon1120@gmail.com', password='SObir2006')
# #         server.sendmail(from_addr='abdurasulovsobirjon1120@gmail.com', to_addrs=send_email, msg=code)
# #         print("Email sent successfully")
# #
# #     except Exception as e:
# #         raise e
#
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# def send_email(email, code):
#     global server
#     sender_email = "abdurasulovsobirjon1120@gmail.com"
#     app_password = "SObir2006"  # Use an app password if you have 2-Step Verification enabled.
#     recipient_email = email
#     subject = "2006"
#     body = f"Your verification code is: {code}"
#
#     # Set up the SMTP server
#     smtp_server = "smtp.gmail.com"
#     port = 587  # For TLS
#
#     # Create the email content
#     msg = MIMEMultipart()
#     msg['abdurasulovsobirjon1120@gmail.com'] = sender_email
#     msg['send_email'] = recipient_email
#     msg['code'] = subject
#
#     # Attach the body of the email to the MIME message
#     msg.attach(MIMEText(body, 'plain'))
#
#     try:
#         # Connect to the SMTP server and start TLS for security
#         server = smtplib.SMTP(smtp_server, port)
#         server.starttls()
#
#         # Log in to the server using the app password
#         server.login(user=sender_email, password=app_password)
#
#         # Send the email
#         server.sendmail(sender_email, recipient_email, msg.as_string())
#
#         print("Email sent successfully!")
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#     finally:
#         # Terminate the SMTP session and close the connection
#         server.quit()
#
