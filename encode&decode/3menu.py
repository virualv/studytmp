#!/usr/bin/python3
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

current_layer = menu
parent_layers = []

while True:
	for key in current_layer:
		print(key)
	choice = input('-->>').strip()
	if choice in current_layer:
		parent_layers.append(current_layer)
		current_layer = current_layer[choice]
	if choice == 'b':
		current_layer = parent_layers.pop()
	else:
		print('No effect object')


