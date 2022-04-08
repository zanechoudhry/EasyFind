from django.shortcuts import render, redirect
from food.forms import Search
from food.models import Restaurants
import requests
def home(request):
    Restaurants.objects.filter(user=request.user).delete()
    form = Search()
    if(request.method == 'POST'):
        form = Search(request.POST)
        if(form.is_valid()):
            cuisine = form.cleaned_data['cuisine']
            zip_code = form.cleaned_data['zip_code']
            price = form.cleaned_data['price']
            API_KEY = "CAHd2C0s_U_6-TZyegzU-91fOD-lxzxv0PI9JJFKpH2QIJc7uCa3xMMGhHJUu1yKqyk7UU3cfbEJhz1L_OPDKKym2N_og27ThCHGwRIDHGutRnLmsSbAl_bBXxQTYnYx"
            ENDPOINT = "https://api.yelp.com/v3/businesses/search"
            HEADERS = {'Authorization':'bearer %s' % API_KEY}
            PARAMETERS = {
                'term':cuisine,
                'location':zip_code,
                'categories': 'food,restaurants',
                'price':price,
                'sort_by':'rating'
            }
            response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
            restaurant_data = response.json()
            for res in restaurant_data['businesses']:
                name = res['name']
                rating = res['rating']
                num_reviews = res['review_count']
                url = res['url']
                address = res['location']['address1']
                zip_code = res['location']['zip_code']
                city = res['location']['city']
                price = res['price']
                Restaurants(user = request.user, name=name, rating=rating,num_reviews=num_reviews,url=url,address=address,
                zip_code=zip_code,city=city,price=price).save()
            return redirect('/restaurants/results')
    context = {'form':form}
    return render(request, "food/search.html",context)
def results(request):
    context = {'restaurants': []}
    restaurants = Restaurants.objects.filter(user=request.user)
    context['restaurants'] = restaurants
    return render(request, 'food/results.html',context)
