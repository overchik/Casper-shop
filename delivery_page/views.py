from django.shortcuts import render


def delivery_page(request):
    return render(request, 'delivery_page/delivery_page.html')