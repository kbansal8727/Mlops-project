from python:3.9 
WORKDIR /app2
COPY . .
RUN pip install numpy scikit-learn pandas 
CMD ["python","app.py", "model33.pkl"]
