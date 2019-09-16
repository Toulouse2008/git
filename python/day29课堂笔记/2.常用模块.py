# configparse
# import configparser
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w') as f:
#    config.write(f)


# import configparser
#
# config = configparser.ConfigParser()
# #---------------------------查找文件内容,基于字典的形式
# # print(config.sections())        #  []
#
# config.read('example.ini')
# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True

# print(config['bitbucket.org']["user"])  # hg
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
#
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
#
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
#
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
#
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
#
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value

# import configparser
# config = configparser.ConfigParser()
# config.read('example.ini')   # 读文件
# config.add_section('yuan')   # 增加section
# config.remove_section('bitbucket.org')   # 删除一个section
# config.remove_option('topsecret.server.com',"forwardx11")  # 删除一个配置项
# config.set('topsecret.server.com','k1','11111')
# config.set('yuan','k2','22222')
# f = open('new2.ini', "w")
# config.write(f) # 写进文件
# f.close()