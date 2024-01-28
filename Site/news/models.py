from django.db import models
# Create your models here.
class int_info(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	function_name=models.CharField(max_length=100)
	function_description=models.TextField(blank=True)
	function_input=models.JSONField(max_length=255, null=True)
	function_tags=models.JSONField(max_length=255, null=True)
	function_function=models.TextField(blank=True)
	class Meta:
		db_table = 'int_info'
class users(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=28)
	surname=models.CharField(max_length=28)
	email_address = models.EmailField(null=True)
	points=models.IntegerField()
	class Meta:
		db_table = 'users'
class tag(models.Model):
	name=models.CharField(max_length=32)
	points=models.IntegerField()
	class Meta:
		db_table = 'tag'