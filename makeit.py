####################################
#
# usage: makeit.py
# Copyright@mz1
#
##################################

#导入库
import os
import re
# from bs4 import BeautifulSoup   # 并不想用，太麻烦了

# 相关配置
MAIN_PAGE = "./index.html.bak"
MAIN_PAGE_OUTPUT = "./index.html"
CONTENT_PATH = "./contents/"         # 博客html内容目录
RAW_PATH = "./raw/"                  # 博文原始内容目录


# 读取raw文件生成html
def generate_html():
	print('> start to generate html！')
	tmp = os.listdir(RAW_PATH)
	page_list = []
	for i in tmp:
		if not os.path.isdir(i):
			page_list.append(i)
	for i in page_list:
		with open(RAW_PATH+i, 'r', encoding='utf-8') as f:
			fcontent = f.read()
		fcontent = fcontent.replace('\n', '<br>')
		with open(CONTENT_PATH+i[:-4]+'.html', 'w', encoding='utf-8') as f:
			f.write(fcontent)




# 读取当前html，定位相应信息, 插入链接
def generate_link():
	# 搜索文档
	print('> start to generate links~')
	tmp = os.listdir(CONTENT_PATH)
	page_list = []
	for i in tmp:
		if not os.path.isdir(i):
			page_list.append(i)
			
	START = '<div id="links">'
	END = '</div>'
	str_link = START
	for i in page_list:
		str_link += '<a href="{}{}">{}</a>'.format(CONTENT_PATH, i, i[:-5])
		str_link += '<br>'
	str_link += END
	# print(str_link)
	with open(MAIN_PAGE, 'r', encoding='utf-8') as f:
		main_page = f.read()

	index = main_page.index('<div id="links">')
	p1 = main_page[:index]
	p2 = main_page[index+len(START+END):]
	fine = p1 + str_link + p2

	with open(MAIN_PAGE_OUTPUT, 'w', encoding='utf-8') as f:
		f.write(fine)
		
	print('> ok! Generate main page {} successfully~'.format(MAIN_PAGE_OUTPUT))


# 验证
def verify():
	with open(MAIN_PAGE_OUTPUT, 'r', encoding='utf-8') as f:
		main_page = f.read()
		
	print('> now: ')
	links = re.findall('<div id="links">(.*?)</div>', main_page)[0]
	links = links.split('<br>')
	for i in links:
		print("    "+i)
	
if __name__ == "__main__":
	print("> start to make it")	
	generate_html()
	generate_link()
	verify()


