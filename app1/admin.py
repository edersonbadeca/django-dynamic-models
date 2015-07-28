import django
from django.contrib import admin
from django.forms import ModelForm
from .models import Partner
from django.db import models

# Register your models here.

class DynamicFields(ModelForm):
    class Meta:
        model = Partner
        fields = []

    def __init__(self, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        super().__init__(*args, **kwargs)
        self.fields['test'] = django.forms.fields.CharField()


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ('name', )
    form = DynamicFields
