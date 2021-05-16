import justpy as jp
import pandas
from datetime import datetime
import pytz
#import matplotlib.pyplot as plt

#Injecting the data from the datasets
data = pandas.read_csv("doge.csv", parse_dates = ["snapped_at"])
data["Day"] =  data["snapped_at"].dt.date
day_avg = data.groupby(["Day"]).mean()

chartdef = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value} dogecoins'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'DOGE',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def page():
    page = jp.QuasarPage()
    heading = jp.QDiv(a = page, text = "Analysis of Dogecoin Price (DOGE)", classes = "text-h1 text-center q-pa-md ")
    p = jp.QDiv(a = page, text = "Graphs represent the prices of (DOGE)", classes = "text-h6 text-center q-pa-md")
    
    charts = jp.HighCharts(a = page, options = chartdef)
    
    charts.options.title.text = "Daily Analysis of Dogecoin"
    charts.options.subtitle.text = "To the MOOOOOON"
    charts.options.yAxis.title.text = "Price"
    
    #charts.options.series[0].data = [[3, 4], [5, 7 ,8]]
    #charts.options.series[0].data = list(zip(x,y))
    
    charts.options.xAxis.categories = list(day_avg.index)
    charts.options.series[0].data = list(day_avg["price"])

    

    return page

jp.justpy(page)