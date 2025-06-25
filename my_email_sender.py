import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import os
print("CHOOSE ANY OF THESE:")
print("SEND EMAIL BY TEXTING")
print("SEND EMAIL BY VOICE TO TEXT MAIL")
user_email = input().strip().lower()

if user_email == "send email by texting": 
    message = EmailMessage()                
    message['from'] = 'sohailmohammed5425@gmail.com'
    message['subject'] = 'MESSAGE FROM SOHAIL'

    emails = input("Enter the email's: ")
    email_list = [e.strip() for e in emails.split(",")]
    message['to'] = ",".join(email_list)

    content = input("Enter the compose email: ")
    message.set_content(content)
    message.set_content(content)
    file_path=input("attach the path to send:")
    if os.path.exists(file_path):
        filename=os.path.basename(file_path)
        exits=filename.split('.')[-1].lower()
        if exits=='pdf':
            maintype,subtype='application','pdf'
        elif exits in ['jpg','jpeg']:
            maintype,subtype='image','jpg'
        elif exits=='mp3':
            maintype,subtype='audio','mp3'
        else:
            maintype,subtype="unknown"
        with open(file_path,'rb') as f:
            message.add_attachment(f.read(),maintype=maintype,subtype=subtype,filename=filename)
       #server mail transfer protocol smtp,server socket login
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login('sohailmohammed5425@gmail.com', 'kzmf cqze zvea ussh') #email,App Password
         smtp.send_message(message)

         print("Email send✅")


elif user_email=="send email by voice to text mail":
    R=sr.Recognizer()
    message=EmailMessage()
    message['from']='sohailmohammed5425@gmail.com'
    message['subject']='MESSAGE FROM SOHAIL'
    emails=input("enter the emails:")
    email_list=[e.strip() for e in emails.split(",")]
    message['to']=",".join(email_list)
    with sr.Microphone() as source:
        print("speak up 🎙️ listening...")
        audio_listen=R.listen(source)
        speak=R.recognize_google(audio_listen)
        print(f"you said:{speak}")
        message.set_content(speak)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smp:
        smp.login('sohailmohammed5425@gmail.com','kzmf cqze zvea ussh')
        smp.send_message(message)
        
    print("Email send✅")
    