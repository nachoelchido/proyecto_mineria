from django.shortcuts import render
import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from .forms import UploadFileForm

context = {}
Datos = ""

def index_v(request):
	if request.method == 'POST':
	    form = UploadFileForm(request.POST, request.FILES)
	    if form.is_valid():
	        file = request.FILES['Archivo']
	        extension = file.name.split('.')[1]
	        
	        if(extension =="csv"):
	        	Datos = pd.read_csv(file,header=None)

	        elif(extension =="txt"):
	        	Datos = pd.read_table(file)

	        elif(extension in ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']):
	        	Datos = pd.read_excel(file,header=None)

	        nombres = Datos.columns.tolist()
	        print(extension)
	        context ={'datos' : Datos, 'nombres' : nombres }
	        request.session['datos'] = Datos.to_json()
	        del Datos
	        return render(request,'carga.html',context)
	else:
	    form = UploadFileForm()
	return render(request,'index.html', {'form': form})