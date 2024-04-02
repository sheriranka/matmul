#Regular Python version of Graphing.ipynb

import pandas as pd
import altair as alt

df4 = pd.read_csv("log4.csv")
df5 = pd.read_csv("log5.csv")
df4 = df4.melt(id_vars=['log4','log2'])
df5 = df5.melt(id_vars=['log5','log2'])

naive = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

strassen = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

alpha = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

fig = alt.layer(alpha, strassen, naive, data=df4).facet('log4:N')
fig.save("log4.html",embed_options={'renderer':'svg'})

naive = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

strassen = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

alpha = alt.Chart().mark_line(point=True).encode(
                x=alt.X('log2').scale(zero=False),
                y=alt.Y('value').scale(zero=False),
                color='variable:N'
        ).interactive()

fig = alt.layer(alpha, strassen, naive, data=df5).facet('log5:N')
fig.save("log5.html",embed_options={'renderer':'svg'})