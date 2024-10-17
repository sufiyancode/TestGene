# # quiz/views.py

# import openai
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

# openai.api_key = settings.OPENAI_API_KEY

# def generate_question(topic):
#     prompt = f"Generate a question about {topic}."
#     response = openai.Completion.create(
#         engine="gpt-4",
#         prompt=prompt,
#         max_tokens=50
#     )
#     return response.choices[0].text.strip()

# def validate_answer(question, answer):
#     prompt = f"Question: {question}\nUser's answer: {answer}\nIs this answer correct? Respond with 'Correct' or 'Incorrect' and provide a brief explanation."
#     response = openai.Completion.create(
#         engine="gpt-4",
#         prompt=prompt,
#         max_tokens=100
#     )
#     return response.choices[0].text.strip()

# @csrf_exempt
# def quiz_view(request):
#     if request.method == 'POST':
#         topic = request.POST.get('topic')
#         question = generate_question(topic)
#         return JsonResponse({'question': question})
#     elif request.method == 'GET' and 'question' in request.GET and 'answer' in request.GET:
#         question = request.GET.get('question')
#         answer = request.GET.get('answer')
#         validation = validate_answer(question, answer)
#         return JsonResponse({'validation': validation})
#     return render(request, 'quiz.html')


# quiz/views.py

import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

openai.api_key = settings.OPENAI_API_KEY

def generate_question(topic):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates quiz questions."},
        {"role": "user", "content": f"Generate a question about {topic}."}
    ]
    print(topic)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()

def validate_answer(question, answer):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that validates quiz answers."},
        {"role": "user", "content": f"Question: {question}\nUser's answer: {answer}\nIs this answer correct? Respond with 'Correct' or 'Incorrect' and provide a brief explanation."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=100
    )
    return response.choices[0].message['content'].strip()

@csrf_exempt
def quiz_view(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        print(topic)
        question = generate_question(topic)
        return JsonResponse({'question': question})
    elif request.method == 'GET' and 'question' in request.GET and 'answer' in request.GET:
        question = request.GET.get('question')
        answer = request.GET.get('answer')
        validation = validate_answer(question, answer)
        return JsonResponse({'validation': validation})
    return render(request, 'quiz.html')