from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from scipy.spatial import distance

def similitudes_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		datos = pd.read_json(mis_datos)
		del mis_datos #Liberando memoria
		Matriz_euclidiana = []
		Matriz_chebyshev = []
		Matriz_manhattan = []
		Matrix_minkowski = []
		for i in range (0,datos.shape[0]):
			temp_euc = []
			temp_cheb = []
			temp_manh = []
			temp_mink = []
			for j in range (0,datos.shape[0]):
				E1 = np.array(pd.to_numeric(datos.iloc[i], downcast='float'))
				E2 = np.array(pd.to_numeric(datos.iloc[j], downcast='float'))
				temp_euc.append(distance.euclidean(E1,E2))
				temp_cheb.append(distance.chebyshev(E1,E2))
				temp_manh.append(distance.cityblock(E1,E2))
				temp_mink.append(distance.minkowski(E1,E2))
			Matriz_euclidiana.append(temp_euc)
			Matriz_chebyshev.append(temp_cheb)
			Matriz_manhattan.append(temp_manh)
			Matrix_minkowski.append(temp_mink)

		print(Matriz_euclidiana)

		context = {'euclidiana': Matriz_euclidiana, 'cheb' : Matriz_chebyshev,
		'manh' : Matriz_manhattan, 'mink' : Matrix_minkowski}
		return render(request,'similitudes.html',context)
	else:
			print("hoooo")
			return redirect('/')
