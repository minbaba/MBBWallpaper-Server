from django.http import HttpResponse

class CustomResponse(HttpResponse):
     def __init__(self, content=b'', code = '0', msg='请求成功', *args, **kwargs):
        super(CustomResponse, self).__init__(*args, **kwargs)
        # Content is a bytestring. See the `content` property methods.
        self.content = '{' + '\"code\":' + code + ',\"msg\":\"' + msg + '\",\"data\":' + content +'}'