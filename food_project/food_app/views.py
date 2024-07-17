from django.shortcuts import redirect, render
from .models import Food
from .forms import FoodForm
import datetime


def food_form(request):
    template_name = 'food_app/form.html'
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)


def food_data(request):
    template_name = 'food_app/data.html'
    objs = Food.objects.all()
    context = {'objs': objs}
    return render(request, template_name, context)


def food_update(request, pk):
    obj = Food.objects.get(pk=pk)
    template_name = 'food_app/form.html'
    form = FoodForm(instance=obj)
    if request.method == 'POST':
        instance = obj
        instance.updated_at = datetime.datetime.now()
        form = FoodForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)

def food_delete(request, pk):
    obj = Food.objects.get(pk=pk)
    template_name = 'food_app/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('data_url')
    context = {'obj': obj}
    return render(request, template_name, context)
