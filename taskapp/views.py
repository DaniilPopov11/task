from django.shortcuts import render

def main(request):
    return render(request, 'taskapp/main.html')