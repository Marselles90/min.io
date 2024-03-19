from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, SerializerMethodField

from .models import (
    UserAccounts, CompanyProjects, CompanySettings, CompanyAnaliticsMail
)


class RefreshTokenSerialzierPost(Serializer):
    refresh = CharField()


class UserSerialzier(ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ['id', 'first_name', 'last_name', 'patronymic_name',
                  'phone', 'email', 'avatar', 'birthday']


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = UserSerialzier.Meta.fields
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'patronymic_name': {'required': False},
            'birthday': {'required': False},
            'email': {'required': False},
            'avatar': {'required': False},
            'phone': {'required': False}
        }


class LoginSerializer(Serializer):
    phone = CharField()
    password = CharField()


class RegisterSeialzier(Serializer):
    first_name = CharField()
    last_name = CharField()
    patronymic_name = CharField()
    birthday = CharField()
    email = CharField()
    phone = CharField()
    password = CharField()


class CompanyProjectSerialzier(ModelSerializer):
    class Meta:
        model = CompanyProjects
        fields = ['id', 'account', 'name', 'company_mail', 'company_phone']


class ComapnyProjectsCreateSerializer(ModelSerializer):
    class Meta:
        model = CompanyProjects
        fields = CompanyProjectSerialzier.Meta.fields


class CompanyProjectsUpdateSerialzier(ModelSerializer):
    class Meta:
        model = CompanyProjects
        fields = CompanyProjectSerialzier.Meta.fields
        extra_kwargs = {
            'account': {'required': False},
            'name': {'required': False},
            'company_mail': {'required': False},
            'company_phone': {'required': False}
        }


class ComapanySettingsSerialiser(ModelSerializer):
    class Meta:
        model = CompanySettings
        fields = ['id', 'company', 'intervar_mail_sends', 'max_mail_sends',
                  'email_title', 'email_subject', 'is_active']


class CompanySettingsCreateSerializer(ModelSerializer):
    class Meta:
        model = CompanySettings
        fields = ComapanySettingsSerialiser.Meta.fields


class CompanySettingsUpdareSerialzier(ModelSerializer):
    class Meta:
        model = CompanySettings
        fields = ComapanySettingsSerialiser.Meta.fields
        extra_kwargs = {
            'company': {'required': False},
            'intervar_mail_sends': {'required': False},
            'max_mail_sends': {'required': False},
            'email_title': {'required': False},
            'email_subject': {'required': False},
            'is_active': {'required': False}
        }


class CompanyAnaliticsMailSerialzier(ModelSerializer):
    class Meta:
        model = CompanyAnaliticsMail
        fields = ['id', 'company', 'company_settings', 
                  'count_sends_mail', 'count_anmswer_mail',
                  'count_open_mail_on_company', 'count_aveible_interval']


class CompanyAnaliticsMailCreateSerialzier(ModelSerializer):
    class Meta:
        model = CompanyAnaliticsMail
        fields = CompanyAnaliticsMailSerialzier.Meta.fields


class CompanyAnaliticsMailUpdateSerialzier(ModelSerializer):
    class Meta:
        model = CompanyAnaliticsMail
        fields = CompanyAnaliticsMailSerialzier.Meta.fields
        extra_kwargs = {
            'company': {'required': False},
            'company_settings': {'required': False},
            'count_sends_mail': {'required': False},
            'count_anmswer_mail': {'required': False},
            'count_open_mail_on_company': {'required': False},
            'count_aveible_interval': {'required': False}
        }