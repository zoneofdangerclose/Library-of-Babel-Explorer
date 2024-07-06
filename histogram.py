import plotly.express as px

data = [0.147, 0.115, 0.122, 0.111, 0.09, 0.12, 0.149, 0.127, 0.139, 0.17, 0.078, 0.093, 0.126, 0.103, 0.179, 0.152, 0.136, 0.147, 0.185, 0.121, 0.102, 0.153, 0.188, 0.138, 0.172, 0.118, 0.104, 0.22, 0.122, 0.155, 0.096, 0.087, 0.183, 0.138, 0.161, 0.1, 0.15, 0.126, 0.132, 0.185, 0.1, 0.131, 0.139, 0.077, 0.08, 0.117, 0.072, 0.124, 0.136, 0.12, 0.143, 0.161, 0.149, 0.146, 0.118, 0.138, 0.095, 0.149, 0.08, 0.129, 0.136, 0.167, 0.119, 0.107, 0.143, 0.184, 0.117, 0.104, 0.105, 0.145, 0.127, 0.14, 0.103, 0.157, 0.162, 0.133, 0.113, 0.079, 0.095, 0.129, 0.089, 0.116, 0.204, 0.106, 0.146, 0.167, 0.127, 0.116, 0.123, 0.106, 0.083, 0.17, 0.142, 0.087, 0.099, 0.083, 0.159, 0.143, 0.15, 0.104]

fig = px.histogram(x=data, title='Histogram of Undefined Words that Passed Filter')
fig.show()