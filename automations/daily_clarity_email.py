#!/usr/bin/env python3
import smtplib

def send_daily_clarity_email():
    sender = "juanmontoyas2003@gmail.com"
    receiver = "juanmontoyas2003@gmail.com"
    password = "wlxp bptc zebz csxo"
    clarity_google_doc = "https://docs.google.com/document/d/1z5JYJnHju7JINas3wzdmlDZ5weGrE1a7MfGH-jk2chw/edit?tab=t.0"

    subject = "Daily Clarity"
    body = "This is a daily clarity email."

    message = f"Subject: {subject}\n\n{body}\n\n{clarity_google_doc}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


if __name__ == "__main__":
    send_daily_clarity_email()