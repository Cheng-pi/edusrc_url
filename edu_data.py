import requests
from lxml import etree

def title():

    print('+------------------------------------------')
    print('+  \033[36m\t\t\tusrc_url\033[0m')
    print('+  \033[36m使用方法:\t登录edu_data将cookie填入即可   \033[0m')
    print('+  \033[36mPowerBy:\t程皮糖别皮   \033[0m')
    print('+------------------------------------------')

def attack():
    headers={
        'Cookie':''
    }
#登录edudata，将cookie值放入上方单引号内
#edudata    https://wiki.shikangsi.com/

    for i in  range(494,3234):
        url = 'https://wiki.shikangsi.com/post/'+str(i)+'/'
        data=requests.get(url,headers=headers).content.decode('utf-8')
        result=etree.HTML(data)
        result_name=result.xpath('//h1[@class="am-article-title"]/text()')
        name='\n'.join(result_name)
        result_url=result.xpath('//a[@target="_blank"]/text()')[-1]
        edu_data=name + '\t\t' + result_url
        with open('edu_data.txt','a+',encoding='utf-8') as f:
            if '零组知识库-011运维与二进制安全目录' in edu_data:
                edu_data=edu_data.replace('零组知识库-011运维与二进制安全目录','暂无')
                print('正在爬取->'  + '\t' + edu_data)
                f.write(edu_data+'\n')
                f.close()
            else:
                print('正在爬取->'  + '\t' + edu_data)
                f.write(edu_data + '\n')
                f.close()

    print('\033[32m[+++]爬取完成！\033[0m')



if __name__ == '__main__':
    title()
    attack()