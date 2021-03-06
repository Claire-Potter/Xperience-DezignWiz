"""
Xperiencedezignwiz dezigntools app Forms Configuration

The SurveyForm is created to refer to the Survey model, display
the body field and capture new content.

The QuestionForm is created to refer to the Question model,
display the question field to allow the user
to capture their own questions.

The OptionForm is created to refer to the Option model,
display the option field to allow the user
to capture their own options.

The AnswerForm is created to refer to the Answer model,
it holds the user's option choices.

The DefaultOPtionsForm is created to refer to the
DefaultOptions model,
it holds the default gender, age range
and industry choices.

The DefaultAnswerForm is created to for answers
to the default survey per user.

The BaseAnswerFormSet is created to hold the
user's completed survey.

The EmailForm is used for the user
to send out their survey. The subject
will contain the email subject. The recipients
field will contain the email addresses and the message
will be the email content.

Forms for the dezigntools app to be rendered by dezigntools/views.py
"""
from django import forms
from django.forms import ModelForm
from multi_email_field.forms import MultiEmailField
from .models import (Survey, Question, Option,
                     DefaultOptions, DefaultAnswers)


class SurveyForm(ModelForm):
    """
    The SurveyForm is created to refer to the Survey model, display
    the title field and capture new content.
    """
    class Meta:
        """
        The Survey model is referenced and
        the title field is included in the form
        """
        model = Survey
        fields = ['title']


class QuestionForm(ModelForm):
    """
    The QuestionForm is created to refer to the Question model,
    display the question field to allow the user
    to capture their own questions.
    """
    class Meta:
        """
        The Question model is referenced and
        the question field is included in the form
        """

        model = Question
        fields = ['question']


class DefaultOptionsForm(ModelForm):
    """
    The DefaultOPtionsForm is created to refer to the
    DefaultOptions model,
    it holds the default gender, age range
    and industry choices.
    """
    def clean_shortcodeactive(self):
        cleaned_data = self.clean()
        active = cleaned_data.get('active')
        if active is False:  # You create this function
            self.add_error('active', 'Please select Active to'
                           'activate the questions')
        return active

    class Meta:
        """
        The DefaultOptions model is referenced and
        the active field is included.
        """

        model = DefaultOptions
        fields = ['active']


class OptionForm(ModelForm):
    """
    The OptionForm is created to refer to the Option model,
    display the option field to allow the user
    to capture their own options.
    """
    class Meta:
        """
        The Option model is referenced and
        the option field is included in the form
        """
        model = Option
        fields = ['option']


class AnswerForm(forms.Form):
    """
    The AnswerForm is created to return data to the Answer model,
    it holds the user's option choices as selected
    when completing the survey.
    """
    def __init__(self, *args, **kwargs):
        """
        The option fields are displayed as Radio
        Button choices. The user will select one option
        per field. The selection is saved
        to the Answers model.
        """
        options = kwargs.pop('options')
        # Options must be a list of Option objects
        choices = {(o.pk, o.option) for o in options}
        super().__init__(*args, **kwargs)
        option_field = forms.ChoiceField(
                                         choices=choices,
                                         widget=forms.RadioSelect,
                                         required=True)
        self.fields['option'] = option_field


class DefaultAnswerForm(ModelForm):
    """
    The DefaultAnswerForm is created to for answers
    to the default survey per user.
    """
    class Meta:
        """
        The DefaultAnswers model is referenced and
        the question answer options included.
        """

        model = DefaultAnswers
        fields = ['age_range', 'gender', 'industry']


class BaseAnswerFormSet(forms.BaseFormSet):
    """
    The BaseAnswerFormSet is created to hold the
    user's completed survey.
    """
    def get_form_kwargs(self, index):
        """
        The user's selected options for each question
        are returned and saved to one form
        """
        kwargs = super().get_form_kwargs(index)
        kwargs['options'] = kwargs['options'][index]
        return kwargs


class EmailForm(forms.Form):
    """
    The EmailForm is used for the user
    to send out their survey. The subject
    will contain the email subject. The recipients
    field will contain the email addresses and the message
    will be the email content.
    """
    subject = forms.CharField()
    recipients = MultiEmailField()
    message = forms.CharField(widget=forms.Textarea)
