import openai

API_KEY = open("OpenAIKey.txt", "r").read()

openai.api_key = API_KEY


response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": "Give me a super quick weather warning in about 20 words based off this weather data: With the local area moving out of a triple dip La Niña to El Niño, a southward shift of a persistently active southern stream upper level flow over the Lower MS River Valley into the southeast US began to take hold. Most of the monthly rain fell during the middle of the month when the coastal plain saw a couple of surface fronts unusually far to the south for mid summer. These fronts along with other mesoscale boundaries provided a focus to concentrate lift along with anomalously high deep layer moisture and environmental instability. The net result was complexes of strong to severe storms moving repeatedly over the same areas causing rain amounts to swell in area rain gauges. The NWS Mobile's Automated Surface Observing Station (ASOS) at Pensacola International Airport saw just shy of 14 inches of rain collected for the month, with well over half of that falling in a one day span. On the 15th, storms deposited 9.30 inches, setting a new daily record rainfall for the date. Even more astounding is the evening rain event on the 15th for the 6 hour period from 6pm to midnight measuring 9.23 inches, aligns itself with one that typically occurs once in 50 to 100 years. It also turns out that this amount stands as the third wettest June day during Pensacola's climate period of record dating back to 1879."}
    ]
)

print("ChatGPT Says: "+response['choices'][0]['message']['content'])

