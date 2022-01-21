from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Sum
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
  widgets = Widget.objects.all()
  widget_sum = Widget.objects.aggregate(Sum('quantity'))['quantity__sum']
  widget_form = WidgetForm()
  return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form, 'widget_sum': widget_sum })

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/'


class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'
