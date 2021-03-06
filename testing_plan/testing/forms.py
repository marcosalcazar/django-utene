from django import forms
from django.forms.models import inlineformset_factory
from testing.models import TestCasePreCondition, TestCase, TestCasePostCondition, \
    TestCaseStep, TestCaseRevision, TestCaseState


TestCasePreConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePreCondition)


TestCasePostConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePostCondition)


TestCaseStepFormSet = \
    inlineformset_factory(TestCase, TestCaseStep)


# TestCaseCorrectiveActionFormSet = \
#     inlineformset_factory(TestCase, TestCaseCorrectiveAction)


class TestCaseRevisionForm(forms.ModelForm):

    class Meta:
        model = TestCaseRevision
        exclude = ('test_case', 'user',)


class TestCaseForm(forms.ModelForm):
    
    class Meta:
        model = TestCase
        exclude = ('author', )


class TestCaseStateForm(forms.ModelForm):
    
    class Meta:
        model = TestCaseState
        exclude = ('test_case', 'user', )