import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv() 

#client = Groq(
#    api_key=os.getenv("GROQ_API_KEY"),
#)

client = Groq(
    api_key=os.getenv(st.secrets["GROQ_API_KEY"]"),
)

def grok_response(prompt):
  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
  )
  return chat_completion.choices[0].message.content

#PROMPT

prompt= f'''
The output should be in structure of Title, hook, build up, body and cta\
These are some examples on scripts\
##
#Example1:
Topic: Multiple Big Creators Stole My Content\
hook:Multiple big creators stole my content and got millions of views, more views than even me, the original creator.\
build up: Multiple big creators stole my content and got millions of views, more views than even me, who is the original. Now, I could be mad at them, but I'm a giver and I will give you two of the best ways to find wild content they shouldn't steal, but use as inspiration.\
body:Multiple big creators stole my content and got millions of views, more views than even me, who is the original. Now, I could be mad at them, but I'm a giver and I will give you two of the best ways to find wild content they shouldn't steal, but use as inspiration. First is Tweet Hunter. Find a creator on Twitter in your space and go to their profile. Tweet Hunter will organize all the tweets by the most likes on the sidebar on the right. Scroll through and specifically look for Twitter threads. These are gold mines for video ideas. The second method is source TikTok. Find a creator on TikTok and use a Chrome extension to sort all their videos by the most views. Comment PB below if you want me to send you a link to these tools, plus a 22-page doc on how to grow your personal brand from scratch\
cta:Comment PB below if you want me to send you a link to these tools, plus a 22 page doc on how to grow your personal brand from scratch.\

#Example2:
Topic: How does the social media algorithm works.\
hook: This is how the algorithm works on social media.\
build up: Once you learn the algorithm, you know the rules of the game and then you know how to win the game.\
body: When you first publish your content, it gets distributed to 20% of your followers and to a portion of people who are not your followers but those whose interest align with your content. Then the algorithm measures your content by 2 things: Watch time and Engagement. And the platform cares more about watch time. Because the longer someone spends on their platform, the more they get paid from ads. So if a person spends time watching your content, it gets pushed to more people with similar interests. Otherwise, if the content doesn't grab the viewers' attention, it gets no boost. Also, if a person shares, comments, likes, or saves your published content, the algorithm pushes your content to more viewers, resulting in more reach and engagement from a broader audience.\
cta: And the biggest cheat code to win this game is to follow for more value.\
#Example3:
Topic : How to Create Viral Hooks for Your Videos Using One Idea\
hook: Here's how to transform one shitty idea into seven viral hooks for your next video.\
build up: Once you learn the algorithm, you know the rules of the game and then you know how to win the game.\
body: You could put a negative spin. Protein powders should never taste this good, or you could put a positive spin. This protein shake actually tastes good and it's completely organic. You can ask a question. Do your protein shakes always taste like chalk? You can share an experience. I wanted to get big this summer, but getting in enough protein feels impossible. You can call the viewer out. If you struggle with gaining muscle, listen up. Tell them how? Here's how you can reach your protein goals and enjoy it. Or you could give social proof. Here's why Ronnie Coleman can't shut up about his protein powder.\
cta: Save this post and follow me for more value.\
##
'''


## streamlit app
st.set_page_config(layout="centered", page_title="YOUTUBE VIDEO SCRIPT GENERATOR", page_icon="")
st.title("YOUTUBE VIDEO SCRIPT GENERATOR")

st.info("Create engaging scripts for your YouTube videos!")

topic = st.text_input("Enter your video topic:")
video_type = st.selectbox("Select video type:", ["Long","Shorts/Reels"])

#Prompt Template

prompt1 = f'''
Your task is generate long form youtube scripts based on the topic written in backticks.\
{prompt}

Topic: ```{topic}```

'''

prompt2 = f'''
Your task is generate short form youtube scripts based on the topic written in backticks.\
{prompt}

Topic: ```{topic}```

'''

# Generate script button
if st.button("Generate Script"):
    if topic and video_type:
        if video_type=="Long":
            response = grok_response(prompt1)
            st.success("Script generated successfully!")
            st.info(response)
        else:
            response = grok_response(prompt2)
            st.success("Script generated successfully!")
            st.info(response)
    else:
        st.error("Please fill in all fields.")
