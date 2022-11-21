from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from .models import *
from .models import DemandeStageBinome



# Create your views here.
def home(request):
    return render(request,'index.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("gestionpfe:home")
	form = NewUserForm()
	return render (request=request, template_name="register/signup.html", context={"register_form":form})
    

def monome(request):
    user=0
    re='parts/monome.html'
    if request.method == "POST":
        cin1=request.POST.get('cin')
        email1=request.POST.get('email')
        parcour1=request.POST.get('parcours')
        nom1=request.POST.get('nom')
        prenom1=request.POST.get('prenom')
        DemandeStageMonome.objects.create(userun=request.user,nom=nom1,prenom=prenom1,ncin=cin1,parcours=parcour1,email=email1)
        return render(request,'parts/document.html',{"cin":cin1,"nom":nom1,"prenom1":prenom1,"parcour":parcour1,"email":email1})
    try:
        user=DemandeStageMonome.objects.get(userun=request.user)
        re='parts/updatemonome.html'
    except:
        pass
    return render(request,re,{'user':user})

def updateDatamonome(request):
    if request.method == "POST":
        user=DemandeStageMonome.objects.get(userun=request.user)
        user.nom=request.POST.get('nom')
        user.prenom=request.POST.get('prenom')
        user.ncin=request.POST.get('cin')
        user.parcours=request.POST.get('parcours')
        user.email=request.POST.get('email')
        user.save()
        return render(request,'parts/document4.html',{'user':user})
  

def binome(request):
    user=0
    temp='parts/binome.html'
    if request.method == "POST":
        ncin1=request.POST.get('cin1')
        mail=request.POST.get('mail1')
        parcour=request.POST.get('parcours1')
        nome=request.POST.get('nom1')
        prenome=request.POST.get('prenom1')
        ncinn=request.POST.get('cin2')
        maill=request.POST.get('mail2')
        parcourr=request.POST.get('parcours2')
        nomm=request.POST.get('nom2')
        prenomm=request.POST.get('prenom2')
        DemandeStageBinome.objects.create(binome1=request.user,nom=nome,prenom=prenome,ncin=ncin1,parcours=parcour,email=mail,nom2=nomm,prenom2=prenomm,ncin2=ncinn,parcours2=parcourr,email2=maill)
        return render(request,'parts/document2.html',{"cin1":ncin1,"nom1":nome,"prenom1":prenome,"parcours1":parcour,"email1":mail,"cin2":ncinn,"nom2":nomm,"prenom2":prenomm,"parcours2":parcourr,"email2":maill})
    try:
        user=DemandeStageBinome.objects.get(binome1=request.user)
        temp='parts/update.html'
    except :
        pass
    return render(request,temp,{'user':user})  


def updateDatabinome(request):
    if request.method == "POST":
        user=DemandeStageBinome.objects.get(binome1=request.user)
        user.nom=request.POST.get('nom1')
        user.prenom=request.POST.get('prenom1')
        user.ncin=request.POST.get('cin1')
        user.parcours=request.POST.get('parcours1')
        user.email=request.POST.get('mail1')
        user.nom2=request.POST.get('nom2')
        user.prenom2=request.POST.get('prenom2')
        user.ncin2=request.POST.get('cin2')
        user.parcours2=request.POST.get('parcours2')
        user.email2=request.POST.get('mail2')
        user.save()
        return render(request,'parts/document3.html',{'user':user})

def cahierC(request):
    return render(request,'parts/CahierCharge.html')


    

    

        
    


 

        
	    
     
    
        
	   
	
   


    
    
    
        
    

