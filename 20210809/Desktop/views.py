def dropdownMenu(request):
    allCategory = Category.objects.all()
    return render(request, "dropdownMenu.html", {'allCategory': allCategory})