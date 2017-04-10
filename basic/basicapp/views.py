from django.shortcuts import render
from basicapp import forms

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS')

    return render(request,'basicapp/form.html',{'form':form})
