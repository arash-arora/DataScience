import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import os

#Image 
path = os.path.dirname(__file__)
image = Image.open(path+"/dna.png")
st.image(image, use_column_width=True)

#Header
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!

***
""")

#Input Section
st.header("Enter DNA Sequence")

sequence_inp = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#Convert the input to a string
sequence = st.text_area("Sequence Input", sequence_inp, height=250)
sequence = sequence.splitlines()[1:]
sequence = "".join(sequence)

st.write("***")

#Displays Input String
st.header("INPUT DNA QUERY")
sequence

#DNA Nucleotide Count
st.header("OUTPUT DNA NUCLEOTIDE COUNT")

#dictionary
st.subheader("1. Print Dictionary")
def dna_nuc_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = dna_nuc_count(sequence)
X

#Print text
st.subheader("2. Print Text")
st.write("There are ", str(X["A"]), "adenine (A)")
st.write("There are ", str(X["T"]), "thymine (T)")
st.write("There are ", str(X["G"]), "guanine (G)")
st.write("There are ", str(X["C"]), "cytosine (C)")

#Display Dataframe
st.subheader("3. Display Dataframe")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

#Display bar chart using altair
st.subheader("3. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)
p = p.properties(
    width=alt.Step(90)
)
st.write(p)