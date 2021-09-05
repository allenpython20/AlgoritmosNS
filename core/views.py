from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator
import requests
import json
# Create your views here.

def carga_info(request,cluster):
	datos = request.session['datos_api']
	clusters = datos[1]
	clusters = list( filter( lambda ins: int(ins['instancia'][0]) == cluster , clusters) )
	print(clusters , "\n")
	datos = [datos[0],clusters]
	return render(request,"core/info-cluster.html",{'datos':datos,'cluster':cluster,'clusters':clusters})


def algoritmo(request):
	url = 'https://cloudxapi.herokuapp.com/cluster/EM';
	datos = True
	params = {}
	pagina_actual = 0
	paginas = 0
	posts = []
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
		# if response != False:
		# 	(response['valsInstances']).sort(key=lambda ins: int(ins['instancia'][0]))
		# 	paginator = Paginator(response['valsInstances'],5)
		# 	pagina = request.GET.get("page") or 1
		# 	posts = paginator.get_page(pagina)
		# 	pagina_actual = int(pagina)
		# 	paginas = range(1,posts.paginator.num_pages + 1)
		# 	datos = [response['attributes'],posts,response['infoCluster'],response['graph']]
		# 	request.session['datos_api'] = datos
		if response != False:

			(response['valsInstances']).sort(key=lambda ins: int(ins['instancia'][0]))
			(response['AttSummaryPanel']).sort( key=lambda ins: int(ins[2]) ,reverse=True )
			request.session['datos_api'] =  [ response['attributes'] ,response['valsInstances'] ]
			datos = [response['attributes'],response['valsInstances'],response['infoCluster'],response['graph'],response['AttSummaryPanel']]

			# datos_figura = list()

			# for i in response['AttSummaryPanel']:
			# 	print(i)


			# print(response['AttSummaryPanel'])
		else:
			datos = None

	# elif request.session['query_instancias']  is not None:
	# 	paginator = Paginator(request.session['query_instancias'],5)
	# 	pagina = request.GET.get("page") or 1
	# 	posts = paginator.get_page(pagina)
	# 	pagina_actual = int(pagina)
	# 	paginas = range(1,posts.paginator.num_pages + 1)
	# 	datos = request.session['datos_api']

		
	#return render(request,"core/algoritmo.html",{'datos':datos,'datos_Form':params,"pagina_actual":pagina_actual,"paginas":paginas,"posts":posts})
	return render(request,"core/algoritmo.html",{'datos':datos,'datos_Form':params})


def generate_request(url, params={}):
	dataJson = False
	_headers = {"Content-Type":"application/json"}
	response = requests.post(url,data=json.dumps(params),headers = _headers)
	if response.status_code == 200:
		dataJson = response.json()

	return dataJson

