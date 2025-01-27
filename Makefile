run:
	xdg-open http://127.0.0.1:8000 2> /dev/null
	uvicorn myApi:app