from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm
from django.contrib import messages


# Create your views here.


def home(request):

    context = {}
    return render(request, "core/home.html", context)


def dashboard(request):
    records = Record.objects.filter(created_by=request.user)
    context ={
        "records": records
    }
    return render(request, "core/dashboard.html", context)


def create_record(request):
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            messages.success(request, f"New Record created successfully")
            return redirect("core:dashboard")

    context = {
        "form": form,
        "title": "Add New Record"
    }
    return render(request, "core/record_form.html", context)


def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)

    context = {
        "record": record
    }

    return render(request, "core/record_detail.html", context)


def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk, created_by=request.user)

    form = RecordForm(instance=record)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record Updated Successfully")
            return redirect("core:record-detail", pk=pk)

    context = {
        "title": "update Record",
        "form": form
    }
    return render(request, "core/record_form.html", context)


def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk, created_by=request.user)

    if request.method == "POST":
        record.delete()
        return redirect("core:dashboard")

    context = {"record": record}
    return render(request, "core/delete_record.html", context)
