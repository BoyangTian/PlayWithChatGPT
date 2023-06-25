from django.shortcuts import render

def home_view(request):
    username = request.session.get("username")  # Assuming you have a registered user logged in
    return render(request, 'home.html', {'username': username})