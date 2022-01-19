from django.shortcuts import render, redirect
from .models import Resident
from .models import Official
from .models import Blotter
from .models import Sk

def index(request):
    return render(request, 'index.html')

def create_residents(request):
    return render(request, 'create_residents.html')

def process_create_resident(request):
    full_name = request.POST.get('full_name')
    nick_name = request.POST.get('nick_name')
    birth_date = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    civil_status = request.POST.get('civil_status')
    purok = request.POST.get('purok')
    voter_status = request.POST.get('voter_status')

    resident = Resident(full_name = full_name, nick_name = nick_name, birth_date = birth_date, gender = gender, civil_status = civil_status, purok = purok, voter_status = voter_status)

    resident.save()

    return redirect('list_residents')

def list_residents(request):
    residents = Resident.objects.all()
    return render(request, 'list_residents.html', { 'residents_list' : residents })

def edit_resident(request, pk):
    resident = Resident.objects.get(pk = pk)
    return render(request, 'edit_residents.html', { 'edit_resident' : resident })

def process_edit_resident(request, pk):

    resident = Resident.objects.get(pk = pk)

    resident.full_name = request.POST.get('full_name')
    resident.nick_name = request.POST.get('nick_name')
    resident.birth_date = request.POST.get('birth_date')
    resident.gender = request.POST.get('gender')
    resident.civil_status = request.POST.get('civil_status')
    resident.purok = request.POST.get('purok')
    resident.voter_status = request.POST.get('voter_status')

    resident.save()

    return redirect('list_residents')

def process_delete_resident(request, pk):

    resident = Resident.objects.get(pk = pk)
    
    resident.delete()

    return redirect('list_residents')

def create_officials(request):
    return render(request, 'create_officials.html')

def process_create_official(request):
    full_name = request.POST.get('full_name')
    chairmanship = request.POST.get('chairmanship')
    position = request.POST.get('position')

    official = Official(full_name = full_name, chairmanship = chairmanship, position = position)

    official.save()

    return redirect('list_officials')

def list_officials(request):
    officials = Official.objects.all()
    return render(request, 'list_officials.html', { 'officials_list' : officials })

def edit_official(request, pk):
    official = Official.objects.get(pk = pk)
    return render(request, 'edit_officials.html', { 'edit_official' : official })

def process_edit_official(request, pk):

    official = Official.objects.get(pk = pk)

    official.full_name = request.POST.get('full_name')
    official.chairmanship = request.POST.get('chairmanship')
    official.position = request.POST.get('position')

    official.save()

    return redirect('list_officials')

def create_blotters(request):
    return render(request, 'create_blotters.html')

def process_create_blotter(request):
    complainant = request.POST.get('complainant')
    respondent = request.POST.get('respondent')
    victim = request.POST.get('victim')
    types = request.POST.get('types')
    location = request.POST.get('location')
    date = request.POST.get('date')
    time = request.POST.get('time')
    status = request.POST.get('status')
    details = request.POST.get('details')

    blotter = Blotter(complainant = complainant, respondent = respondent, victim = victim, types = types, location = location, date = date, time = time, status = status, details = details)

    blotter.save()

    return redirect('list_blotters')

def list_blotters(request):
    blotters = Blotter.objects.all()
    return render(request, 'list_blotters.html', { 'blotters_list' : blotters })

def edit_blotter(request, pk):
    blotter = Blotter.objects.get(pk = pk)
    return render(request, 'edit_blotters.html', { 'edit_blotter' : blotter })

def process_edit_blotter(request, pk):

    blotter = Blotter.objects.get(pk = pk)

    blotter.complainant = request.POST.get('complainant')
    blotter.respondent = request.POST.get('respondent')
    blotter.victim = request.POST.get('victim')
    blotter.types = request.POST.get('types')
    blotter.location = request.POST.get('location')
    blotter.date = request.POST.get('date')
    blotter.time = request.POST.get('time')
    blotter.status = request.POST.get('status')
    blotter.details = request.POST.get('details')

    blotter.save()

    return redirect('list_blotters')

def process_delete_blotter(request, pk):

    blotter = Blotter.objects.get(pk = pk)
    
    blotter.delete()

    return redirect('list_blotters')

def create_sks(request):
    return render(request, 'create_sks.html')

def process_create_sk(request):
    full_name = request.POST.get('full_name')
    position = request.POST.get('position')

    sk = Sk(full_name = full_name, position = position)

    sk.save()

    return redirect('list_sks')

def list_sks(request):
    sks = Sk.objects.all()
    return render(request, 'list_sks.html', { 'sks_list' : sks })

def edit_sk(request, pk):
    sk = Sk.objects.get(pk = pk)
    return render(request, 'edit_sks.html', { 'edit_sk' : sk })

def process_edit_sk(request, pk):

    sk = Sk.objects.get(pk = pk)

    sk.full_name = request.POST.get('full_name')
    sk.position = request.POST.get('position')

    sk.save()

    return redirect('list_sks')