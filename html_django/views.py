from django.shortcuts import render

def menupage(request):
    return render(request, 'menu.html')
def aboutpage(request):
    return render(request, 'about.html')
def testimonialpage(request):
    return render(request, 'testimonial.html')
def teampage(request):
    return render(request, 'team.html')
def servicepage(request):
    return render(request, 'service.html')
def contactpage(request):
    return render(request, 'contact.html')
def indexpage(request):
    return render(request, 'index.html')
