from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    texts = request.POST['texts']
    word_count = len(texts.split())
    return render(request, 'counter.html', {'number_of_words': word_count})
