from python:3.9 
WORKDIR /app2
COPY app.py /app2/ 
COPY model33.pkl /app2/ 
COPY price.csv /app2/ 
RUN pip install numpy scikit-learn pandas 
CMD ["python", "app.py", "model33.pkl", "price.csv"]