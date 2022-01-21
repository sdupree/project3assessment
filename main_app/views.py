from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
  widgets = Widget.objects.all()
  widget_form = WidgetForm()
  print("Widget count:", widgets.count())
  return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form })

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/'


class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'
