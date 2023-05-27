from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *

from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            u = User.objects.get(username=user)

            customer, created = Customer.objects.get_or_create(
                user=u,
                role=request.POST.get('role'),
                name=user
            )
            customer.save()

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'lab/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}

    return render(request, 'lab/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def index(request):
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def createClient(request):
    if request.method == "POST":

        if request.user.is_authenticated:
            customer = request.user.customer

            if customer.role == 'Client':
                client = Client.objects.create(
                    name=request.POST['clientName']
                )

        orders = Order.objects.all()
        sellers = Seller.objects.all()
        clients = Client.objects.all()
        dishes = Dish.objects.all()
        products = Product.objects.all()
        context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
        return render(request, "lab/index.html", context)


def createSeller(request):
    if request.method == "POST":

        if request.user.is_authenticated:
            customer = request.user.customer

            if customer.role == 'Seller':
                seller = Seller.objects.create(
                    name=request.POST["sellerName"]
                )

        orders = Order.objects.all()
        sellers = Seller.objects.all()
        clients = Client.objects.all()
        dishes = Dish.objects.all()
        products = Product.objects.all()
        context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
        return render(request, "lab/index.html", context)


def deleteSeller(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer

        if customer.role == 'Seller':
            seller = Seller.objects.get(id=id)
            seller.delete()

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def updateSellerPage(request, id):
    seller = Seller.objects.get(id=id)
    context = {"Seller": seller}
    return render(request, "lab/updateSellerPage.html", context)


def updateSeller(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer

        if customer.role == 'Seller':
            seller = Seller.objects.get(id=id)
            seller.name = request.POST["sellerName"]
            seller.save()

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def updateClientPage(request, id):
    client = Client.objects.get(id=id)
    context = {"Client": client}
    return render(request, "lab/updateClientPage.html", context)


def updateClient(request, id):

    if request.method == "POST":

        if request.user.is_authenticated:
            customer = request.user.customer

            if customer.role == 'Client':
                client = Client.objects.get(id=id)
                client.name = request.POST["clientName"]
                client.save()

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def createDish(request):
    if request.method == "POST":
        dish = Dish.objects.create(
            title=request.POST['dishName']
        )
        dish.save()
        orders = Order.objects.all()
        sellers = Seller.objects.all()
        clients = Client.objects.all()
        dishes = Dish.objects.all()
        products = Product.objects.all()
        context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
        return render(request, "lab/index.html", context)


def deleteDish(request, id):
    dish = Dish.objects.get(id=id)
    dish.delete()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def updateDishPage(request, id):
    dish = Dish.objects.get(id=id)
    context = {"Dish": dish}
    return render(request, "lab/updateDishPage.html", context)


def updateDish(request, id):
    dish = Dish.objects.get(id=id)
    dish.title = request.POST["dishName"]
    dish.save()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def createProduct(request):
    dish = Dish.objects.get(
        title=request.POST['productDishTitle']
    )

    product = Product.objects.create(
        dish=dish,
        name=request.POST['productName']
    )

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def updateProductPage(request, id):
    dishes = Dish.objects.all()
    product = Product.objects.get(id=id)
    context = {"Product": product, 'Dishes': dishes}
    return render(request, "lab/updateProductPage.html", context)


def updateProduct(request, id):
    dish = Dish.objects.get(title=request.POST['productDishTitle'])
    product = Product.objects.get(id=id)
    product.name = request.POST['productName']
    product.save()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def createOrder(request):
    orders = Order.objects.all()

    dish = Dish.objects.filter(title=request.POST['orderDishTitle'])

    client = Client.objects.get(name=request.POST['orderClientTitle'])
    seller = Seller.objects.get(name=request.POST['orderSellerDishTitle'])

    order = Order.objects.create(
        number=len(orders) + 1,
        client=client,
        seller=seller
    )

    order.dish.set(dish)

    order.save()

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)


def updateOrderPage(request, id):
    clients = Client.objects.all()
    sellers = Seller.objects.all()
    dishes = Dish.objects.all()
    order = Order.objects.get(id=id)
    context = {'Order': order, "Clients": clients, 'Sellers': sellers, 'Dishes': dishes}
    return render(request, "lab/updateOrderPage.html", context)


def updateOrder(request, id):
    dish = Dish.objects.filter(title=request.POST['orderDishTitle'])

    client = Client.objects.get(name=request.POST['orderClientTitle'])
    seller = Seller.objects.get(name=request.POST['orderSellerDishTitle'])

    order = Order.objects.get(id=id)

    order.seller = seller
    order.client = client
    order.dish.set(dish)

    order.save()

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    clients = Client.objects.all()
    dishes = Dish.objects.all()
    products = Product.objects.all()
    context = {"Sellers": sellers, "Clients": clients, "Dishes": dishes, "Products": products, "Orders": orders}
    return render(request, "lab/index.html", context)
