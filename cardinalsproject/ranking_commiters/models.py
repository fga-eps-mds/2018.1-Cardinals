from django.db import models


class Weight():
    
    def __init__(self, request):
        self.commit = int(request.POST['weight_commit'])
        self.line_code = int(request.POST['weight_line_code'])
        self.issues_created = int(request.POST['weight_issues_created'])
        self.issues_closed = int(request.POST['weight_issues_closed'])
