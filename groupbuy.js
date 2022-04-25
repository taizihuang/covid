
    Highcharts.chart('container2', {
        chart: {
            type: 'xrange',
            panning: true,
            pinchType: 'x',
            height: 0
        },
        title: {
            text: '<b>团购清单</b>',
            align: 'left'
        },
        legend: {
            enabled: false
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
                day: '%m/%d'
            }
        },
        yAxis: {
            title: {
                text: ''
            },
            categories: [],
            reversed: true
        },
        tooltip: {
            dateTimeLabelFormats: {
                day: '%m/%d'
            }
        },
        series: [{
            name: '团购',
            borderColor: 'gray',
            pointWidth: 20,
            data: [
            ],
            dataLabels: {
                enabled: true,
                format: '<span>团长：{point.leader}</span>'
            }
        }]
    }, function(c) {
        // 动态改变 x 轴范围即可实现拖动
        c.xAxis[0].setExtremes(Date.UTC(2022, 3, 14), Date.UTC(2022, 3, 25));
    });
    