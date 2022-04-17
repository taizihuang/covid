
    Highcharts.chart('container2', {
        chart: {
            type: 'xrange',
            panning: true,
            pinchType: 'x',
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
            categories: ['21cake', '百货', '汉康豆制品'],
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
                {
                x: Date.UTC(2022, 3, 16),
                x2: Date.UTC(2022, 3, 20),
                y: 0,
                'leader': '7-301',
                partialFill: 0.25
            },
                {
                x: Date.UTC(2022, 3, 15),
                x2: Date.UTC(2022, 3, 17),
                y: 1,
                'leader': '10-601',
                partialFill: 1
            },
                {
                x: Date.UTC(2022, 3, 12),
                x2: Date.UTC(2022, 3, 20),
                y: 2,
                'leader': '8-401',
                partialFill: 0.62
            },
            ],
            dataLabels: {
                enabled: true,
                format: '<span>团长：{point.leader}</span>'
            }
        }]
    }, function(c) {
        // 动态改变 x 轴范围即可实现拖动
        c.xAxis[0].setExtremes(Date.UTC(2022, 3, 10), Date.UTC(2022, 3, 21));
    });
    