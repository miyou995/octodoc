import re
import json
from django.contrib.messages import get_messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import resolve, reverse 
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from re import compile
from config import settings

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]



class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass
        # assert hasattr(request, 'user')

        # path = request.path_info.lstrip('/')
        # url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        # # if "dashboard" not in path:
        # #     url_is_exempt = True
        # redirect_to = settings.LOGIN_URL
        # if path == settings.LOGOUT_REDIRECT_URL.lstrip('/'):
        #     logout(request)
        # if request.user.is_authenticated or url_is_exempt:
        #     return None
        # else:
        #     return redirect(reverse(redirect_to))

        #     ## return redirect(f"{settings.LOGIN_URL}?next=/{path}")


# class LoginRequiredMiddleware(MiddlewareMixin):
#     """
#     Middleware that requires a user to be authenticated to view any page other
#     than LOGIN_URL. Exemptions to this requirement can optionally be specified
#     in settings by setting a tuple of routes to ignore
#     """
#     def process_request(self, request):
#         pass
    
    #### DECOMMENT WHEN COMPLETING ACCOUNTS APP WITH ITS URLS ####

        # if request.path.startswith(reverse('admin:index')):
        #     return None
        # assert hasattr(request, 'user'), """
        # The Login Required middleware needs to be after AuthenticationMiddleware.
        # Also make sure to include the template context_processor:
        # 'django.contrib.auth.context_processors.auth'."""

        # if not request.user.is_authenticated:
        #     current_route_name = resolve(request.path_info).url_name

        #     if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
        #         return HttpResponseRedirect(reverse(settings.LOGIN_URL))




class HtmxMessageMiddleware(MiddlewareMixin):

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:

        # The HX-Request header indicates that the request was made with HTMX
        if "HX-Request" not in request.headers:
            return response

        # Ignore redirections because HTMX cannot read the headers
        if 300 <= response.status_code < 400:
            return response

        # Extract the messages
        messages = [
            {"message": message.message, "tags": message.tags}
            for message in get_messages(request)
        ]
        if not messages:
            return response

        # Get the existing HX-Trigger that could have been defined by the view
        hx_trigger = response.headers.get("HX-Trigger")

        if hx_trigger is None:
            # If the HX-Trigger is not set, start with an empty object
            hx_trigger = {}
        elif hx_trigger.startswith("{"):
            # If the HX-Trigger uses the object syntax, parse the object
            hx_trigger = json.loads(hx_trigger)
        else:
            # If the HX-Trigger uses the string syntax, convert to the object syntax
            hx_trigger = {hx_trigger: True}

        # Add the messages array in the HX-Trigger object
        hx_trigger["messages"] = messages
        # print('messages from HTMX ============>', messages)
        # print('hx_trigger from HTMX ============>', hx_trigger)
        # Add or update the HX-Trigger
        response.headers["HX-Trigger"] = json.dumps(hx_trigger)
        return response