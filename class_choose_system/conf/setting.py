# Author : virualv
# Time : 10/22/2018 6:48 PM

School = {
    'sh':{
        'name':'joyschool_shanghai',
        'address':'shanghai pudong',
        'city':'Shanghai'
    },
    'bj':{
        'name':'joyschool_beijing',
        'address':'beijing wudaokou',
        'city':'Beijing'
    }
}

Course = {
    'linux':{
        'school':School['bj'],
        'name':'linux',
        'price':14000,
        'outline':'120 days'
    },
    'python':{
        'school':School['bj'],
        'name':'python',
        'price':17000,
        'outline':'180 days'
    },
    'go':{
        'school':School['sh'],
        'name':'go',
        'price':20000,
        'outline':'150 days'
    }
}

Class = {
    'semester':2,    
}