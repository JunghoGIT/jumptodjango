from models import Answer

templist = list(Answer.objects.all().values_list('question_id'))
temp_answer_id = [x for x in templist]

print(temp_answer_id)