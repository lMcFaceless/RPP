from django.shortcuts import render
from .models import *


def index(request):
    sellers = Seller.objects.all()
    context = {"Sellers":sellers}
    return render(request, "lab/index.html", context)


def createSeller(request):
    if request.method == "POST":
        seller = Seller.objects.create(
            name = request.POST["sellerName"]
        )
        sellers = Seller.objects.all()
        context = {"Sellers": sellers}
        return render(request, "lab/index.html", context)


def deleteSeller(request, id):
    seller = Seller.objects.get(id = id)
    seller.delete()
    sellers = Seller.objects.all()
    context = {"Sellers": sellers}
    return render(request, "lab/index.html", context)


def updateSellerPage(request, id):
    seller = Seller.objects.get(id=id)
    context = {"Seller": seller}
    return render(request, "lab/updateSellerPage.html", context)


def updateSeller(request, id):
    seller = Seller.objects.get(id=id)
    seller.name = request.POST["sellerName"]
    seller.save()
    sellers = Seller.objects.all()
    context = {"Sellers": sellers}
    return render(request, "lab/index.html", context)