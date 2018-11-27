from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        name = self.request.query_params.get('name')

        if email and name:
            return self.queryset.filter(email=email, name=name)
        elif email:
            return self.queryset.filter(email=email)
        elif name:
            return self.queryset.filter(name=name)
        else:
            return self.queryset
