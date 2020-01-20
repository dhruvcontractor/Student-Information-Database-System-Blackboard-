from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import View
from .models import Student, Profile
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.views.generic.edit import UpdateView
import datetime
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = 'students/index.html'
    context_object_name = 'profiles_list'
    def get_queryset(self):


        return Profile.objects.all()



class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = '__all__'
    template_name_suffix = '_update_form'

    success_message = 'Profile Updated! Time: %s' % str(timezone.now())





class DetailView(generic.DetailView):
    model = Profile
    template_name = 'students/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'students/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            messages.success(request, 'Student added! Time: %s' % str(timezone.now()))
#            if user is not None:

#                if user.is_active:
#                    login(request, user)
            return redirect('students:profile')
        return render(request, self.template_name, {'form':form})

class ProfileFormView(View):
    form_class = ProfileForm
    template_name = 'students/profile_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            profile = form.save(commit=False)

            #cleaned data
            user = form.cleaned_data['user']
            role = form.cleaned_data['role']
            banner_id = form.cleaned_data['banner_id']
            gpa = form.cleaned_data['gpa']
            total_credit = form.cleaned_data['total_credit']
            balance = form.cleaned_data['balance']
            profile.save()
            messages.success(request, 'Profile added! Time: %s' % str(timezone.now()))
            return render('students:index')
        return render(request, self.template_name, {'form':form})
