menu = {
	'anhui':{
		'luan':{
			'shouxian':{
				'zhongxing',
				'yankou',
				'anfeng',
				'baoyi'
				},
			'jinanqu':{
				'zhangdian',
				'maotanchang',
				'muchan'	
				}
			},
		'hefei':{
			'gaoxin':{
				'iflytek',
				'autoserver',
				'xiaomi'
				},
			'jingkai':{
				'lenovo',
				'jd',
				'huawei'
				},
			'baohe':{
				'ustc',
				'hegongda'
				}
			},
		},
	'hubei':{
		'wuhan':{
			'qingshan':{
				'bobei',
				'haile',
				'jingqi'
				},
			'dongxihu':{
				'wufang',
				'lianjia',
				'deepin'
				},
			'wuchang':{
				'wuda',
				'huazhongkejida'
				}
			},
		'huanggang':{
			'huanggangzx':'gaocaisheng'
			}
		},
	'jiangsu':{
		'nanjing':{
			'jingan':'shen'
			}
		}
}
f = open('menu1','r+')
f.write(str(menu))



current_layer = menu
parent_layers = []

while True:
	for key in current_layer:
		print(key)
		# add_y_or_no = ('Would you want to add?[y/n]')
		# if	add_y_or_no == 'y'：


	choice = input('-->>').strip()
	if choice in current_layer:
		parent_layers.append(current_layer)
		current_layer = current_layer[choice]
	elif choice == 'b':
		current_layer = parent_layers.pop()
	else:
		print('No effect object\n')
