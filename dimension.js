
var chart = Highcharts.chart('container0', {
    chart: {
        backgroundColor: 'white',
        events: {
            load: function() {
                // Draw the flow chart
                var ren = this.renderer,
                    colors = Highcharts.getOptions().colors;
                // 横线
                ren.path(['M', 10, 150, 'L', 320, 150])
                    .attr({
                        'stroke-width': 2,
                        stroke: 'silver',
                        dashstyle: 'dash'
                    }).add();
                // 竖线
                ren.path(['M', 170, 50, 'L', 170, 260])
                    .attr({
                        'stroke-width': 2,
                        stroke: 'silver',
                        dashstyle: 'dash'
                    }).add();
                // Headers
                ren.label('返回居家人数<br/>', 40, 50)
                    .attr({
                        fill: 'blue',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(7, 30, 50)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('已确诊总人数', 210, 50)
                    .attr({
                        fill: 'red',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(6, 200, 50)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('待转运人数<br>确诊+密接', 55, 170)
                    .attr({
                        fill: 'orange',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(0+'+'+0, 5, 180)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('已转运总人数<br>确诊+密接', 210, 170)
                    .attr({
                        fill: 'green',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(6+'+'+2, 170, 180)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
            }
        }
    },
    title: {
        text: '<b></b>',
        align: 'left',
        style: {
            color: 'black'
        }
    }
});
