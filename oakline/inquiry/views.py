from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from inquiry.models import ContactMessage
# Create your views here.

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

class ContactUsView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        return render(request, self.template_name, {'show_popup': True})
