from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Review_Entity
from .models import Hotel_Entity
from .forms import ReviewForm


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
