import requests

def get_cover_url():
	av_id = input('请输入av号：')
	url = "https://www.bilibili.com/video/av" + av_id
	headers = {'Host': 'www.bilibili.com', 
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
	text = requests.get(url, headers=headers).text
	begin_index = text.find('itemprop=\"image\"') + len('itemprop=\"image\" content=\"')
	end_index = text.find('\"', begin_index)
	cover_url = text[begin_index:end_index]
	print(cover_url)

get_cover()