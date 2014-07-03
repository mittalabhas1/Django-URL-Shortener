from django.db import models

class URLDatabase(models.Model):
	"""
	Database of shortened URLs.
	"""
	long_url = models.URLField(max_length=400, blank=False, unique=True)
	short_url = models.CharField(max_length=15, blank=False, unique=True)
	visits = models.PositiveIntegerField(default=0)
	created_time = models.DateTimeField(auto_now_add=True)
	last_visit_time = models.DateTimeField(auto_now=True)

	def __init__(self, arg):
		super(URLDatabase, self).__init__()
		self.arg = arg

	def __unicode__(self):
		return self.short_url;

	def post_save(self):
		allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijkmnopqrstuvwxyz"
		allowed_chars_size = len(allowed_chars)
		flight = 5256
		"""
		For minimum three characters
		"""

		long_url = self.long_url
		id = self.id + flight

		short_url = ''

		while(id > allowed_chars_size - 1):
			rem = id % allowed_chars_size
			short_url = allowed_chars[rem] + short_url
			id = id / allowed_chars_size

		self.short_url = short_url
		self.save()

