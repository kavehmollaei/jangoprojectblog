from learning_logs.models import Topic
from django.shortcuts import render
from .models import Topic,Person




# Create your views here.
def index(request):
    return  render(request,"learning_logs/index.html")


def topics(request):
        topics = Topic.objects.order_by("date_added")
        context = {"topics":topics}
        return render(request,"learning_logs/topics.html",context)


def person(request):
    person_info = Person.objects.all()
    fname_info = [i.name for i in person_info]
    print(fname_info)
    # context = {"Persons":person_info}
    lst = [1,2,3]
    context_fname ={"fname": fname_info,"lname":lst}
    return render(request,"learning_logs/personal.html",context_fname)        


