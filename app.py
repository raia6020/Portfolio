from flask import Flask,render_template,request
import smtplib
from jinja2 import Template
from flask import send_file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        myEmail = 'backmykingdom11@gmail.com'
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Warm regards from Aman"
        msg['From'] = myEmail
        msg['To'] = email
        
       # Create the body of the message (a plain-text and an HTML version).

        with open("templates/contact.html", encoding='utf-8-sig') as myfile:
            outerdata=myfile.read()
            template = Template(outerdata)
            mainpage=template.render(firstName = name,body = message)
        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = mainpage

       # Record the MIME types of both parts - text/plain and text/html.
        # part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

       # Attach parts into message container.
       # According to RFC 2046, the last part of a multipart message, in this case
       # the HTML message, is best and preferred.
        # msg.attach(part1)
        msg.attach(part2)

       # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myEmail, 'zikbmcdxwcovohrw')
        mail.sendmail(myEmail, email, msg.as_string())
        mail.quit()
        return render_template('index.html')
        
    return render_template('index.html')

@app.route('/download_cv')
def download_cv():
    filename = 'resume.pdf'  # Replace with the path to your CV file
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
