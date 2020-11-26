from .models import Linker
from django.forms import Form, CharField

class LinkForm(Form):
    link = CharField(label='Link', max_length=300)
    link_hash = CharField(label='Link hash', required=False, max_length=32)