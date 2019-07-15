from .utils import DH_Endpoint
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Self


def partial(request, m_pub):
    self = Self()
    device = DH_Endpoint(self.public_key, m_pub, self.private_key)
    partial_key = device.generate_partial_key()
    print(partial_key)
    return HttpResponse('This is the partial')
