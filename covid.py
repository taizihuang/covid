import requests,json,datetime,os,time
import pandas as pd
from mako.template import Template


def genHTML(df):

    df_time = df.loc[df['返回信息'] != '`'].copy()
    return_list = []
    for i in df_time.index:
        info = df_time.loc[i,'返回信息'].split(';')
        for l in info:
            l = l.split(' ')
            while '' in l:
                l.remove('')
            loc = pd.to_datetime(l[0],format='%Y/%m/%d')+datetime.timedelta(days=int(l[2][0:-1]))
            if loc > datetime.datetime.now():
                return_list.append('{}: {}（{} 解封）'.format(df_time.loc[i,'楼栋'],l[1],loc.strftime('%m-%d')))
    r = ''
    for ret in return_list:
        r = r+'<p>'+ret+'</p>'

    s = """
    <!DOCTYPE HTML>
    <html>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <link rel="stylesheet" href="covid.css">
        <style>
            /* css 代码  */
        </style>
        <script src="https://cdn.highcharts.com.cn/highcharts/highcharts.js"></script>
        <script src="https://cdn.highcharts.com.cn/highcharts/modules/exporting.js"></script>
        <script src="https://cdn.highcharts.com.cn/highcharts/modules/heatmap.js"></script>
        <script src="https://cdn.highcharts.com.cn/highcharts/modules/oldie.js"></script>
        <script src="https://cdn.highcharts.com.cn/highcharts/modules/tilemap.js"></script>
        <script src="https://code.highcharts.com.cn/highcharts/modules/timeline.js"></script>
        <script src="https://cdn.highcharts.com.cn/highcharts/modules/xrange.js"></script>
    </head>

    <body>
        <title>593弄公告板</title>
        <h2>593弄公告板</h2>
        <p class="notice"><span style="color:red">{} 更新</span></p>
        {}
        <div id="container0"></div>
        <script src="dimension.js"></script>
        <div id="container"></div>
        <script src="covid.js"></script>
        <div id="container1"></div>
        <script src="timeline.js"></script>
        <div id="container2"></div>
        <script src="groupbuy.js"></script>
        <img style="display: block;margin: auto;width:100px;height:120px;padding-top:20px" src="qr.jpg">
    </body>

    </html>
    """.format(datetime.datetime.now().strftime('%m/%d %H:%M'),r)
    with open('index.html','w',encoding='utf8') as f:
        f.write(s)
def fetchData(tab='BB08J2',start=0,n=20):
    url = 'https://docs.qq.com/dop-api/get/sheet?padId=300000000%24LSEySnuVxEtM&subId={}&startrow={}&endrow={}&outformat=1&rev=1000'.format(tab,start,start+20)
    headers = {
        'Referer': 'https://docs.qq.com/sheet/DTFNFeVNudVZ4RXRN?tab=BB08J2',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    l = requests.get(url,headers=headers).content
    l = json.loads(l)
    data = l['data']['initialAttributedText']['text'][0][-1][0]['c'][1]
    col = int(len(data)/(n+1))
    flag = data[str(col-1)]['0']
    data_list = []
    for i in range(n+1):
        row_list = []
        for j in range(col):
            loc = str(i*col+j)
            if data[loc]['0'] != flag:
                row_list.append(data[loc]['2'][1])
            else:
                row_list.append('`')
        data_list.append(row_list)
    return data_list
def fetchSheet1(n=7):
    data_list = []
    for i in range(n):
        data_list = data_list + fetchData(start=i*20)
    df = pd.DataFrame(columns=data_list[0],data=data_list[1:])
    #df['确诊日期'] = pd.to_datetime(df['确诊日期']-365*70-18, utc=True, unit='d')
    df = df.drop_duplicates(subset='楼栋').reset_index(drop=True)
    return df
def fetchSheet2(tab='m7ohzm',start=0):
    url = 'https://docs.qq.com/dop-api/get/sheet?padId=300000000%24LSEySnuVxEtM&subId={}&startrow={}&endrow={}&outformat=1&rev=1000'.format(tab,start,start+40)
    headers = {
        'Referer': 'https://docs.qq.com/sheet/DTFNFeVNudVZ4RXRN?tab=BB08J2',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    l = requests.get(url,headers=headers).content
    l = json.loads(l)
    data = l['data']['initialAttributedText']['text'][0][-1][0]['c'][1]
    col = 0
    n = 0
    while data[str(col)]['2'][1] != 'NA' and col < 20:
        col = col + 1
    data_list = []

    row_i = [list(data.keys())[0]]
    for i in data.keys():
        if int(i)-int(row_i[-1])>col:
            row_i.append(i)
    for i in row_i[:-1]:
        row_list = []
        for j in range(col+1):
            loc = str(int(i)+j)
            s = '`'
            if loc in data.keys():
                if '2' in data[loc].keys():
                    s = data[loc]['2'][1]
            row_list.append(s)
        data_list.append(row_list)
    df = pd.DataFrame(columns=data_list[0],data=data_list[1:])
    df = df.loc[(df['团长'] !='`') & (df['团长'] !='') & (~df['到货日期'].str.contains('无',na=False)) & (df['到货日期'] !='`')]
    df['团购日期'] = pd.to_datetime(df['团购日期']-365*70-18, unit='d')
    df['到货日期'] = pd.to_datetime(df['到货日期']-365*70-18, unit='d')
    return df
def genDimension(df):
    dimension = Template("""
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
                ren.label(${num1}, 30, 50)
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
                ren.label(${num2}, 200, 50)
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
                ren.label(${num3}+'+'+${num4}, 5, 180)
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
                ren.label(${num5}+'+'+${num6}, 170, 180)
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
""")
    df_time = df.loc[df['返回信息'] != '`'].copy()
    num1 = 0
    for i in df_time.index:
        info = df_time.loc[i,'返回信息'].split(';')
        for l in info:
            l = l.split(' ')
            while '' in l:
                l.remove('')
            loc = pd.to_datetime(l[0],format='%Y/%m/%d')+datetime.timedelta(days=int(l[2][0:-1]))
            if loc > datetime.datetime.now():
                num1 = num1 + int(l[1][0:-1])

    num2 = df['目前确诊人数'].replace('`',0).replace('NA').sum()
    num3 = df['确诊待转运'].replace('`',0).replace('NA').sum()
    num4 = df['密接待转运人数'].replace('`',0).replace('NA').sum()
    num5 = df['确诊已转运人数'].replace('`',0).replace('NA').sum()
    num6 = df['密接已转运'].replace('`',0).replace('NA').sum()
    with open('dimension.js','w',encoding='utf8') as f:
        f.write(dimension.render(num1=str(num1),num2=str(num2),num3=str(num3),num4=str(num4),num5=str(num5),num6=str(num6)))
def genCovid(df): 
    covid = Template("""
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
                value: ${value[12]},
                'desc': "${desc[12]}"
            }, {
                'hc-a2': '11',
                name: '11',
                region: 'West',
                x: 1,
                y: 2,
                value: ${value[11]},
                'desc': "${desc[11]}"
            }, {
                'hc-a2': '10',
                name: '10',
                region: 'West',
                x: 1,
                y: 3,
                value: ${value[10]},
                'desc': "${desc[10]}"
            }, {
                'hc-a2': '9',
                name: '9',
                region: 'West',
                x: 1,
                y: 4,
                value: ${value[9]},
                'desc': "${desc[9]}"
            }, {
                'hc-a2': '8',
                name: '8',
                region: 'West',
                x: 2,
                y: 1,
                value: ${value[8]},
                'desc': "${desc[8]}"
            }, {
                'hc-a2': '7',
                name: '7',
                region: 'West',
                x: 2,
                y: 2,
                value: ${value[7]},
                'desc': "${desc[7]}"
            }, {
                'hc-a2': '6',
                name: '6',
                region: 'West',
                x: 2,
                y: 3,
                value: ${value[6]},
                'desc': "${desc[6]}"
            }, {
                'hc-a2': '5',
                name: '5',
                region: 'West',
                x: 3,
                y: 1,
                value: ${value[5]},
                'desc': "${desc[5]}"
            }, {
                'hc-a2': '4',
                name: '4',
                region: 'West',
                x: 3,
                y: 2,
                value: ${value[4]},
                'desc': "${desc[4]}"
            }, {
                'hc-a2': '3',
                name: '3',
                region: 'West',
                x: 3,
                y: 3,
                value: ${value[3]},
                'desc': "${desc[3]}"
            }, {
                'hc-a2': '2',
                name: '2',
                region: 'West',
                x: 3,
                y: 4,
                value: ${value[2]},
                'desc': "${desc[2]}"
            }]
        }]
    });
    """)
    value_dict = {}
    desc_dict = {}
    for i in range(13):
        value_dict[str(i)] = 0
        desc_dict[str(i)] = ' '
    for i in df.loc[(df['目前确诊人数'] != '`')&(df['目前确诊人数'] != 0)].index:
        loc = df.loc[i,'楼栋'].split('-')
        value_dict[loc[0]] = value_dict[loc[0]] + df.loc[i,'目前确诊人数']
        desc_dict[loc[0]] = desc_dict[loc[0]] + '<br>'+loc[1]+'（{}人，已转运{}人）；'.format(df.loc[i,'目前确诊人数'],df.loc[i,'确诊已转运人数'])
    with open('covid.js','w',encoding='utf8') as f:
        f.write(covid.render(value=list(value_dict.values()),desc=list(desc_dict.values())))
def genTimeline(df):
    timeline = Template("""
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
                %for x,name,label,color in time_li:
                {
                x: Date.UTC(2022, ${x[0]}, ${x[1]}),
                name: "${name}",
                label: "${label}",
                description: "",
                color: "${color}",
            },
            %endfor
            {
                x: Date.UTC(2022, ${t_max[0]}, ${t_max[1]}),
                name: ' ',
                label: ' ',
                description: "",
                color: 'black',
            }]
        }]
    }, function(c) {
        // 动态改变 x 轴范围即可实现拖动
        c.xAxis[0].setExtremes(Date.UTC(2022, ${t_min[0]}, ${t_min[1]}), Date.UTC(2022, ${t_max[0]}, ${t_max[1]-1}));
    });
    """)
    df_time = df.loc[df['确诊信息'] != '`'].copy()
    #df_time['确诊日期'] = pd.to_datetime(df_time['确诊日期']-365*70-18, utc=True, unit='d')
    with open('test.json','r',encoding='utf8') as f:
        t = json.loads(f.read())
    for i in df_time.index:
        # loc = df_time.loc[i,'确诊日期'].strftime('%m/%d')
        info = df_time.loc[i,'确诊信息'].split(';')
        for l in info:
            l = l.split(' ')
            while '' in l:
                l.remove('')
            loc = l[0].replace('2022/','0')
            if loc in t.keys():
                t[loc] = t[loc]+';<br>{}确诊{}'.format(df_time.loc[i,'楼栋'],l[1])
            else:
                t[loc] = '{}确诊{}'.format(df_time.loc[i,'楼栋'],l[1])
    time_li = []
    for i in t.keys():
        x = [int(i.split('/')[0])-1,int(i.split('/')[1])]
        name = t[i]
        label = t[i]
        if '确诊' in name:
            color = 'red'
        else:
            color = 'black'
        time_li.append((x,name,label,color))
    t_max = datetime.datetime.today()
    t_min = t_max+datetime.timedelta(days=-5)
    t_min = [t_min.month-1,t_min.day]
    t_max = [t_max.month-1,t_max.day+1]
    with open('timeline.js','w',encoding='utf8') as f:
        f.write(timeline.render(time_li=time_li,t_min=t_min,t_max=t_max))
def genGroupbuy(df):
    groupBuy = Template("""
    Highcharts.chart('container2', {
        chart: {
            type: 'xrange',
            panning: true,
            pinchType: 'x',
            height: ${height}
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
            categories: ${category},
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
                %for x,x2,y,color,leader,fill in groupBuy_li:
                {
                x: Date.UTC(2022, ${x[0]}, ${x[1]}),
                x2: Date.UTC(2022, ${x2[0]}, ${x2[1]}),
                y: ${y},
                color: '${color}',
                'leader': '${leader}',
                partialFill: ${fill}
            },
            %endfor
            ],
            dataLabels: {
                enabled: true,
                format: '<span>团长：{point.leader}</span>'
            }
        }]
    }, function(c) {
        // 动态改变 x 轴范围即可实现拖动
        c.xAxis[0].setExtremes(Date.UTC(2022, ${t_min[0]}, ${t_min[1]}), Date.UTC(2022, ${t_max[0]}, ${t_max[1]}));
    });
    """)
    color_list = ['#f1ccb8','#f1f1b8','#b8f1ed','#b8f1cc','#e7dac9']
    groupBuy_li = []
    category = []
    y = 0
    for i in df.index:
        leader = df.loc[i,'团长']
        color = color_list[y % len(color_list)]
        x = [df.loc[i,'团购日期'].month-1,df.loc[i,'团购日期'].day]
        x2 = [df.loc[i,'到货日期'].month-1,df.loc[i,'到货日期'].day]
        t = datetime.datetime(2022,datetime.datetime.today().month,datetime.datetime.today().day)
        if df.loc[i,'到货日期']>=t:
            fill = round((t-df.loc[i,'团购日期']).days/(df.loc[i,'到货日期']-df.loc[i,'团购日期']).days,2)
            groupBuy_li.append((x,x2,y,color,leader,fill))
            category.append(df.loc[i,'团品'])
            y = y + 1
    t_max = max(df['到货日期'])
    t_min = t_max+datetime.timedelta(days=-10)
    t_min = [t_min.month-1,t_min.day]
    t_max = [t_max.month-1,t_max.day+1]
    with open('groupbuy.js','w',encoding='utf8') as f:
            f.write(groupBuy.render(groupBuy_li=groupBuy_li,category=category,t_min=t_min,t_max=t_max,height=70*len(category)))

os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()
df1 = fetchSheet1()
df2 = fetchSheet2()
genCovid(df1)
genDimension(df1)
genTimeline(df1)
genGroupbuy(df2)
genHTML(df1)
