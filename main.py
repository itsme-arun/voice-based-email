import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "vthtteam16@gmail.com"                        # Login credentials of our email id
pwd = "cccr luee gukm lcuq"

r = sr.Recognizer()

engine = pyttsx3.init()                                 # Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)




def speak(str):                                         # Function for text to speech
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():                                           # function for speech to text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)

def sendmail():
    str = "Please speak the recipient's email address"
    speak(str)
    rec_email = listen()

    if rec_email:
        # Remove spaces from the recipient's email address
        rec_email_without_spaces = rec_email.replace(" ", "")
        
        # Convert the email address to lowercase
        rec_email_lowercase = rec_email_without_spaces.lower()

        # Replace "dot" with actual dot (.)
        rec_email_dot = rec_email_lowercase.replace("dot", ".")
        rec_email_final = rec_email_dot.replace("at", "@")

        str = "Recipient's email address is: " + rec_email_final
        # Now, you can use rec_email_lowercase in your code
        speak(str)
        rec = rec_email_final

    str = "Please speak the body of your email"
    speak(str)
    sub = listen()

    str = "Your body of the email is"
    speak(str)
    speak(sub) 

    # Assuming unm and pwd are defined somewhere in your code
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, sub)
    server.quit()

    str = "The email has been Sent"
    speak(str)


# Assuming you have the required libraries imported
# You might need to replace 'e' with the actual library you are using for email operations
# Also, make sure to implement the 'listen()' and 'speak()' functions appropriately.

def readmail():
    server = e.connect("imap.gmail.com", unm, pwd)
    email_ids = server.listids()

    speak("Please say the serial number of the email you want to read starting from the latest")

    user_input = listen()

    if user_input:
        # Check if 'user_input' is "one" and convert it to 1
        if user_input.lower() == "one":
            user_input = "1"

        try:
            email_index = int(user_input) - 1

            if 0 <= email_index < len(email_ids):
                email = server.mail(email_ids[email_index])

                speak("The email is from:")
                speak(email.from_addr)
                speak("The subject of the email is:")
                speak(email.title)
                speak("The body of the email is:")
                speak(email.body)
            else:
                speak("Invalid email number. Please provide a valid serial number.")
        except ValueError:
            speak("Could not recognize the serial number you said. Please provide a valid number.")
    else:
        speak("No input was recognized. Please try again.")


str = "Welcome to voice controlled email service"
speak(str)

while(1):

    str = "Speak SEND to Send email    Speak READ to Read Inbox   Speak EXIT to Exit"
    speak(str)

    ch = listen()

    if (ch == 'send') :
        str = "You have chosen to send an email"
        speak(str)
        sendmail()

    elif ( ch == 'read') :
        str = "You have chosen to read email"
        speak(str)
        readmail()

    elif (ch == 'exit') :
        str = "You have chosen to exit, bye bye"
        speak(str)
        exit(1)

    else:
        str = "Invalid choice, you said:"
        speak(str)
        speak(ch)





