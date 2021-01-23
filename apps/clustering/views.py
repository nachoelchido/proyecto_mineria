from django.shortcuts import render,redirect
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

def clustering_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		#del request.session['datos'] #Liberando memoria
		datos = pd.read_json(mis_datos)
		nombres = datos.columns.tolist()
		print(nombres[1])
		del mis_datos #Liberando memoria
		Matriz = datos.corr(method='pearson')
		context = {'matriz' : Matriz.round(4), 'nombres' : nombres}
		plt.matshow(Matriz)
		fig = plt.gcf()
		imgdata = StringIO()
		fig.savefig(imgdata, format='svg')
		imgdata.seek(0)
		data = imgdata.getvalue()
		
		if request.method == 'POST':
			var_a = request.POST.get('variable-a','')
			var_b = request.POST.get('variable-b','')
		else:
			var_a = datos.columns[0]
			var_b = datos.columns[1]

		print("*************")
		print(var_a)
		print(var_b)
		print("*************")

		plt.clf()
		plt.plot(datos[var_a],datos[var_b], 'bo')
		plt.ylabel(var_a)
		plt.xlabel(var_b)


		fig2 = plt.gcf()
		imgdata2 = StringIO()
		fig2.savefig(imgdata2, format='svg')
		imgdata2.seek(0)
		data2 = imgdata2.getvalue()

		context = {'matriz' : Matriz.round(4), 'nombres' : nombres, 'graph' : data, 'lineal' : data2, 'var_a' : var_a, 'var_b' : var_b}
		return render(request,'pearson.html',context)
	else:
			print("hoooo")
			return redirect('/')
