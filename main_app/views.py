from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
  widgets = Widget.objects.all()
  widget_form = WidgetForm()

  return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form })

class WidgetCreate(CreateView):
  model = Widget
  field = '__all__'
  success_url = '/'