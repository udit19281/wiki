from django.shortcuts import render
from django.core.files.storage import default_storage
from . import util
from markdown2 import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getpage(request,name):
    if(util.get_entry(name)!=None):
            f = default_storage.open(f"entries/{name}.md")
            with open(f"entries/{name}.md","r") as markdown_file:
              article=markdown(markdown_file.read())
            fi=open(f"encyclopedia/templates/encyclopedia/{name}.html","w")
            preload="{% extends 'encyclopedia/layout.html' %}{% block title %}"+name+"{% endblock %}{% block body %}"+article+"{% endblock %}"
            fi.write(preload)
            fi.close()
            #print(article)
            return render(request,f"encyclopedia/{name}.html")
    else :
        return index(request)

def searchme(request):
  if request.method =="POST":
    query=request.POST.get("q")
    return getpage(request,query)

def create(request):
   if request.method =="POST":
     title=request.POST.get("title")
     content=request.POST.get("content")
     util.save_entry(title,content)
     return index(request)
   else:
      return render(request,"encyclopedia/create.html")
