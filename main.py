import google.generativeai as genai
import os
from promptChange import *

genai.configure(api_key="AIzaSyDbDxFkssnq_6DqBBu75d5uVWJLdjP1gsY")

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "write only one number: average duration_in_mins"
prompt = addToPrompt(prompt)

trips_csv = genai.upload_file("trips.csv")
# run_data = genai.upload_file("run_data.csv")
# stops_date = genai.upload_file("stops_data.csv")
# dwell_sorted = genai.upload_file("dwell_sorted.csv")

response = model.generate_content([prompt, trips_csv])

#add next line in model.generate_content if it works
#, run_data, stops_date, dwell_sorted

print("Response:")
print(response.text)



