
    Highcharts.chart('container1', {
        chart: {
            type: 'timeline',
            panning: true,
            pinchType: 'x',
            marginLeft: '25',
            marginRight: '15'
        },
        xAxis: {
            type: 'datetime',
            visible: false,
        },
        yAxis: {
            gridLineWidth: 1,
            title: null,
            labels: {
                enabled: false
            }
        },
        legend: {
            enabled: false
        },
        title: {
            text: '<b>防疫时刻</b>',
            align: 'left',
        },
        subtitle: {
            text: ''
        },
        tooltip: {
            style: {
                width: 400
            }
        },
        series: [{
            dataLabels: {
                allowOverlap: true,
                format: '<span style="width:100px"><b>{point.x:%m/%d}</b><br>{point.label}</span>'
            },
            marker: {
                symbol: 'circle',
                color: '{point.color}',

            },
            data: [
                {
                x: Date.UTC(2022, 3, 15),
                name: "全员抗原",
                label: "全员抗原",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 16),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 18),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 20),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 21),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 24),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 26),
                name: "全员核酸",
                label: "全员核酸",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 27),
                name: "全员抗原",
                label: "全员抗原",
                description: "",
                color: "black",
            },
                {
                x: Date.UTC(2022, 3, 14),
                name: "4-502确诊1人",
                label: "4-502确诊1人",
                description: "",
                color: "red",
            },
                {
                x: Date.UTC(2022, 3, 19),
                name: "4-502确诊2人",
                label: "4-502确诊2人",
                description: "",
                color: "red",
            },
                {
                x: Date.UTC(2022, 3, 23),
                name: "4-502确诊1人",
                label: "4-502确诊1人",
                description: "",
                color: "red",
            },
                {
                x: Date.UTC(2022, 3, 10),
                name: "6-401确诊3人",
                label: "6-401确诊3人",
                description: "",
                color: "red",
            },
                {
                x: Date.UTC(2022, 3, 17),
                name: "6-502确诊1人",
                label: "6-502确诊1人",
                description: "",
                color: "red",
            },
            {
                x: Date.UTC(2022, 3, 30),
                name: ' ',
                label: ' ',
                description: "",
                color: 'black',
            }]
        }]
    }, function(c) {
        // 动态改变 x 轴范围即可实现拖动
        c.xAxis[0].setExtremes(Date.UTC(2022, 3, 24), Date.UTC(2022, 3, 29));
    });
    