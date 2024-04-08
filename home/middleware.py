# middleware.py
from django.utils.deprecation import MiddlewareMixin
from datetime import date
from .models import Visitor

class VisitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            visitor = Visitor.objects.get(date=date.today())
            visitor.count += 1
        except Visitor.DoesNotExist:
            visitor = Visitor.objects.create(date=date.today(), count=1)
        visitor.save()