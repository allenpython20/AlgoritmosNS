from django.shortcuts import render,HttpResponse
import requests
import json
# Create your views here.

def algoritmo(request):
	url = 'https://cloudxapi.herokuapp.com/cluster/EM';
	datos = True
	params = {}
	if  request.POST.get('query'):
		body = request.POST
		params = {
				"queryBD": body.get('query').strip(),
				"numFolds": body.get('numFolds'),
				"numKMeansRuns": body.get('numKMeansRuns'),
				"maximumNumberOfClusters": body.get('maximumNumberOfClusters'),
				"numClusters": body.get('numClusters'),
				"maxIterations": body.get('maxIterations')
			};

		response = generate_request(url,params)
		if response != False:
			(response['valsInstances']).sort(key=lambda ins: int(ins['instancia'][0]))
			datos = [response['attributes'],response['valsInstances'],response['infoCluster'],response['graph']]
		else:
			datos = None
		
	return render(request,"core/algoritmo.html",{'datos':datos,'datos_Form':params})


def generate_request(url, params={}):
	dataJson = False
	_headers = {"Content-Type":"application/json"}
	response = requests.post(url,data=json.dumps(params),headers = _headers)
	if response.status_code == 200:
		dataJson = response.json()

	return dataJson

