from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from app.models import Register, CandidateInfo
import hashlib
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.base import SessionBase

def index(request):
    #return render_to_response("index.html", context_instance = RequestContext(request))
	return render(request, "index.html", {})

def register(request):
	if request.method == "POST":
		fname = request.POST['fullname']
		uname = request.POST['username']
		pword = request.POST['password']
		#password = hashlib.md5(pword).hexdigest()
		#print(password)
		eid = request.POST['emailid']
		checkuser = Register.objects.filter(emailid = eid).exists()
		if checkuser == True:
			#return render_to_response("register.html", {'mess': 'Email id already in use.Please check another emailid', 'status': 'False'}, context_instance=RequestContext(request))
			return render(request, "register.html", {'mess': 'Email id already in use.Please check another emailid', 'status': 'False'})
		print(checkuser)
		if checkuser == False:
			registersers = Register(
				fullname= fname,
				username = uname,
				#password = md5_crypt.encrypt(pword),
				#password = hashlib.md5(pword),
				#password = hashlib.new(pword).hexdigest(),
				password = pword,
				emailid = eid
			)
			registersers.save()
			return render(request, "login.html", {'mess': 'Registration successfully','status':'True'})

	#return render_to_response("register.html", context_instance = RequestContext(request))
	return render(request, "register.html", {})

def login(request):
	if request.method == 'POST':
		check_count = Register.objects.count()
		if check_count > 0:
			username = request.POST['username']
			password = request.POST['password']
			checkuser = Register.objects.filter(emailid = username).exists()
			if checkuser == True:
				checkuser = Register.objects.get(emailid = username)
				if  username == checkuser.emailid.strip() and password == checkuser.password:
					request.session['sessionuser'] = username
					getuserInfo = CandidateInfo.objects.filter(email = request.session['sessionuser'])
					if getuserInfo:
						getlogindata=getuserInfo[0]
						#return render_to_response("edit-profile.html", {'mess': 'login successfully','status':'True', 'data':getlogindata}, context_instance=RequestContext(request))
						return render(request, "edit-profile.html", {'mess': 'login successfully', 'status': 'True',
																		'data': getlogindata})
					else:
						#return render_to_response("edit-profile.html", {'mess': 'login successfully','status':'True'}, context_instance=RequestContext(request))
						return render(request, "edit-profile.html", {'mess': 'login successfully', 'status': 'True'})
				else:
					#return render_to_response("login.html", {'mess': 'Invalid Userid or Password', 'status':'False'},context_instance=RequestContext(request))
					return render(request, "login.html", {'mess': 'Invalid Userid or Password', 'status': 'False'})
			else:
				#return render_to_response("login.html", {'mess': 'Invalid Username', 'status':'False'},context_instance=RequestContext(request))
				return render(request, "login.html", {'mess': 'Invalid Username', 'status': 'False'})
		else:
			#return render_to_response("register.html", {'mess': 'First Registeruser', 'status':'False'},context_instance=RequestContext(request))
			return render(request, "register.html", {'mess': 'First Registeruser', 'status': 'False'})
			
	return render(request, "login.html", {})

def contact(request):
    return render_to_response("contact-us.html", context_instance = RequestContext(request))

def about(request):
    return render_to_response("about-us.html", context_instance=RequestContext(request))

def listview(request):

    return render_to_response("candidate-listing.html", context_instance=RequestContext(request))

def edit_profile(request):
    personalinfo = CandidateInfo.objects.filter(email=request.session["sessionuser"])
    return render(request, "edit-profile.html", {"data": personalinfo[0]})

def profile(request):
	if request.method == 'POST':
		getsessionuser = request.session['sessionuser']
		checkuser = CandidateInfo.objects.filter(email = getsessionuser).exists()
		if checkuser == True:
			getuserprofileInfo = CandidateInfo.objects.filter(email = request.session['sessionuser'])
			print (getuserprofileInfo)
			getprofiledata=getuserprofileInfo[0]
			#return render_to_response("edit-profile.html", {'mess': 'login successfully','status':'True', 'data':getprofiledata}, context_instance = RequestContext(request))
			return render(request, "edit-profile.html",
									  {'mess': 'login successfully', 'status': 'True', 'data': getuserprofileInfo})
		username = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		website = request.POST['website']
		address = request.POST['address']
		designation = request.POST['designation']
		experience = request.POST['experience']
		age = request.POST['age']
		current = request.POST['current']
		demand = request.POST['demand']
		edulevel = request.POST['edulevel']
		uploadcv = request.FILES['uploadcv']
		fs = FileSystemStorage()
		filename_cv = fs.save(uploadcv.name, uploadcv)
		uploaded_file_url = fs.url(filename_cv)
		print('URL', uploaded_file_url )
		aboutme = request.POST['aboutme']
		skill = request.POST['skill']
		skilllevel = request.POST['skilllevel']
		degreename = request.POST['degreename']
		degreedate = request.POST['degreedate']
		aboutdeg = request.POST['aboutdeg']
		company = request.POST['company']
		webcom = request.POST['webcom']
		join_frm = request.POST['join_frm']
		endon = request.POST['endon']
		location = request.POST['location']
		about_company = request.POST['about_company']
		projname = request.POST['projname']
		startfrm = request.POST['startfrm']
		projendon = request.POST['endon2']
		projdesc = request.POST['projdesc']
		project_file = request.FILES['project_file']
		projectfs = FileSystemStorage()
		filename = projectfs.save(project_file.name, project_file)
		project_file_url = fs.url(filename)
		fb = request.POST['fb']
		twitter = request.POST['twitter']
		gplus = request.POST['gplus']
		linkedin = request.POST['linkedin']
		pinterest = request.POST['pinterest']
		behance = request.POST['behance']
		profileInfo = CandidateInfo(
			username=username,
			email=email,
			phone=phone,
			website=website,
			address=address,
			designation=designation,
			experience=experience,
			age=age,
			current_salary=current,
			expected_salary=demand,
			edulevel=edulevel,
			uploadcv=uploadcv,
			cv_path=uploaded_file_url,
			aboutme=aboutme,
			skill_name=skill,
			skill_level=skilllevel,
			degree_name=degreename,
			degree_date=degreedate,
			about_degree=aboutdeg,
			company=company,
			company_website=webcom,
			join_from=join_frm,
			endon=endon,
			location=location,
			about_company=about_company,
			project_name=projname,
			project_start=startfrm,
			project_end=projendon,
			project_desc=projdesc,
			project_file=project_file,
			project_file_path=project_file_url,
			facebook=fb,
			twitter=twitter,
			google_plus=gplus,
			linkedin=linkedin,
			pinterest=pinterest,
			behance=behance		
		)
		profileInfo.save()
		print('Session',request.session['sessionuser'])
		getuserInfo = CandidateInfo.objects.filter(email = request.session['sessionuser'])
		#get_data = CandidateInfo.objects.get(email=request.session['sessionuser'])
		#get_data = CandidateInfo.objects.get(email=request.session['sessionuser'])
		#print('DATA', get_data.project_desc)
		#return render_to_response("edit-profile.html", {'status': 'True', 'mess':'Personal Information successfully saved !','data':getuserInfo,'user':username,'url':uploaded_file_url},context_instance = RequestContext(request))
		return render(request, "edit-profile.html",
								  {'status': 'True', 'mess': 'Personal Information successfully saved !', 'data': getuserInfo, 'user': username, 'url': uploaded_file_url})
	else:
		#return render_to_response("edit-profile.html", context_instance = RequestContext(request))
		return render(request, "edit-profile.html", {})

def candidatedetail(request):
	#return render_to_response("candidate-detail.html", context_instance = RequestContext(request))
    return render(request, "candidate-detail.html", {})

def logout_alt(request, *args, **kwargs):
	for sesskey in request.session.keys():
		print('key',sesskey)
		del request.session[sesskey]
	return original_logout(request, *args, **kwargs)

def profile_retrive(request):
	getuserInfo = CandidateInfo.objects.all().filter(email = request.session['sessionuser'])
	print(getuserInfo)
	return render(request, "candidate-detail.html", {'data':getuserInfo})
	
	
def logout(request):
	if request.method == 'POST':
		Session.objects.all().delete()
		return render(request, "index.html", {'status':'True', 'mess':'Logout successfully !'})
		del request.session[sessionuser]
		print('del',request.session['sessionuser'] )
		if request.session['sessionuser'] == None:
			Session.objects.all().delete()
			#request.session['username'] = No
			del request.session['username']
			del request.session['email'] 
			del request.session['phone']
			del request.session['website']
			del request.session['address']
			del request.session['designation']
			del request.session['experience']
			del request.session['age'] 
			del request.session['current']
			del request.session['demand'] 
			del request.session['edulevel']
			del request.session['uploaded_file_url'] 
			del request.session['skill']
			del request.session['skilllevel']
			del request.session['degreename']
			del request.session['degreedate']
			del request.session['aboutdeg']
			del request.session['company']
			del request.session['webcom']
			del request.session['join_frm']
			del request.session['endon']
			del request.session['location'] 
			del request.session['about_company']
			del request.session['projname']
			del request.session['startfrm']
			del request.session['projendon']
			del request.session['project_file_url']
			del request.session['fb']
			del request.session['twitter']
			del request.session['gplus']
			del request.session['linkedin']
			del request.session['pinterest']
			del request.session['behance']
			return render(request, "index.html", {'status':'True', 'mess':'Logout successfully !'})
		else:
			return render(request, "index.html", {})
			
	return render(request, "index.html", {})

def resetpassword(request):
	if request.method == 'POST':
		email = request.session['sessionuser']
		print('0000000000000', email)
		oldpassword = request.POST['oldpassword']
		getoldpasswordfromdb = Register.objects.get(email=email)
		if oldpassword == getoldpasswordfromdb:
			passwordchanged = Register(
				password=oldpassword
			)
			passwordchanged.save()
			return render_to_response("resetpassword.html", {'status': 'True', 'mess': 'Password changed successfully'}, content_type = RequestContext(request))
		else:
			return render_to_response("resetpassword.html", {'status': 'False', 'mess': 'Old password not match'}, content_type = RequestContext(request))
		newpassword = request.POST['password']
		confirmpassword = request.POST['confirmpassword']
		if confirmpassword != newpassword:
			return render_to_response("resetpassword.html", {'status':'False', 'mess':'ConfirmPassword not match with NewPassword'}, content_type = RequestContext(request))

	return render_to_response("resetpassword.html", context_instance = RequestContext(request))
#
# Create your views here.
