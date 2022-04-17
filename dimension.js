
var chart = Highcharts.chart('container0', {
    chart: {
        backgroundColor: 'white',
        events: {
            load: function() {
                // Draw the flow chart
                var ren = this.renderer,
                    colors = Highcharts.getOptions().colors;
                // 横线
                ren.path(['M', 0, 150, 'L', 380, 150])
                    .attr({
                        'stroke-width': 2,
                        stroke: 'silver',
                        dashstyle: 'dash'
                    }).add();
                // 竖线
                ren.path(['M', 180, 50, 'L', 180, 250])
                    .attr({
                        'stroke-width': 2,
                        stroke: 'silver',
                        dashstyle: 'dash'
                    }).add();
                // Headers
                ren.label('待复核核酸总人数<br/>', 40, 50)
                    .attr({
                        fill: 'blue',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(0, 40, 50)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('已确诊总人数', 220, 50)
                    .attr({
                        fill: 'red',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(5, 210, 50)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('待转运人数（确诊+密接）', 20, 170)
                    .attr({
                        fill: 'orange',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(0+'+'+12, 5, 170)
                    .attr({
                        padding: 40,
                    })
                    .css({
                        fontWeight: 'bold',
                        fontSize: 40,
                    }).add();
                ren.label('已转运总人数（确诊+密接）', 190, 170)
                    .attr({
                        fill: 'green',
                        stroke: 'white',
                        'stroke-width': 2,
                        padding: 5,
                        r: 5
                    }).css({
                        color: 'white'
                    }).add().shadow(true);
                ren.label(5+'+'+2, 180, 170)
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
