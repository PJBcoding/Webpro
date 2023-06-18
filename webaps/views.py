from django.shortcuts import render
from django.views import View
# Create your views here.


class StartingPageView(View):
    def get(self, req):
        return render(req, 'webaps/index.html')
