import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    # st.image("images/photo.png")
    # st.image("images/resume.png")
    st.image("images/P.jpg")

with col2:
    st.title("Wang Yanghuijing (Leo)")
    content = """"
    Hello, I'm Wang Yanghuijing, currently pursuing a BSc in Computer Science at the University of Victoria, located in the beautiful city of Victoria, BC. I'm in my fourth year of studies, and my educational journey has been filled with exciting challenges and opportunities.

My technical skills have been honed through both coursework and personal projects. I'm proficient in programming languages such as Java, C#, and Python, which have empowered me to develop a wide range of software solutions. Additionally, I have experience in web development, working with technologies like JavaScript, HTML, and Node.js to create interactive and dynamic web applications.

Databases are another area of expertise for me, particularly MySQL, which I've used to design and manage data-driven applications. I'm well-versed in essential development tools like Git, Visual Studio, Eclipse, and PyCharm, which streamline the software development process. My familiarity with various operating systems, including Windows, Linux, and Unix, has allowed me to adapt and work effectively in diverse computing environments.

My commitment to excellence isn't limited to the tech realm. During my time as a Chef at I Love Sushi Restaurant in Regina, SK, I provided exceptional customer service by explaining sushi ingredients and creating delightful dining experiences. I handled various aspects of food preparation and consistently ensured the restaurant's closing procedures met security standards.

In summary, my academic journey, technical proficiency, and real-world experience have equipped me with a diverse skill set and a passion for problem-solving. I'm excited to bring my expertise to new challenges and continue to learn and grow in a dynamic environment. Thank you for reading.
    
    """
    st.info(content)

content2="""
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)


col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")