from django import forms


class SearchRepositoryForm(forms.Form):

    repository = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(SearchRepositoryForm, self).is_valid():
            self.addErro('Insira um repositório válido!')
            valid = False

        return valid

    def addErro(self, message):
        errors = self._e.setdefault(forms.forms.NON_FIELD_ERRORS,
                                    forms.utils.ErrorList())
        errors.append(message)
