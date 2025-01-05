import telebot
import subprocess
import datetime
import os
import logging
from datetime import datetime

# Initialize bot with your token
BOT_TOKEN = ""
CHAT_ID = ""
bot = telebot.TeleBot(BOT_TOKEN)

# Handler for /screenshot command
@bot.message_handler(commands=['screenshot'])
def handle_screenshot(message):
    try:
        # Take screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.expanduser("~\\Desktop")
        output_file = os.path.join(output_dir, f"screenshot_{timestamp}.png")
        
        # Take screenshot using nircmd
        result = subprocess.run(
            ["C:\\Program Files\\nircmd\\nircmd.exe", 'savescreenshot', output_file], 
            check=True,
            capture_output=True,
            text=True
        )
        
        # Verify file exists before trying to send
        if os.path.exists(output_file):
            print(f"Screenshot saved successfully to: {output_file}")
            
            # Send to Telegram
            with open(output_file, 'rb') as photo:
                bot.send_photo(CHAT_ID, photo, caption="Screenshot")
            
            # Clean up
            os.remove(output_file)
        else:
            raise FileNotFoundError(f"Screenshot file was not created: {output_file}")
            
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        bot.reply_to(message, error_msg)

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    logging.basicConfig(level=logging.INFO)
    bot.infinity_polling() 