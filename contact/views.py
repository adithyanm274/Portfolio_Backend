import json
import os
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            subject = f"Contact Form Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Use the configured default from email (set via environment)
            from_email = settings.DEFAULT_FROM_EMAIL
            
            # The recipient email: where you want to receive contact messages
            # It's best to set this as an environment variable, fallback to your Gmail
            recipient_email = os.environ.get("CONTACT_EMAIL", "adithyan.m.2742001@gmail.com")
            recipient_list = [recipient_email]

            send_mail(subject, body, from_email, recipient_list)

            return JsonResponse({'success': True, 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)