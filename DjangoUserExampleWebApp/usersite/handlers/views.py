from django.http import HttpResponse

# Create your views here.
# @login_required
def demo(request):
    return HttpResponse("Hello World!")