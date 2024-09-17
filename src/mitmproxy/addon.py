import logging
import asyncio
import httpx


class BetPlacementNotifier:
    def __init__(self):
        self.num = 0

    async def send_async_request(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get("https://api.telegram.org/bot7514011991:AAF-8dzHVIISowicdAF26zJJriImb3S8Ufg/sendMessage?chat_id=-1002292296247&text=123")

                logging.info(f"Response from bet365: {response.json()}")

                return response
            except Exception as e:
                logging.error(f"Error fetching from httpbin: {e}")

                return None

    def response(self, flow):
        if 'bet365' in flow.request.host and 'placebet' in flow.request.path and flow.request.method == "POST":
            asyncio.create_task(self.send_async_request())


addons = [BetPlacementNotifier()]

