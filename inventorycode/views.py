from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import NewInventoryForm, NewProductionForm, NewProcurementForm
from .models import Inventory, Production, Procurement


def InventoryCreate(request):
    if request.method == "POST":
        form = NewInventoryForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory Form Saved')
            return redirect('dashboard')

    form = NewInventoryForm()
    context = {
        "form": form
    }
    return render(request, 'inventory_create.html', context)


def InventoryListView(request):
    invent = Inventory.objects.all()
    context = {
        "invent": invent
    }
    return render(request, 'inventory.html', {"invent": invent})


def InventoryEdit(request, id):
    invent = get_object_or_404(Inventory, pk=id)
    if request.method == "POST":
        form = NewInventoryForm(request.POST, instance=invent)

        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory Form Updated')
            return redirect('dashboard')

    form = NewInventoryForm(instance=invent)
    context = {
        "form": form
    }
    print(form)
    return render(request, "inventory_edit.html", context)


def ProductionCreate(request):
    if request.method == "POST":
        form = NewProductionForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Production Form Saved')
            return redirect('dashboard')

    form = NewProductionForm()
    context = {
        "form": form
    }
    return render(request, 'production_create.html', context)


def ProductionListView(request):
    product = Production.objects.all()
    context = {
        "product": product
    }
    return render(request, 'production.html', context)


def ProductionEdit(request, id):
    product = get_object_or_404(Production, pk=id)
    if request.method == "POST":
        form = NewProductionForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Production Form Updated')
            return redirect('dashboard')

    form = NewProductionForm(instance=product)
    context = {
        "form": form
    }
    print(form)
    return render(request, "production_edit.html", context)


def ProcurementCreate(request):
    if request.method == "POST":
        form = NewProcurementForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Procurement Form Saved')
            return redirect('dashboard')

    form = NewProcurementForm()
    context = {
        "form": form
    }
    return render(request, 'procurement_create.html', context)


def ProcurementListView(request):
    procure = Procurement.objects.all()
    context = {
        "procure": procure
    }
    return render(request, 'procurement.html', {"procure": procure})


def ProcurementEdit(request, id):
    procure = get_object_or_404(Procurement, pk=id)
    if request.method == "POST":
        form = NewProcurementForm(request.POST, instance=procure)

        if form.is_valid():
            form.save()
            messages.success(request, 'Procurement Form Updated')
            return redirect('dashboard')

    form = NewProcurementForm(instance=procure)
    context = {
        "form": form
    }
    print(form)
    return render(request, "procurement_edit.html", context)
