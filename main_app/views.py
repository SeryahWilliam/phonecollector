from django.shortcuts import render
phones_list = [
    {'id': 1, 'name': 'iPhone 11', 'manufacturer': 'Apple', 'year': 2019, 'color': 'Black'},
    {'id': 4, 'name': 'iPhone 11 Pro', 'manufacturer': 'Apple', 'year': 2019, 'color': 'Midnight Green'},
    {'id': 6, 'name': 'iPhone 12', 'manufacturer': 'Apple', 'year': 2020, 'color': 'Red'},
    {'id': 8, 'name': 'iPhone 12 Pro Max', 'manufacturer': 'Apple', 'year': 2020, 'color': 'Pacific Blue'},
    {'id': 5, 'name': 'Galaxy S20 Ultra', 'manufacturer': 'Samsung', 'year': 2020, 'color': 'Cosmic Gray'},
    {'id': 2, 'name': 'Galaxy S20', 'manufacturer': 'Samsung', 'year': 2020, 'color': 'Blue'},
    {'id': 9, 'name': 'Galaxy Note 20', 'manufacturer': 'Samsung', 'year': 2020, 'color': 'Mystic Bronze'},
    {'id': 7, 'name': 'Galaxy S21', 'manufacturer': 'Samsung', 'year': 2021, 'color': 'Phantom White'},

    {'id': 3, 'name': 'Pixel 5', 'manufacturer': 'Google', 'year': 2020, 'color': 'Black'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def phones_index(request):
    context = {'phones': phones_list}
    return render(request, 'phones/index.html', context)