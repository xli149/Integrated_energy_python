class Option:
	def pie(data, title):
		"""
		{ value: 9, name: '澎湃新闻' },
		{ value: 9, name: '微信公众号' },
		{ value: 9, name: '新浪新闻' },
		{ value: 9, name: '新浪微博' },
		"""
		option = {
			'title': {
				'text': title,
				'subtext': '',
				'left': 'center'
			},
			'tooltip': {
				'trigger': 'item'
			},
			'legend': {
				'orient': 'vertical',
				'left': 'left',
			},
			'series': [
				{
					'name': '',
					'type': 'pie',
					'radius': '50%',
					'data': data,
					'emphasis': {
						'itemStyle': {
							'shadowBlur': 10,
							'shadowOffsetX': 0,
							'shadowColor': 'rgba(0, 0, 0, 0.5)'
						}
					}
				}
			]
		}
		return option

	def bar(x_list, y_list):
		option = {
			'xAxis': {
				'type': 'category',
				'data': x_list,
				'axisLabel': {
					'interval': 0,
					'rotate': 45,
					'textStyle': {
						'color': "black",
						'fontSize': 10,
						'fontFamily': 'Microsoft YaHei'
					}
				}
			},
			'yAxis': {
				'type': 'value'
			},
			'series': [{
				'data': y_list,
				'type': 'bar',
				'showBackground': 'true',
				'backgroundStyle': {
					'color': 'rgba(180, 180, 180, 0.2)'
				}
			}]
		}
		return option

	def loudou():
		option = """option = {
            title: {
                text: '',
                subtext: '纯属虚构'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c}%"
            },
            toolbox: {
                feature: {
                    dataView: {readOnly: false},
                    restore: {},
                    saveAsImage: {}
                }
            },
            legend: {
                data: ['展现','点击','访问','咨询','订单']
            },

            series: [
                {
                    name:'漏斗图',
                    type:'funnel',
                    left: '10%',
                    top: 60,
                    //x2: 80,
                    bottom: 60,
                    width: '80%',
                    // height: {totalHeight} - y - y2,
                    min: 0,
                    max: 100,
                    minSize: '0%',
                    maxSize: '100%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                        show: true,
                        position: 'inside'
                    },
                    labelLine: {
                        length: 10,
                        lineStyle: {
                            width: 1,
                            type: 'solid'
                        }
                    },
                    itemStyle: {
                        borderColor: '#fff',
                        borderWidth: 1
                    },
                    emphasis: {
                        label: {
                            fontSize: 20
                        }
                    },
                    data: [
                        {value: 60, name: '访问'},
                        {value: 40, name: '咨询'},
                        {value: 20, name: '订单'},
                        {value: 80, name: '点击'},
                        {value: 100, name: '展现'}
                    ]
                }
            ]
        };"""
		return option

	def dashboard(data):
		option = {
			'tooltip': {
				'formatter': '{a} <br/>{b} : {c}%'
			},
			'series': [{
				'name': 'Pressure',
				'type': 'gauge',
				'detail': {
					'formatter': '{value}'
				},
				'data': [{
					'value': data[1],
					'name': data[0],
				}]
			}]
		}
		return option


if __name__ == "__main__":
	print(Option.loudou())
