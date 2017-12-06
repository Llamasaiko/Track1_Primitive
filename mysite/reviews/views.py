from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Review_Entity
from .models import Hotel_Entity
from .forms import ReviewForm
from haversine import haversine
import requests
import redis


def search(request):
    if request.method == 'POST': # this will be POST now      
        review_date =  request.POST.get('query') # do some research what it does
        try:
            status = Review_Entity.objects.filter(hid__Hotel_Name__icontains=review_date)
        except Review_Entity.DoesNotExist:
            status = None
        return render(request,'reviews/review_list.html',{'reviews':status})
    else:
        return render(request,'reviews/review_list.html',{})

def review_list(request):
    reviews = Review_Entity.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def save_review_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            reviews = Review_Entity.objects.all()
            data['html_review_list'] = render_to_string('reviews/includes/partial_review_list.html', {
                'reviews': reviews
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
    else:
        form = ReviewForm()
    return save_review_form(request, form, 'reviews/includes/partial_review_create.html')


def review_update(request, pk):
    review = get_object_or_404(Review_Entity, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
    else:
        form = ReviewForm(instance=review)
    return save_review_form(request, form, 'reviews/includes/partial_review_update.html')


def review_delete(request, pk):
    review = get_object_or_404(Review_Entity, pk=pk)
    data = dict()
    if request.method == 'POST':
        review.delete()
        data['form_is_valid'] = True
        reviews = Review_Entity.objects.all()
        data['html_review_list'] = render_to_string('reviews/includes/partial_review_list.html', {
            'reviews': reviews
        })
    else:
        context = {'review': review}
        data['html_form'] = render_to_string('reviews/includes/partial_review_delete.html', context, request=request)
    return JsonResponse(data)


def advanced(request):
    # do API query
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDHfW2OgG6ZglRJUzuFHoNZ-L5nmNIO9rI"
    # addr = request.get
    # make the request to endpoint

    if request.method == 'POST': # this will be POST now      
        address = request.POST.get('address') # do some research what it does
        query = request.POST.get('query') 
        radius = int(request.POST.get('radius'))
        address = address.replace(' ', '+')
        url = endpoint.format(address)

        rds = redis.StrictRedis()
        words = query.strip().lower().split()
        hotel_ids = rds.sinter(words)

        matching_hotels = Hotel_Entity.objects.filter(hid__in=hotel_ids)

        r = requests.get(url)
        lat = r.json()['results'][0]['geometry']['location']['lat']
        lng = r.json()['results'][0]['geometry']['location']['lng']

        nearby_hotels = list()
        userloc = (lat, lng)
        for hotel in matching_hotels:
            # if hotel geolocation in radius of input latlng, append to nearby hotels
            #radius = 50
            distance = haversine(userloc, (hotel.lat, hotel.lng), miles=True)
            if distance <= radius:
                print('found {} in {}'.format(distance, radius))
                nearby_hotels.append(hotel)
           # print('{}: {},{}'.format(hotel.Hotel_Name, hotel.lat, hotel.lng))
        
        return render(request,'reviews/advanced.html',{'hotels': nearby_hotels, 'geolocation':(lat,lng)})
    else:
        return render(request, 'reviews/advanced.html', {'hotels': [], 'geolocation':(40.11,-88.23)})

def visualize(request):
    if request.method == 'POST': # this will be POST now      
        vis = request.POST.get('visual')
        return render(request,'reviews/visualize.html',{'visualize': vis})
    else:
        return render(request, 'reviews/visualize.html', {'visualize': ''})
        
        



        
