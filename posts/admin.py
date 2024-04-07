from django.contrib import admin
from .models import Advertise,Inquiry,Reports
# Register your models here.




class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'posted_by_username' , 'user_username', )

    def posted_by_username(self, obj):
        return obj.posted_by if obj.posted_by else None
    posted_by_username.short_description = 'Enquiry By '

    def user_username(self, obj):
        return obj.advertise.user.first_name+" "+obj.advertise.user.last_name if obj.advertise.user else None
    user_username.short_description = 'Enquiry for user'

    # def user_username(self, obj):
    #     return obj.advertise.user.first_name if obj.advertise.user else None
    # user_username.short_description = 'User Username'

   
# admin.site.register(Enquiry,)


class ReportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username',"report_from_user" )

    
    def report_from_user(self, obj):
        return obj.posted_by if obj.posted_by else None
    report_from_user.short_description = 'Report from User'

    def user_username(self, obj):
        return obj.advertise.user.first_name+" "+obj.advertise.user.last_name if obj.advertise.user else None
    user_username.short_description = 'Reports for user '


admin.site.register(Advertise)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Reports,ReportsAdmin)
