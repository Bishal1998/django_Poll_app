from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import poll
from myapp.forms import PollForm

# Create your views here.

def index(request):
    data = poll.objects.all()
    context = {
        "data" : data
    }
    return render(request, 'index.html', context)

def create(request):
    form = PollForm()
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            _ques = form.cleaned_data['question']
            _one = form.cleaned_data['option_one']
            _two = form.cleaned_data['option_two']
            _three = form.cleaned_data['option_three']
            ins = poll(question=_ques, option_one=_one, option_two=_two, option_three=_three)
            ins.save()
            print(ins)
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def result(request, id):
    result = poll.objects.get(pk=id)
    context = {
        "result" : result
    }
    return render(request, 'results.html', context)

def vote(request, id):
    vote = poll.objects.get(pk=id)
    if request.method == "POST":
        selected = request.POST['poll']
        if selected == "option1":
            vote.option_one_count+= 1
        elif selected == "option2":
            vote.option_two_count+= 1
        elif selected == "option3":
            vote.option_three_count+= 1
        else:
            return HttpResponse(400, 'Invalid Form')
        vote.save()

        return redirect('result', id)
    context = {
        "vote" : vote
    }
    return render(request, 'vote.html',context)