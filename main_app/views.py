import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Phone, Accessory, Photo
from .forms import RepairForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def phones_index(request):
    phones = Phone.objects.filter(user=request.user)
    return render(request, 'phones/index.html', {
        'phones' : phones
    })

@login_required
def phones_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    id_list = phone.accessory.all().values_list('id')
    accessories_phone_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    repair_form = RepairForm()
    return render(request, 'phones/detail.html', 
        {'phone' : phone, 'repair_form' : repair_form,
        'accessory' : accessories_phone_doesnt_have
    })

@login_required
def add_photo(request, phone_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, phone_id=phone_id)  
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('phone_detail', phone_id=phone_id)  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def assoc_accessory(request, phone_id, accessory_id):
    Phone.objects.get(id=phone_id).accessory.add(accessory_id)
    return redirect('detail', phone_id=phone_id)

@login_required
def remove_accessory(request, phone_id, accessory_id):
    Phone.objects.get(id=phone_id).accessory.remove(accessory_id)
    return redirect('detail', phone_id=phone_id)

@login_required
def add_repair(request,phone_id):
    form = RepairForm(request.POST)
    if form.is_valid():
        new_repair = form.save(commit=False)
        new_repair.phone_id = phone_id
        new_repair.save()
    return redirect('detail', phone_id=phone_id)

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class PhoneCreate(LoginRequiredMixin, CreateView):
    model = Phone
    fields = ['name', 'manufacturer', 'model', 'year', 'color']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhoneUpdate(LoginRequiredMixin, UpdateView):
    model = Phone
    fields = ['manufacturer', 'model', 'year', 'color']

class PhoneDelete(LoginRequiredMixin, DeleteView):
    model = Phone
    success_url = '/phones'

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = ['name', 'color']
    success_url = reversed('accessory_index')

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['nsme', 'color']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = 'phones'