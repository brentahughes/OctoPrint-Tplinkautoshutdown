import asyncio
from kasa import SmartStrip, SmartDeviceException
from .ThreadedWorker import ThreadedWorker

class TpLinkHandlerSmartStrip(SmartDeviceException):
	def __init__(self, address):
		self.worker = ThreadedWorker()
		self.device = SmartStrip(address)

	def update(self):
		asyncio.run(self.device.update())

	def update_two(self):
		asyncio.create_task(self.device.update())

	def update_three(self):
		future = asyncio.run_coroutine_threadsafe(self.device.update(), self.worker.loop)
		result = future.result()

	def shutdown_btn(self):
		asyncio.create_task(self.device.turn_off())
		return "shutdown"

	def turnOn_btn(self):
		asyncio.create_task(self.device.turn_on())
		return "Turning on"

	def turn_on(self, plugNumber):
		asyncio.run(self.device.children[plugNumber].turn_on())

	def shutdown(self, plugNumber):
		asyncio.run(self.device.children[plugNumber].turn_off())

	def get_plug_information(self):
		return self.device.hw_info

	def __repr__(self):
		pass
