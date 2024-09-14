"""
Basic skeleton of a mitmproxy addon with asynchronous HTTP request handling.

Run as follows: mitmproxy -s anatomy.py
"""

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

                logging.info(f"Response from httpbin: {response.json()}")

                return response
            except Exception as e:
                logging.error(f"Error fetching from httpbin: {e}")

                return None

    def response(self, flow):
        self.num += 1

        print(flow.request.host)
        print(flow.request.path)

        logging.info("We've seen %d flows" % self.num)

        # Asynchronously handle specific request to httpbin.org/ip
        if flow.request.host == "httpbin.org" and flow.request.path == "/ip" and flow.request.method == "GET":
            asyncio.create_task(self.send_async_request())


addons = [BetPlacementNotifier()]

