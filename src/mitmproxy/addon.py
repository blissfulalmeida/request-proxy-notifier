import logging
import asyncio
import httpx
import subprocess
import datetime

class BetPlacementNotifier:

    # Constants for Telegram Bot
    TELEGRAM_BOT_TOKEN = '2015393664:AAEnOcrdGeFY0k8gR7HGWgKrDJR3PsaUC7k'
    CHAT_ID = '-4548554255'

def __init__(self):
        self.num = 0

    def response(self, flow):
        # if 'bet365' in flow.request.host and 'placebet' in flow.request.path and flow.request.method == "POST":
        if 'httpbin' in flow.request.host and flow.request.method == "POST":
            asyncio.create_task(self.generate_screenshot())

    async def generate_screenshot(self):
        # Generate a timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"C:\\screenshot_{timestamp}.png"

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

        # Run the PowerShell command
        subprocess.run(["powershell", "-Command", powershell_command])

        # Send the screenshot to Telegram
        await self.send_to_telegram(output_file)

    async def send_to_telegram(self, file_path):
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Prepare the request to send the photo
            url = f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendPhoto"
            payload = {
                'chat_id': self.CHAT_ID,
            }
            files = {
                'photo': file,
            }

            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(url, data=payload, files=files)

                    if response.status_code == 200:
                        logging.info(f"Screenshot sent to Telegram successfully: {file_path}")

                    return response
                except Exception as e:
                    logging.error(f"Error sending screenshot: {e}")

                    return None

addons = [BetPlacementNotifier()]