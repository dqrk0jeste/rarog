from django.http import HttpResponse

def index(request):
    html = f'''
    <html>
        <body>
            <h1>Hello!</h1>
            <p>Connected to the database.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)