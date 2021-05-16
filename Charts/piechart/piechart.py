import justpy as jp
import pandas
from datetime import datetime
import pytz

data = pandas.read_csv("popu.csv")
wshare = data.groupby(["Country (or dependency)"])["Population (2020)"].mean()



chartdef = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'World Population by % 2020'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def page():
    page = jp.QuasarPage()
    heading = jp.QDiv(a = page, text = "Analysis of World Population", classes = "text-h1 text-center q-pa-md ")
    p = jp.QDiv(a = page, text = "Chart represent the World Population", classes = "text-h6 text-center q-pa-md")

    charts = jp.HighCharts(a = page, options = chartdef)
    charts_data = [{"name": var1, "y": var2} for var1, var2 in zip(wshare.index, wshare)]
    charts.options.series[0].data = charts_data
    
    return page

jp.justpy(page)