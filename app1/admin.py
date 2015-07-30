import django
from django.contrib import admin
from django.forms import ModelForm
from .models import Partner

fields_mapping = {
    'text': django.forms.fields.CharField,
    'url': django.forms.fields.URLField,
    'int': django.forms.fields.IntegerField,
}

form_dynamic_data = {
    'license_size': {
        'type': 'int',
        'args': {'min_value': 1},
    },
    'my_dog_name': {
        'type': 'text',
        'args': {'max_length': 20}
    },
}


class PartnerAdminForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dynamic_fields = self.build_dynamic_fields(form_dynamic_data)
        self.fields.update(dynamic_fields)

    def build_dynamic_fields(self, dynamic_fields):
        fields = {}
        for field_name, field_args in dynamic_fields.items():
            field_class = fields_mapping[field_args['type']]
            fields[field_name] = field_class(**field_args['args'])
        return fields


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        dynamic_fields = PartnerAdminForm().fields
        return type('PartnerAdminForm_', (PartnerAdminForm, ), dynamic_fields)
