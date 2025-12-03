run.server.local:
	poetry run ./backend/manage.py runserver 0.0.0.0:8000

run.server.prod:
	PYTHONPATH=./backend poetry run gunicorn config.wsgi:application \
		--bind 0.0.0.0:8000 \
		--workers ${GUNICORN_WORKERS} \
		--threads ${GUNICORN_THREADS} \
		--max-requests ${GUNICORN_MAX_REQUESTS} \
		--max-requests-jitter ${GUNICORN_MAX_REQUESTS_JITTER} \
		--access-logfile - \
		--error-logfile - \
		--log-level info \
		--access-logformat '%(t)s "%(r)s" %(s)s %(b)s %(L)s'

run.bot:
	poetry run python -m telegram_bot

migrate:
	poetry run ./backend/manage.py migrate

collectstatic:
	poetry run ./backend/manage.py collectstatic --no-input

superuser:
	poetry run ./backend/manage.py createsuperuser --email ""

celery:
	cd backend && poetry run celery -A config worker --loglevel=info