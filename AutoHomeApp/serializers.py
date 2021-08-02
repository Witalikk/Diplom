from rest_framework import serializers
from django.contrib.auth.models import User
from AutoHomeApp.models import *
from django.core.mail import send_mail
from .tasks import send_spam_email

class CreateTestDriveSerializers(serializers.ModelSerializer):
    def create(self, validated_data, ):
        user = User.objects.get(username=validated_data['user'])
        send_spam_email.delay(user.first_name, user.email)
        return super().create(validated_data=validated_data)

    class Meta:
        model = TestDrive
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone']


class AllUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

        @staticmethod
        def update(instance, validated_data):
            instance.username = validated_data['username']
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.email = validated_data['email']
            instance.phone = validated_data['phone']
            instance.save()

            return instance


class MarkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelAutoSerializers(serializers.ModelSerializer):
    marka = MarkaSerializers(many=False)

    class Meta:
        model = ModelAuto
        fields = '__all__'


class UpdateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = ['model', 'body_type', 'power', 'engine_volume', 'number_of_gears',
                  'year_of_issue', 'price', 'logo']


class CreateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = '__all__'


class RoomDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class SmsDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = '__all__'


class UserDeleteSerializers(serializers.ModelSerializer):
    def create(self, validated_data, ):
        print(validated_data['user'])
        user = User.objects.get(username=validated_data['user'])
        send_mail(
            'Удаление.',  # tema
            'Здравствуйте уважаемый ' + user.first_name +
            '. Ваша заявка на покупку автомобиля одобрена.'
            ' Для уточнения можете связаться с нами: autohome228@gmail.com',
            'autohome228@gmail.com',
            [user.email],
            False
        )
        return super().create(validated_data=validated_data)

    class Meta:
        model = User
        fields = '__all__'


class SoldCarsSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = SoldCars
        fields = '__all__'


class CreateSoldCarsSerializers(serializers.ModelSerializer):

    def create(self, validated_data, ):
        print(validated_data['user'])
        user = User.objects.get(username=validated_data['user'])
        send_mail(
            'Заявка на покупку автомобиля.',
            'Здравствуйте уважаемый ' + user.first_name + '. Ваша заявка на покупку автомобиля одобрена. Для уточнения можете связаться с нами: autohome228@gmail.com',
            'autohome228@gmail.com',
            [user.email],
            False
        )
        return super().create(validated_data=validated_data)

    class Meta:
        model = SoldCars
        fields = '__all__'


class InquirySerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = Inquiry
        fields = '__all__'


class CreateInquirySerializers(serializers.ModelSerializer):
    def create(self, validated_data, ):
        print(validated_data['user'])
        user = User.objects.get(username=validated_data['user'])
        send_mail(
            'Заявка отменена.',
            'Здравствуйте уважаемый ' + user.first_name + '.Ваша заявка на автомобиля отклонена.',
            'autohome228@gmail.com',
            [user.email],
            False
        )
        return super().create(validated_data=validated_data)

    class Meta:
        model = Inquiry
        fields = '__all__'


class TestDriveSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = TestDrive
        fields = '__all__'





class ServiceSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    models = ModelAutoSerializers(many=False)

    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class UpdateSMSAutoSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    room = RoomSerializers(many=False)

    class Meta:
        model = SMS
        fields = '__all__'


class SMSSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    room = RoomSerializers(many=False)

    class Meta:
        model = SMS
        fields = '__all__'


class CreateSMSSerializers(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = '__all__'