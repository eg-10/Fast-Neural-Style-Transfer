import os
import time

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from style_transfer.forms import UploadContentForm
from django.conf import settings


def home(request):
    content = None
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['content']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 
                                                    'content'))
        fs.save(content.name,content)
        print(content.name)
    return render(request, 'style_transfer/index.html', {'content':content})
