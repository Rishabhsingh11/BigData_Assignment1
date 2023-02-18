From python:3.11.1

WORKDIR /app

COPY streamlit_app.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["streamlit","run","streamlit_app.py","--server.port","8080"]