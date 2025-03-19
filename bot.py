import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler
import yagmail
import os

# Telegram bot token (Get this from @BotFather)
TELEGRAM_BOT_TOKEN = "7200863338:AAHB5vASJK7luUk9K2OIa1suB2b-Jf4BsIQ"

# Email credentials (Use an App Password if using Gmail)
EMAIL_ADDRESS = "asssasin105@gmail.com"
EMAIL_PASSWORD = "tattigal"

# Initialize email sender
yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Function to send mass emails
async def send_email(update, context):
    try:
        # Example recipients and message
        recipients = ["mail@bka.bund.de", "dsa.telegram@edsr.eu"]
        subject = "Test Mass Email"
        body = "Hello, this is a test email sent via the Telegram bot."

        # Send email
        yag.send(to=recipients, subject=subject, contents=body)

        # Send confirmation message to user
        await update.message.reply_text("Emails sent successfully!")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Build Telegram bot application
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Add command handler for sending emails
app.add_handler(CommandHandler("sendemail", send_email))

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()

