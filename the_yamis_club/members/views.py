from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  miembro = Member.objects.all().values()
  columna_firstname = Member.objects.values_list('firstname')
  espe = Member.objects.filter(firstname='Yamith', lastname='Rosas').values()
  mydata = Member.objects.filter(Q(firstname='Elyan') | Q(firstname='Davidson')).values()
  ski=Member.objects.filter(firstname__startswith='L').values()
  tilin = Member.objects.filter(lastname__icontains='ez').values()
  xd = Member.objects.filter(firstname__endswith='s').values()
  nose = Member.objects.filter(id__range=(2, 4)).values()
  alo = Member.objects.filter(id__lte=3).values()
  order_by = Member.objects.all().order_by('firstname').values()
  order_by_desc = Member.objects.all().order_by('-firstname').values()
  
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
    'miembros' : miembro,
    'columna_firstname': columna_firstname,
    'espe': espe,
    'mydata': mydata,
    'tilin': tilin,
    'ski': ski,
    'xd': xd,
    'nose': nose,
    'alo': alo,
    'order_by': order_by,
    'order_by_desc': order_by_desc,
  }
  return HttpResponse(template.render(context, request))