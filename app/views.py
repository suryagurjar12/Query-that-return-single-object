from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.

def home(request):
    # get(coloumn_name=value)
    # data0 = Student.objects.get(id=2) # get arguments always used primary-key coloumn
    # # data0 = Student.objects.get(stu_name="Neeraj Kumar")
    # # data0 = Student.objects.get(stu_name="Arvind singh")
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)
    
    ## first()
    # data0 = Student.objects.first()
    # # data0 = Student.objects.order_by('stu_name').first()
    # # data0 = Student.objects.order_by('-stu_name').first()
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)

    # last()
    # data0 = Student.objects.last()
    # # data0 = Student.objects.order_by('stu_name').last()
    # # data0 = Student.objects.order_by('-stu_name').last()
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)

    # # latest(*fields/Coloumn)
    # data0 = Student.objects.latest("id") # latest entry in Student table
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)

    # # earliest(*fields/Coloumn)
    # data0 = Student.objects.earliest("id") # very first entry in this Student table
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)

    # # exists()
    # data0 = Student.objects.all()
    # print(data0.exists())
    # return HttpResponse(data0)

    # # create(coloumn1=value1,coloumn2=value2)
    # data0 = Student.objects.create(stu_name='Ravi',stu_email='ravi@gmail.com',stu_city='Bhopal')
    # print(data0.id, data0.stu_name,data0.stu_city)
    # return HttpResponse(data0)

    # # get_or_create(default=None,**kwargs)
    # data0,created = Student.objects.get_or_create(stu_name='RaviSingh',stu_email='ravisingh@gmail.com',stu_city='Pune')
    # print(data0.id, data0.stu_name,data0.stu_city)
    # print(created)
    # return HttpResponse(data0)

    ## update(**kwargs)
    # data0 = Student.objects.filter(id=14).update(stu_name='Ravi Thakur',stu_city='Indore')
    # print(data0)
    # return HttpResponse(data0)
    
    ## Update Multiple objects values at a time
    # data0 = Student.objects.filter(stu_city="Bhopal").update(stu_name='Neeraj')
    # print(data0)
    # return HttpResponse(data0)

    ## Delete the given object
    # data0 = Student.objects.get(id=14).delete() or
    # data0 = Student.objects.get(id=14)
    # data0.delete()
    # data0 = Student.objects.filter(stu_name = "Neeraj").delete()
    # print(data0)
    # return HttpResponse(data0)

    ## count all no of object prasent in table
    # data0 = Student.objects.all()
    # print(data0.count()) # In terminal provide total no of objects present
    
    # data0 = Student.objects.explain()
    # print(data0)

    # # update_or_create(**kwargs,default=None)
    # data0,created = Student.objects.update_or_create(id=15, stu_city="Pune", defaults={'stu_name':"Ravi"})
    # print(data0)
    # print(created)
    # return HttpResponse(data0)
    # data = Student.objects.all()
    # print(data)

    # data1 = Student.objects.filter(id=1).update(stu_name = "Neeraj Patel")
    # print(data1)

    # data1 = Student.objects.filter(id=2).delete()
    # print(data1)       
            
    data = Student.objects.bulk_create([Student(stu_name="Neeraj",stu_email="Neeraj@gmail.com",stu_city='Indore'),Student(stu_name="Raj" ,stu_email="Raj@gmail.com",stu_city='Jabalpur'),Student(stu_name="Arvind" ,stu_email="Arvind@gmail.com",stu_city='Mandala')
    ])
    print(data)