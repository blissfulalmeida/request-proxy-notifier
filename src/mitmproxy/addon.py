import subprocess
import datetime
import logging
import asyncio
import httpx
import time
import uuid
import os

class BetPlacementNotifier:

    # Constants for Telegram Bot (for now, you can keep them as placeholders)
    TELEGRAM_BOT_TOKEN = ''
    CHAT_ID = ''

    SCREENSHOT_COUNT = 4
    SCREENSHOT_DELAY = 0.5

    def __init__(self):
        self.num = 0

    async def response(self, flow):
        # if 'httpbin' in flow.request.host and flow.request.method == "POST":
        if 'bet365' in flow.request.host and 'placebet' in flow.request.path and flow.request.method == "POST":
            asyncio.create_task(self.send_screenshots())

    async def send_screenshots(self):
        batch_uuid = '#' + str(uuid.uuid4()).replace('-', '_')

        for i in range(self.SCREENSHOT_COUNT):
            output_file = await self.take_screenshot(i)
            tmp_batch_uuid = batch_uuid + f"\nImage {i + 1}"
            await self.send_photo_to_telegram(self.TELEGRAM_BOT_TOKEN, self.CHAT_ID,  output_file, tmp_batch_uuid)
            await self.remove_file(output_file)

            await asyncio.sleep(self.SCREENSHOT_DELAY)

        # ***** Utils *****
    async def take_screenshot(self, index):
        # Generate a timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nircmd_path = f"C:\\Users\\Administrator\\Downloads\\nircmd-x64\\nircmd.exe"
        output_file = f"C:\\screenshot_{timestamp}_{index}.png"

        subprocess.run([nircmd_path, 'savescreenshot', output_file], check=True)
        print(f"Screenshot saved to {output_file}")
        logging.info(f"Screenshot saved at: {output_file}")

        return output_file

    async def send_photo_to_telegram(self, bot_token, chat_id, photo_path, caption):
        url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

        with open(photo_path, 'rb') as photo_file:
            payload = {
                'chat_id': chat_id,
                'caption': caption
            }
            files = {
                'photo': photo_file
            }

            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(url, data=payload, files=files)
                    response.raise_for_status()  # Raise an error for bad responses
                    logging.info(f"Screenshots sent to Telegram successfully.")
                except httpx.HTTPStatusError as e:
                    logging.error(f"Error sending photo to Telegram: {e.response.status_code} - {e.response.text}")
                except Exception as e:
                    logging.error(f"Error sending photo to Telegram: {e}")

    async def remove_file(self, file_path):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logging.error(f"Error removing file {file_path}: {e}")

addons = [BetPlacementNotifier()]
