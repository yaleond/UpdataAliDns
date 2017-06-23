

1.配置：
以下三个参数需要自己填写：
Access_Key_ID = "Access_Key_IDAccess_Key_IDAccess_Key_ID"
Access_Key_Secret = "Access_Key_SecretAccess_Key_Secret"
DomainName = "xxxxx.com"
Access_Key_ID、Access_Key_Secret需要到https://ak-console.aliyun.com/?spm=5176.7926440.772176.2.aFFi1b#/accesskey创建/查看自己的secretID\KEY。
DomainName则是自己需要更新的域名

2.执行updatedns.py来动态更新当前IP到阿里云服务上;此更新会一直运行，每次运行都会到当前用户的home目录下查找ip文件，对比此文件中记录的ip跟当前ip是否相同，不同的话会把当前ip更新到阿里中去，成功后再更新此文件中记录值为当前IP;然后sleep 10分钟后继续上一步。
