from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from io import StringIO
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def regresion_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		datos = pd.read_json(mis_datos)
		nombres = datos.columns.tolist()
		del mis_datos #Liberando memoria
		
		if request.method == 'POST':
			var_a = request.POST.get('variable-a','')
			var_b = request.POST.get('variable-b','')
			mis_nombres = []
			columna = request.POST.get('columna','')
			for nombre in nombres:
				if request.POST.get(nombre) != 'ninguna':
					mis_nombres.append(request.POST.get(nombre,'ninguna'))
		else:
			var_a = 'M'
			var_b = 'B'
			columna = nombres[0]
			mis_nombres = nombres

		datos = datos.replace({var_a: 0, var_b: 1})
		
		print(mis_nombres)
		X = np.array(datos[mis_nombres])
		pd.DataFrame(X)
		

		Y = np.array(datos[[columna]])
		pd.DataFrame(Y)
		
		Clasificacion = linear_model.LogisticRegression()

		validation_size = 0.2
		seed = 1234
		X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed, shuffle = True)
		
		pd.DataFrame(X_train)
		pd.DataFrame(Y_train)
		Clasificacion.fit(X_train, Y_train)

		Probabilidad = Clasificacion.predict_proba(X_train)
		pd.DataFrame(Probabilidad)

		Predicciones = Clasificacion.predict(X_train)
		pd.DataFrame(Predicciones)

		exactitud = Clasificacion.score(X_train, Y_train)

		PrediccionesNuevas = Clasificacion.predict(X_validation)
		
		exactitud2 = Clasificacion.score(X_validation, Y_validation)
		reporte = classification_report(Y_validation, PrediccionesNuevas)
		
		#Se le da formato para presentar en web al reporte ya que es un string
		reporte = reporte.split("\n")
		report = []
		for line in reporte:
			temp_line = []
			temp_line = line.split()
			if temp_line != []:
				if len(temp_line) == 4:
					temp_line.insert(0, " ")
				elif len(temp_line) == 3:
					temp_line.insert(1, " ")
					temp_line.insert(2, " ")
				if temp_line[1] == 'avg':
					temp_line.remove('avg')
				report.append(temp_line)
		print(report)
			
		context = {'datos':datos, 'a':var_a,'b':var_b,'columna':columna,
		'probabilidad':pd.DataFrame(Probabilidad),'predicciones':pd.DataFrame(Predicciones),
		'exactitud':exactitud, 'predicciones2':pd.DataFrame(PrediccionesNuevas),
		'exactitud2':exactitud2, 'reporte':report
		}
		return render(request,'regresion.html',context)
	else:
			print("hoooo")
			return redirect('/')