from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd
from apyori import apriori

def apriori_v(request):
	if(request.session.get('datos')):
		mis_datos = request.session.get('datos')
		del request.session['datos'] #Liberando memoria
		datos = pd.read_json(mis_datos)
		del mis_datos #Liberando memoria
		rows = len(datos.index)
		columns = len(datos.columns)

		#Si hubo una solicitud en el formulario donde se indica el lift, soporte, etc.
		if request.method == 'POST':
			soporte = int(request.POST.get('soporte',''))
			soporte = soporte/rows
			confianza = int(request.POST.get('range',''))
			confianza = confianza/100
			lift = int(request.POST.get('lift',''))
			minimo_elementos = int(request.POST.get('min-elem',''))
		#Se ejecuta el algoritmo
			Transacciones = []

			for i in range(0, rows):
	  			Transacciones.append([str(datos.values[i,j]) for j in range(0, columns)])

			Reglas = apriori(Transacciones, min_support=soporte, min_confidence=confianza, min_lift=lift, min_length=minimo_elementos)
			Resultado = list(Reglas)
			del Reglas

			resultados_tabla = []

			del rows
			del columns
			del Transacciones
			del datos

			for item in Resultado:
				#Primer indice de la lista interna
				#Contiene un elemento base y agrega otro
				resultado_iter = []
				
				pair = item [0]
				items = [x for x in pair]
				print("Regla :" + items[0] + " -> " + items[1])
				resultado_iter.append(items[0])
				resultado_iter.append(items[1])
				#Segundo indice de la lista interna
				print("Soporte: " + str(item[2][0][2]))
				resultado_iter.append(item[2][0][2])
				print("Lift: " + str(item[2][0][3]))
				resultado_iter.append(item[2][0][3])
				resultados_tabla.append(resultado_iter)
				print("=======================================")
			context ={'resultados' : resultados_tabla, 'soporte' : soporte, 'confianza' : confianza*100, 'lift' : lift, 'minimo_elementos' : minimo_elementos}
			return render(request,'apriori.html',context)
		else:
			print("hoooo")
			return redirect('/')
	else:
		print("hoooo")
		return redirect('/')

		#apriori
		#caracteristicas de pearson
		#metricas similitudes