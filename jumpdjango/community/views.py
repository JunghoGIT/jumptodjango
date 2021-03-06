from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Question,Answer


def index(request):
    """
    """
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request,'community/question_list.html',context)

def detail(request, question_id):

    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'community/question_detail.html', context)

def answer_create(request, question_id):

    question = get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('community:detail',question_id=question.id)