from app.wsgi import *
from core.erp.models import Type
from core.erp.models import Employee

#Listar
#query = Type.objects.all() #Similar a SELECT * FROM
#print(query)

#Insert
#t = Type(name='Presidente')
#t.save()

#Listar
#query = Type.objects.all()
#print(query)

#Edicion
#t = Type.objects.get(id=1)
#print(t.name)

#Edicion
#t = Type.objects.get(pk=1)
#print(t.name)

#Manejo de Excepciones
#try:
#    t = Type.objects.get(pk=1)
#    t.name = "Presidente"
#    t.save()
#except Exception as e:
#    print(e)


#Listar por filtros
#obj = Type.objects.filter(name__icontains='pre')
#obj = Type.objects.filter(name__starswith='pre')
#obj = Type.objects.filter(name__endswith='pre')
#obj = Type.objects.filter(name__in=['Presidente']).count()
#obj = Type.objects.filter(name__icontains='pre').query
#obj = Type.objects.filter(name__contains='pre').query
#obj = Type.objects.filter(name__icontains='pre').exclude(id=6)
#print(obj)

for i in Type.objects.filter(name__endswith='e'):
    print(i.name)

#Consulta por medio de Llave Foranea
obj = Employee.objects.filte(type_id=1)
