
    Highcharts.chart('container', {
        chart: {
            type: 'tilemap',
            inverted: true,
            height: '90%',
            marginLeft: 40,
        },
        title: {
            text: '<b>确诊地图</b>',
            align: 'left',
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            visible: false
        },
        yAxis: {
            visible: false
        },
        colorAxis: {
            dataClasses: [{
                from: 0,
                to: 1,
                color: '#92ebc0',
                name: '无确诊'
            }, {
                from: 1,
                to: 2,
                color: '#FF7987',
                name: '确诊1位'
            }, {
                from: 2,
                color: '#FF2371',
                name: '确诊大于1'
            }]
        },
        tooltip: {
            headerFormat: '',
            pointFormat: '<b> {point.name}</b>号楼确诊<b>{point.value}</b>位{point.desc}'
        },
        plotOptions: {
            series: {
                dataLabels: {
                    enabled: true,
                    format: '{point.hc-a2}',
                    color: '#000000',
                    style: {
                        textOutline: false,
                        fontSize: 17,
                    }
                }
            }
        },
        series: [{
            name: '',
            data: [{
                'hc-a2': '12',
                name: '12',
                region: 'South',
                x: 1,
                y: 1,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '11',
                name: '11',
                region: 'West',
                x: 1,
                y: 2,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '10',
                name: '10',
                region: 'West',
                x: 1,
                y: 3,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '9',
                name: '9',
                region: 'West',
                x: 1,
                y: 4,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '8',
                name: '8',
                region: 'West',
                x: 2,
                y: 1,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '7',
                name: '7',
                region: 'West',
                x: 2,
                y: 2,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '6',
                name: '6',
                region: 'West',
                x: 2,
                y: 3,
                value: 2,
                'desc': " <br>401（2人，已转运2人）；"
            }, {
                'hc-a2': '5',
                name: '5',
                region: 'West',
                x: 3,
                y: 1,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '4',
                name: '4',
                region: 'West',
                x: 3,
                y: 2,
                value: 3,
                'desc': " <br>502（3人，已转运3人）；"
            }, {
                'hc-a2': '3',
                name: '3',
                region: 'West',
                x: 3,
                y: 3,
                value: 0,
                'desc': " "
            }, {
                'hc-a2': '2',
                name: '2',
                region: 'West',
                x: 3,
                y: 4,
                value: 0,
                'desc': " "
            }]
        }]
    });
    