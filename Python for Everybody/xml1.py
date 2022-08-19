import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type='intl'>
+1 734 303 4456
</phone>
<email hide='yes'/>
</person>'''

tree = ET.fromstring(data) #将以上字符串形式的xml，建立起一个内部的树状数据结构
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
