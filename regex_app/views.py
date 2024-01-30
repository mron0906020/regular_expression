from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse
import re

def index(request):
    return render(request,"regex_app/index.html")

def confirm(request):
    name=request.POST.get("name")
    age = request.POST.get("age")
    zip_code=request.POST.get("zip_code")
    tel=request.POST.get("tel")
    checkname =re.sub(" ","",name)
    checkage=re.match("^[0-9]{1,3}$",age)
    checkzip_code=re.match("([0-9]{3}-?[0-9]{4})",zip_code)
    checktel=re.match("([0-9]{3}-?[0-9]{4}-?[0-9]{4})",tel)
    if checkage and checkzip_code and checktel is not None:
        context = {
           "name":checkname,
           "age": checkage.group(),
           "zip_code":checkzip_code.group(),
           "tel":checktel.group(),
        }
        return render(request,"regex_app/confirm.html", context)  
    elif checkage and checkzip_code is not None:
            tel=""
            context = {
                "name":name,
                "age":age,
                "zip_code":zip_code,
            }
            return render(request,"regex_app:index.html",context)
    elif  checkage and checktel is not None:
            zip_code=""
            context={
                "name":name,
                "age":age,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    elif checkzip_code and checktel is not None:
            age=""
            context={
                "name":name,
                "zip_code":zip_code,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    elif  checkage is not None:
            zip_code = ""
            tel=""
            context = {
                "name":name,
                "age":age,
            }
            return render(request,"regex_app/index.html",context)
    elif checkzip_code is not None:
            age=""
            tel=""
            context = {
                "name":name,
                "zip_code":zip_code
            }
            return render(request,"regex_app/index.html",context)
    elif  checktel is not None:
            age=""
            zip_code=""
            context = {
                "name":name,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    else:
            context={
                "name":name,
            }
            return render(request,"regex_app/index.html",context)
        
        
            return render(request,"regex_app/index.html",context)
       
# if checkage and checkzip_code is None:
#             age=""
#             zip_code=""
#             context = {
#                 "name":name,
#                 "tel": tel,
#             }
#             return render(request,"regex_app/index.html",context)
#         else:          
#             if checkage and checktel is None:
#                 age=""
#                 tel=""
#                 context={
#                     "name":name,
#                     "zip_code":zip_code,
#                     }
#                 return render(request,"regex_app/index.html",context)
#             else:
                # if  checkzip_code and checktel is None:
                #     zip_code=""
                #     tel=""
                #     context={
                #         "name":name,
                #         "age":age,
                #     }
                #     return render(request,"regex_app/index.html",context)
                # else:
                    # if  checkage is None:
                    #     age = ""
                    #     context = {
                    #     "name":name,
                    #     "zip_code":zip_code,
                    #     "tel": tel,
                    #     }
                    #     return render(request,"regex_app/index.html",context)
                    # else:
                        # if  checkzip_code is None:
                        #     zip_code = ""
                        #     context = {
                        #         "name":name,
                        #         "age": age,
                        #         "tel": tel,
                        #     }
                        #     return render(request,"regex_app/index.html",context)
                        # else:
                        #     if  checktel is None:
                        #         tel = ""
                        #         context = {
                        #             "name":name,
                        #             "age":age,
                        #             "zip_code":zip_code,
                        #         }
                        #         return render(request,"regex_app/index.html",context)
                        #     else:
                        #         context={
                        #             "name":name,
                        #         }
                        #         return render(request,"regex_app/index.html",context)
    
#     return render(request,"regex_app/confirm.html")
    

#     elif  checkage == None:
#                         age = ""
#                         context = {
#                         "name":name,
#                         "zip_code":zip_code,
#                         "tel": tel,
#                         }
#                         return render(request,"regex_app/index.html",context)
#     elif checkzip_code == None:
#                             zip_code = ""
#                             context = {
#                                 "name":name,
#                                 "age": age,
#                                 "tel": tel,
#                             }
#                             return render(request,"regex_app/index.html",context)
#     elif  checktel == None:
#                                 tel = ""
#                                 context = {
#                                     "name":name,
#                                     "age":age,
#                                     "zip_code":zip_code,
#                                 }
#                                 return render(request,"regex_app/index.html",context)
#     elif checkage and checkzip_code == None:
#             age=""
#             zip_code=""
#             context = {
#                 "name":name,
#                 "tel": tel,
#             }
#             return render(request,"regex_app/index.html",context)
#     elif  checkage and checktel == None:
#                 age=""
#                 tel=""
#                 context={
#                     "name":name,
#                     "zip_code":zip_code,
#                     }
#                 return render(request,"regex_app/index.html",context)
#     elif checkzip_code and checktel == None:
#                     zip_code=""
#                     tel=""
#                     context={
#                         "name":name,
#                         "age":age,
#                     }
#                     return render(request,"regex_app/index.html",context)
# #    
    
            
         

# # # Create your views here.
