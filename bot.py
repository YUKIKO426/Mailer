import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from email_validator import validate_email, EmailNotValidError

# Your Telegram bot token
TELEGRAM_API_TOKEN = '7200863338:AAHB5vASJK7luUk9K2OIa1suB2b-Jf4BsIQ'

# Email account details for SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "asssasin105@gmail.com"  # Your email
SENDER_PASSWORD = "tattigal"  # Your email password (or app password if 2FA enabled)

# List of recipient email addresses
RECIPIENTS = ["mail@bka.bund.de", "dsa.telegram@edsr.eu"]  # Add your recipients here

# Function to send email
def send_email(subject, body):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = ", ".join(RECIPIENTS)  # Multiple recipients
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, RECIPIENTS, text)

        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

# Start command handler for the Telegram bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Send '/send_mass_email' to send a mass email.")

# Send mass email command handler for the Telegram bot
def send_mass_email(update: Update, context: CallbackContext):
    # Basic email details
    subject = "Mass Email Subject"
    body = "This is the body of the mass email."

    try:
        # Validate email format
        for recipient in RECIPIENTS:
            try:
                validate_email(recipient)
            except EmailNotValidError as e:
                update.message.reply_text(f"Invalid email: {recipient}")
                return
        
        # Send email
        send_email(subject, body)
        update.message.reply_text("Mass email sent successfully!")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Main function to start the Telegram bot
def main():
    # Create Updater and pass your bot's token
    from telegram.ext import Application

app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()


    # Get the dispatcher to register handlers
def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher

    # Add handlers for commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("send_mass_email", send_mass_email))

    # Start the bot
    app.run_polling()
    updater.idle()

if __name__ == "__main__":
    main()
