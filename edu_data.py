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
        result=etree.HTML(data)                 #返回的页面html
        result_name=result.xpath('//h1[@class="am-article-title"]/text()')      #处理学校名
        name='\n'.join(result_name)
        result_url=result.xpath('//a[@target="_blank"]/text()')[-1]     #处理学校域名
        start_ip=result.xpath('/html/body/div[1]/div/div/article/div[2]/p[9]/text()')       #获取开始IP
        start_ip=(','.join(str(x) for x in start_ip))               #去掉[]
        stop_ip=result.xpath('/html/body/div[1]/div/div/article/div[2]/p[10]/text()')       #获取结束IP
        stop_ip = (','.join(str(y) for y in stop_ip))               #去掉[]
        edu_data=name + '\t\t\t\t' + result_url

        with open('edu_data.txt','a+',encoding='utf-8') as f:
            if '零组知识库-011运维与二进制安全目录' in edu_data:
                edu_data=edu_data.replace('零组知识库-011运维与二进制安全目录','暂无')
                print('正在爬取->'  + '\t\t' + edu_data)
                f.write(edu_data+'\t\t\t\t'+start_ip+'-'+stop_ip+'\n')
                f.close()
            else:
                print('正在爬取->'  + '\t\t\t' + edu_data)
                f.write(edu_data+'\t\t\t\t'+start_ip+'-'+stop_ip + '\n')
                f.close()

    print('\033[32m[+++]爬取完成！\033[0m')



if __name__ == '__main__':
    title()
    attack()
