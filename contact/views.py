# contact/views.py
import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt  # for simplicity; in production you'd use proper CSRF tokens
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            # Validate required fields
            if not name or not email or not message:
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            # Compose email
            subject = f"Contact Form Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = settings.EMAIL_HOST_USER  # your Gmail address
            recipient_list = [settings.EMAIL_HOST_USER]  # send to yourself

            send_mail(subject, body, from_email, recipient_list)

            return JsonResponse({'success': True, 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)