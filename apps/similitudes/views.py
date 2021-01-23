from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from scipy.spatial import distance

def similitudes_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		del request.session['datos'] #Liberando memoria
		datos = pd.read_json(mis_datos)
		del mis_datos #Liberando memoria
		rows = len(datos.index)
		columns = len(datos.columns)
		Matriz_euclidiana = []
		for i in range (1,rows):
			lista_temp = []
			for j in range (1,columns):
				E1 = np.array(pd.to_numeric(datos.iloc[i], downcast='float'))
				E2 = np.array(pd.to_numeric(datos.iloc[j], downcast='float'))
				datos_temp = distance.euclidean(E1,E2)
				lista_temp.append(datos_temp)
		Matriz_euclidiana.append(lista_temp)

		context = {'euclidiana': Matriz_euclidiana ,'nombre' : 'Nacho'}
		return render(request,'similitudes.html',context)
	else:
			print("hoooo")
			return redirect('/')
