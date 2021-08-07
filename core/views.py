from django.shortcuts import render,HttpResponse
import requests
import json
# Create your views here.




def home(request):
	return render(request,"core/home.html")

def about(request):
	return render(request,"core/about.html")

def contact(request):
	return render(request,"core/contact.html")

def algoritmo(request):
	url = 'https://cloudxapi.herokuapp.com/cluster/EM';
	datos = []
	params = {}
	if  request.POST.get('query'):
		
		params = {
				"queryBD": request.POST.get('query'),
				"numFolds": request.POST.get('numFolds'),
				"numKMeansRuns": request.POST.get('numKMeansRuns'),
				"maximumNumberOfClusters": request.POST.get('maximumNumberOfClusters'),
				"numClusters": request.POST.get('numClusters'),
				"maxIterations": request.POST.get('maxIterations')
			};

		response = generate_request(url,params)

		if response:
			datos = response
	

	return render(request,"core/algoritmo.html",{'datos':datos,'datos_Form':params})


def generate_request(url, params={}):
	dataJson = False
	_headers = {"Content-Type":"application/json"}
	response = requests.post(url,data=json.dumps(params),headers = _headers)
	if response.status_code == 200:
		dataJson = response.json()

	return dataJson

