from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from companies.forms import CompaniesForm
from companies.models import Companies


class CompaniesIndexView(ListView):
    model = Companies
    template_name = 'companies/companies_index.html'
    context_object_name = 'all_companies'


class NewCompanyView(CreateView):
    model = Companies
    form_class = CompaniesForm
    template_name = 'companies/companies_form.html'

    def get_success_url(self):
        return reverse('companies:index')


class UpdateCompanyView(UpdateView):
    model = Companies
    form_class = CompaniesForm
    template_name = 'companies/companies_form.html'

    def get_success_url(self):
        return reverse('companies:index')
