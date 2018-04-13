import time
from model import Model
from utils import get_local_time


class Todo(Model):
	def __init__(self, form):
		self.id = self.getid()
		self.title = form.get("title", "")
		self.ct = get_local_time(time.time())
		self.ut = self.ct