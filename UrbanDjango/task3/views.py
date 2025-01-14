from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Service(TemplateView):
    template_name = 'third_task/service.html'


def in_work(request):
    title = 'ОБОРУДОВАНИЕ'
    device1 = 'Принтеры 1' # наименование устройства для context
    device2 = 'Сканеры 2' # наименование устройства для context
    device3 = 'МФУ 3' # наименование устройства для context
    devices = ['Принтеры HP', 'Сканеры HP', 'МФУ HP']
    context = {
        'title' : title,
        'device1' : device1, # устройство закоментировано в in_work.html вариант 1
        'device2' : device2, # устройство закоментировано в in_work.html вариант 1
        'device3' : device3, # устройство закоментировано в in_work.html вариант 1
        'devices' : devices, # в in_work.html вариант 2
    }
    return render(request, 'third_task/in_work.html', context)

def ready(request):
    return render(request, 'third_task/ready.html')
