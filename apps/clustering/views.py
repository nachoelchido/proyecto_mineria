from django.shortcuts import render,redirect
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator       #https://github.com/arvkevi/kneed/blob/master/kneed/   Utiliza una interpolación

def clustering_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		#del request.session['datos'] #Liberando memoria
		datos = pd.read_json(mis_datos)
		nombres = datos.columns.tolist()
		del mis_datos #Liberando memoria
		Matriz = datos.corr(method='pearson')
		context = {'matriz' : Matriz.round(4), 'nombres' : nombres}
		#Se lee si se ingresaron variables (columnas) por POST
		if request.method == 'POST':
			mis_nombres = []
			for nombre in nombres:
				if request.POST.get(nombre) != 'ninguna':
					mis_nombres.append(request.POST.get(nombre,'ninguna'))
		#Si no se ingresaron variables, se seleccionan todas las columnas
		else:
			mis_nombres = nombres

		variablesModelo = np.array(datos[mis_nombres])
		
		SSE = []
		for i in range(2, 16):
			km = KMeans(n_clusters=i, random_state=0)
			km.fit(variablesModelo)
			SSE.append(km.inertia_)

		kl = KneeLocator(range(2, 16), SSE, curve="convex", direction="decreasing")
		print("=================")
		print(kl.elbow)

		plt.figure(figsize=(10, 7))
		plt.plot(range(2, 16), SSE, marker='o')
		plt.xlabel('Cantidad de clusters *k*')
		plt.ylabel('SSE')
		plt.title('Elbow Method')

		fig = plt.gcf()
		imgdata = StringIO()
		fig.savefig(imgdata, format='svg')
		imgdata.seek(0)
		data = imgdata.getvalue()

		MParticional = KMeans(n_clusters=kl.elbow, random_state=0).fit(variablesModelo)
		MParticional.predict(variablesModelo)
		MParticional.labels_

		datos['clusterP'] = MParticional.labels_

		CentroidesP = MParticional.cluster_centers_

		context = {'matriz' : Matriz.round(4), 'nombres' : nombres, 'ideales':kl.elbow,
		'datos' : datos.round(4), 'centroides':pd.DataFrame(CentroidesP.round(4)),
		'grafico':data}
		return render(request,'clustering.html',context)
	else:
			print("hoooo")
			return redirect('/')
