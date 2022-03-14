from django.http import HttpResponse
from django.shortcuts import render
from boto.s3.connection import S3Connection

from pyapp import settings

def index(request):
    bucketlist = []
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.MEDIA_BUCKET)
    for key in bucket.list():
        bucketlist.append(key.name)
        print(key)

    blogs = [
        {
            'title': 'First Blog',
            'content': 'Blog Content'
        },
        {
            'title': 'Second Blog',
            'content': 'Blog Content'
        },
        {
            'title': 'Third Blog',
            'content': 'Blog Content'
        },
    ]

    content = {
        'blogs': blogs,
        'bucket': bucketlist
    }
    return render(request, 'index.html', content)

def currentBlog(request):
    return HttpResponse('Current blog')
