from pyecharts import Bar

if __name__ == '__main__':
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    bar.render()  # 生成本地 HTML 文件