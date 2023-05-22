from django.shortcuts import render
from django.http import JsonResponse
from .models import MusicFile, ClassificationResult

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        music_file = MusicFile.objects.create(file=file)

        # Perform classification on the music file and save the result
        # to the ClassificationResult model

        return JsonResponse({'message': 'File uploaded successfully.'})

    return JsonResponse({'error': 'Invalid request method.'})

def get_classification_result(request, music_file_id):
    try:
        classification_result = ClassificationResult.objects.get(music_file_id=music_file_id)
        result = {'genre': classification_result.genre}
    except ClassificationResult.DoesNotExist:
        result = {'genre': 'Classification result not available.'}

    return JsonResponse(result)
