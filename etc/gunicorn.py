import multiprocessing

bind = '0.0.0.0:8000'
max_requests = 10000
keepalive = 5

proc_name = 'blog_diango'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gaiohttp'

loglevel = 'info'
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'
