from django.db import models


class Weight():
    
    def __init__(self, request=None):

        if request:
            self.commit = int(request.POST['weight_commit'])
            self.line_code = int(request.POST['weight_line_code'])
            self.issues_created = int(request.POST['weight_issues_created'])
            self.issues_closed = int(request.POST['weight_issues_closed'])
        else:
            self.commit = 1
            self.line_code = 1
            self.issues_created = 1
            self.issues_closed = 1

    def save_in_session(self, request):
        request.session['w_commit'] = self.commit
        request.session['w_line_code'] = self.line_code
        request.session['w_issues_created'] = self.issues_created
        request.session['w_issues_closed'] = self.issues_closed

    def create_from_request(request):

        w = Weight()
        try:
            w.commit = request.session['w_commit']
            w.line_code = request.session['w_line_code']
            w.issues_created = request.session['w_issues_created']
            w.issues_closed = request.session['w_issues_closed']
        except:
            w = Weight()

        return w


    

