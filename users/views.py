from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Certificate
from .forms import CertificateForm


def AboutMe(request):
    return render(request, 'AboutMe.html', {})


def certificate_view(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('certificate_list')  # 자격증 등록 후 목록으로 이동
    else:
        form = CertificateForm()

    return render(request, 'Certificate.html', {'form': form})

class CertificateListView(ListView):
    model = Certificate
    template_name = 'users/certificate_list.html'
    context_object_name = 'certificates'

def index(request):
    board_list = Certificate.objects.order_by('-create_date')
    context = {'certificates': board_list}
    return render(request, 'users/certificate_list.html', context)
def detail(request, board_id):
    certificate = Certificate.objects.get(id=board_id)
    context = {'certificate': certificate}
    return render(request, 'certificate_detail.html', context)

def ResearchProject(request):
    return render(request, 'ResearchProject.html', {})

def SchoolLife(request):
    return render(request, 'SchoolLife.html', {})
