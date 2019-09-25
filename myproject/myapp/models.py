from django.db import models

# Create your models here.
class Users(models.Model):
	user_name = models.CharField(max_length = 50)
	user_phone = models.CharField(max_length = 15)
	user_email = models.EmailField()
	user_password = models.CharField(max_length = 100)
	user_address = models.TextField()
	user_privelage = models.TextField()
	user_status = models.SmallIntegerField(default = 1)

	def check_email_exist(self):
		return True
