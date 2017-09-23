web: gunicorn -b 0.0.0.0:8888 manage:app --log-file -
worker: celery worker -A red_packet.core.worker.celery --loglevel=info
