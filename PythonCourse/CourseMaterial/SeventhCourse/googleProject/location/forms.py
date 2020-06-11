from location.models import Location

from django import forms


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country']

    def __init__(self, pk, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        cityVal = cleaned_data.get('city')  # accesam valorile din input html
        countryVal = cleaned_data.get('country')
        # Location.objects.get() # Returneaza un singur rezultat, iar in cazul in care returneaza mai multe sau niciun obj apare eroare.
        # Location.objects.filter() # Returneaza o lista de obiecte si nu apare eroare in caz de obiecte multiple sau nule.
        if Location.objects.filter(city=cityVal, country=countryVal).exists():
            msg = "City and country already exist."
            self._errors['city'] = self.error_class([msg])
            return cleaned_data
