from django.shortcuts import render
from dotenv import load_dotenv
import openai, os
load_dotenv()
# Create your views here.

api_key = os.getenv('OPENAI_KEY', None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= f"Traslate this text to spanish: \n {request.POST.get('user_input')}",
            max_tokens=256,
            stop=".",
            temperature=0.5,
        )

        print(response)
        chatbot_response = response.choices[0].text
    return render(request, 'index.html', {'response': chatbot_response})


