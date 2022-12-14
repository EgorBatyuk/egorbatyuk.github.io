from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .models import Message
from .forms import ReviewForm


def index(request):
    return render(request, 'review/index.html')


def review(request):
    reviews = Message.objects.all()
    context = {'message': reviews}
    return render(request, 'review/review.html', context)


def message(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            message = Message()
            message.author_name = form.cleaned_data['author_name']
            message.text = form.cleaned_data['review']
            message.save()
            print(message)
            return HttpResponseRedirect('/review/')
    else:
        form = ReviewForm()

    return render(request, 'review/forms.html', {'form': form})

