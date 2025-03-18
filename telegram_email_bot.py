import logging
import smtplib
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Email configuration
EMAIL_ADDRESS = 'asssasin105@gmail.com'
EMAIL_PASSWORD = 'tattigal'  # Make sure to use an app password if 2FA is enabled
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Function to send emails
def send_email(recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /send to send mass emails.')

# Send command handler
def send(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 3:
        update.message.reply_text('Usage: /send <subject> <body> <recipient1> <recipient2> ...')
        return

    subject = context.args[0]
    body = context.args[1]
    recipients = context.args[2:]

    for recipient in recipients:
        try:
            send_email(recipient, subject, body)
            update.message.reply_text(f'Email sent to {recipient}')
        except Exception as e:
            logger.error(f'Failed to send email to {recipient}: {e}')
            update.message.reply_text(f'Failed to send email to {recipient}: {e}')

# Main function to run the bot
def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN_HERE")  # Replace with your bot token

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("send", send))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if name == 'main':
    main()
