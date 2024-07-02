from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import TodoList
from .forms import CreateNewList

@login_required
def list(request, id):
    ls = TodoList.objects.get(id=id)

    if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Inválido.")
            return redirect("/%i" % ls.id)

    return render(request, "main/list.html", {"ls": ls})

def home(request):
    return render(request, 'main/home.html')

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            todo = TodoList(name=name)
            todo.save()
            request.user.todolist.add(todo)
            return redirect("/%i" % todo.id)
    else:
        form = CreateNewList()

    return render(request, "main/create.html", {"form": form})

@login_required
def view(request):
    return render(request, "main/view.html", {})
