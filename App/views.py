from django.shortcuts import render
from django import forms
import pandas as pd
from datetime import datetime

def home(request):
	df = pd.read_csv("/home/siddharth/Stock-Market-Analysis-master/Stock-Market-App/data.csv")
	date = df.ix[:,0].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").date())
	date = date.to_json(orient = 'records')
	close = df.ix[:,4].to_json(orient = 'records')
	print(date)
	print(close)
	return render(request, 'data/Home.html', { 'date' : date  , 'price' : close})





