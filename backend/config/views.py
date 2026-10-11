from django.http import JsonResponse
from django.utils import timezone

def health_check(request):
    return JsonResponse({
        "status": "ok",
        "application": "SS Footwear",
        "message": "Backend is running successfully.",
        "timestamp": timezone.now().isoformat(),
    })