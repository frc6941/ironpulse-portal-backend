from django.forms import Form, fields

from activity.models import Activity
from user.models import User


class GetUserByName(Form):
    name = fields.CharField(
        required=True,
        error_messages={
            'required': 'ironpulse.user.name.required'
        }
    )

    def clean_name(self):
        if not User.objects.filter(name=self.cleaned_data.get('name')).exists():
            raise fields.ValidationError('ironpulse.user.not_exist')

        return self.cleaned_data.get('name')


class GetUserByToken(Form):
    token = fields.UUIDField(
        required=True,
        error_messages={
            'required': 'ironpulse.user.token.required'
        }
    )

    def clean_token(self):
        if not User.objects.filter(token=self.cleaned_data.get('token')).exists():
            raise fields.ValidationError('ironpulse.user.not_exist')

        return self.cleaned_data.get('token')


class SignIn(Form):
    token = fields.UUIDField(
        required=True,
        error_messages={
            'required': 'ironpulse.user.token.required'
        }
    )

    activity_id = fields.UUIDField(
        required=True,
        error_messages={
            'required': 'ironpulse.activity.id.required'
        }
    )

    def clean_token(self):
        if not User.objects.filter(token=self.cleaned_data.get('token')).exists():
            raise fields.ValidationError('ironpulse.user.not_exist')

        return self.cleaned_data.get('token')

    def clean_activity_id(self):
        if not Activity.objects.filter(id=self.cleaned_data.get('activity_id')).exists():
            raise fields.ValidationError('ironpulse.activity.not_exist')

        return self.cleaned_data.get('activity_id')
