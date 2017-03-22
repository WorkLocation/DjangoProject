from django.db import models

class Register(models.Model):

    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    emailid = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
	
    def __str__(self):
        return self.username
    def __str__(self):
        return self.password

    class Meta:
        db_table = "registered_users"
		
class CandidateInfo(models.Model):
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=70, null=True, blank=True, unique=True)
	phone = models.CharField(max_length=50)
	website = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)
	experience = models.CharField(max_length=50)
	age = models.CharField(max_length=50)
	current_salary = models.CharField(max_length=50)
	expected_salary = models.CharField(max_length=50)
	edulevel = models.CharField(max_length=50)
	uploadcv = models.CharField(max_length=255, blank=True)
	#document = models.FileField(upload_to='documents/')
	cv_path = models.CharField(max_length=255, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	aboutme = models.CharField(max_length=50)
	skill_name = models.CharField(max_length=50)
	skill_level = models.CharField(max_length=50)
	degree_name = models.CharField(max_length=50)
	degree_date = models.CharField(max_length=50)
	about_degree = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	company_website = models.CharField(max_length=50)
	join_from = models.CharField(max_length=50)
	endon= models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	about_company = models.CharField(max_length=50)
	project_name = models.CharField(max_length=50)
	project_start = models.CharField(max_length=50)
	project_end = models.CharField(max_length=50)
	project_desc = models.CharField(max_length=50)
	project_file = models.CharField(max_length=255, blank=True)
	project_file_path = models.FileField(max_length=255, blank=True)
	project_uploaded_at = models.DateTimeField(auto_now_add=True)
	facebook = models.CharField(max_length=50)
	twitter = models.CharField(max_length=50)
	google_plus = models.CharField(max_length=50)
	linkedin = models.CharField(max_length=50)
	pinterest = models.CharField(max_length=50)
	behance = models.CharField(max_length=50)
	def __str__(self):
		return self.username
	class Meta:
		db_table = "PersonalInfo"
# Create your models here.
