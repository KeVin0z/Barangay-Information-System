from django.shortcuts import render, redirect
from .models import Resident
from .models import Official
from .models import Blotter
from .models import Sk
from django.core.files.storage import FileSystemStorage
import os



def index(request):
    pb = Official.objects.get(position = 'Punong Barangay')
    appro = Official.objects.get(chairmanship = 'COMMITTEE ON APPROPRIATION')
    pw = Official.objects.get(chairmanship = 'COMMITTEE ON PUBLIC WORKS')
    ch = Official.objects.get(chairmanship = 'COMMITTEE ON HEALTH')
    ag = Official.objects.get(chairmanship = 'COMMITTEE ON AGRICULTURE')
    ev = Official.objects.get(chairmanship = 'COMMITTEE ON ENVIRONMENT')
    ed = Official.objects.get(chairmanship = 'COMMITTEE ON EDUCATION')
    po = Official.objects.get(chairmanship = 'COMMITTEE ON PEACE & ORDER')
    sk = Official.objects.get(chairmanship = 'SANGGUNIANG KABATAAN')
    bs = Official.objects.get(position = 'Barangay Secretary')
    bt = Official.objects.get(position = 'Barangay Treasurer')
    bh = Official.objects.get(position = 'BHW President')
    ct = Official.objects.get(position = 'Chief Tanod')
    dcw = Official.objects.get(position = 'Day Care Worker')
    return render(request, 'index.html', { 'pb' : pb, 'appro' : appro, 'pw' : pw, 'ch' : ch, 'ag' : ag, 'ev' : ev, 'ed' : ed, 'po' : po, 'sk' : sk, 'bs' : bs, 'bt' : bt, 'bh' : bh, 'ct' : ct, 'dcw' : dcw })

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

    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

    official = Official(image = uploaded_file_url, full_name = full_name, chairmanship = chairmanship, position = position)

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

    if request.FILES.get('image',False):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        if os.path.isfile(os.getcwd()+official.image):
            os.remove(os.getcwd()+official.image)
        official.image = fs.url(filename)

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

def list_residents_bc(request):
    residents_bc = Resident.objects.all()
    return render(request, 'list_residents_bc.html', { 'list_residents_bc' : residents_bc })

def gbc_resident(request, pk):
    resident_bc = Resident.objects.get(pk = pk)
    pb = Official.objects.get(position = 'Punong Barangay')
    return render(request, 'barangay_clearance.html', { 'gbc_resident' : resident_bc, 'pb' : pb })

def list_residents_cr(request):
    residents_cr = Resident.objects.all()
    return render(request, 'list_residents_cr.html', { 'list_residents_cr' : residents_cr })

def gcr_resident(request, pk):
    resident_cr = Resident.objects.get(pk = pk)
    pb = Official.objects.get(position = 'Punong Barangay')
    return render(request, 'certificate_residency.html', { 'gcr_resident' : resident_cr, 'pb' : pb })

def list_residents_ci(request):
    residents_ci = Resident.objects.all()
    return render(request, 'list_residents_ci.html', { 'list_residents_ci' : residents_ci })

def gci_resident(request, pk):
    resident_ci = Resident.objects.get(pk = pk)
    pb = Official.objects.get(position = 'Punong Barangay')
    return render(request, 'certificate_indigency.html', { 'gci_resident' : resident_ci, 'pb' : pb })

