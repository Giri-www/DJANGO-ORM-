import logging
# from django.contrib.auth.models import User
from user_details.models import User
from rest_framework import serializers

logger = logging.getLogger(__name__)

''' Base Model Serializer for AuditTimestampModel columns'''
class BaseModelSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField(read_only=True)
    updated_by_name = serializers.SerializerMethodField(read_only=True)

    def get_created_by_name(self, obj):
        ''' Created By User Name '''
        if obj.created_by:
            name = User.objects.get(id=obj.created_by).get_full_name()
            return name
        return None

    def get_updated_by_name(self, obj):
        ''' Updated By User Name'''
        if obj.updated_by:
            name = User.objects.get(id=obj.updated_by).get_full_name()
            return name
        return None

class UserSerializers(BaseModelSerializer):
    ''' User Serializers  '''
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    phone_no = serializers.SerializerMethodField(read_only=True)
    # password =  serializers.SerializerMethodField(read_only=True)
    user_type_id = serializers.SerializerMethodField(read_only=True)
    user_type =  serializers.SerializerMethodField(read_only=True)
    user_control = serializers.SerializerMethodField(read_only=True)

    def get_first_name(self,obj):
        ''' get first name '''
        UserSerializers.get_first_name.first_name = None
        try :
            UserSerializers.get_first_name.first_name = obj.first_name
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_first_name.first_name 
  
    def get_last_name(self,obj):
        ''' get last name '''
        UserSerializers.get_last_name.last_name = None
        try :
            UserSerializers.get_last_name.last_name = obj.last_name
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_last_name.last_name 
        
    def get_email(self,obj):
        ''' get email name '''
        UserSerializers.get_email.email = None
        try :
            UserSerializers.get_email.email = obj.email
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_email.email 

    def get_full_name(self,obj):
        ''' get full name '''
        UserSerializers.get_full_name.full_name = None
        try :
            UserSerializers.get_full_name.full_name = obj.user.get_full_name
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_full_name() 

    def get_phone_no(self,obj):
        ''' get phone no'''
        UserSerializers.get_phone_no.phone_no = None
        try :
            UserSerializers.get_phone_no.phone_no = obj.phone_no
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_phone_no.phone_no 
    
    def get_user_type(self,obj):
        ''' get user type '''
        UserSerializers.get_user_type.user_type = None
        try :
            UserSerializers.get_user_type.user_type = obj.user_type_name
        except Exception as ex:
            logger.info(ex)
        return UserSerializers.get_user_type.user_type 

    