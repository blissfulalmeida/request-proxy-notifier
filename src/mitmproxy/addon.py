import logging
import asyncio
import httpx
import subprocess
import datetime
import time
import uuid
import os
from utils import take_screenshot

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
            asyncio.create_task(self.generate_screenshot())

    async def generate_screenshot(self):

        screenshots = []

        for i in range(self.SCREENSHOT_COUNT):
            output_file = await take_screenshot(i)  # Take a screenshot and get the output file path
            screenshots.append(output_file)

            # Wait for 1 second before taking the next screenshot
            await asyncio.sleep(self.SCREENSHOT_DELAY)

        # Send the screenshot to Telegram
        await self.send_screenshots(screenshots)

    async def send_screenshots(self, file_paths):
        # Open the file in binary mode
        batch_uuid = '#' + str(uuid.uuid4()).replace('-', '_')

        for index, file_path in enumerate(file_paths):
            with open(file_path, 'rb') as file:
                url = f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendPhoto"
                tmp_batch_uuid = batch_uuid + f"\nImage {index + 1}"
                payload = {
                    'chat_id': self.CHAT_ID,
                    'caption': tmp_batch_uuid
                }
                files = {
                    'photo': file
                }

                async with httpx.AsyncClient() as client:
                    try:
                        response = await client.post(url, data=payload, files=files)
                        if response.status_code == 200:
                            logging.info(f"Screenshots sent to Telegram successfully.")

                    except Exception as e:
                        logging.error(f"Error sending screenshot: {e}")

        await self.remove_files(file_paths)

    async def remove_files(self, file_paths):
       for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logging.error(f"Error removing file {file_path}: {e}")



addons = [BetPlacementNotifier()]
