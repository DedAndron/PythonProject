import time


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        response = self.get_response(request)
        end_time = time.perf_counter() - start_time
        method = request.method
        url = request.get_full_path()

        print('===')
        print(f'Method: {method}')
        print(f'Url: {url}')
        print(f'Time: {end_time:.6f} seconds')
        print('===')

        return response