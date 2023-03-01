from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.

class cartdetailview(View):
    def get(self, request):
        return render(request, 'cart/cartdetail.html', {})


class addprofuct(View):
    def post(self, request):
        print('added product ')
        return redirect('cart:cartdetail')
