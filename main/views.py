from django.shortcuts import render



def main(request):

    context = {}

    return render(request, "main/homepage.html", context)
