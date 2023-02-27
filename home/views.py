
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from product.models import Category
# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'

def category_list(request):
    categorys = Category.objects.all()
    return render(request, 'product/category.html', {'categorys': categorys})