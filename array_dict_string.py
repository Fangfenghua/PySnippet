# �����б�
sample_list = ['a',1,('a','b')]

# Python �б����
sample_list = ['a','b',0,1,3]

# �õ��б��е�ĳһ��ֵ
value_start = sample_list[0]
end_value = sample_list[-1]

# ɾ���б�ĵ�һ��ֵ
del sample_list[0]

# ���б��в���һ��ֵ
sample_list[0:0] = ['sample value']

# �õ��б�ĳ���
list_length = len(sample_list)

# �б����
for element in sample_list:
    print 'element' 
    
#Python �б�߼�����/����

#����һ����ֵ�����б�
num_inc_list = range(30)
#will return a list [0,1,2,...,29]

# ��ĳ���̶�ֵ��ʼ���б�
initial_value = 0
list_length = 5
sample_list = [ initial_value for i in range(10)]
sample_list = [initial_value]*list_length
# sample_list ==[0,0,0,0,0]


# ����python��������
#1��list���б�����̬���飬C++��׼���vector�����ɺ���ͬ���͵�Ԫ����һ��list�У�
a = ["I","you","he","she"]      ��Ԫ�ؿ�Ϊ�κ����͡�

#�±꣺���±��д���͵������鴦��
#��0��ʼ���и��±��ʹ��
#0��һ��Ԫ�أ�-1���һ��Ԫ�أ�
#-len��һ��Ԫ�أ�len-1���һ��Ԫ��
#ȡlist��Ԫ������
len(list)   #list�ĳ��ȡ�ʵ�ʸ÷����ǵ����˴˶����__len__(self)������ 

#����������list
L = range(1,5)      #�� L=[1,2,3,4],�������һ��Ԫ��
L = range(1, 10, 2) #�� L=[1, 3, 5, 7, 9]

#list�ķ���
L.append(var)   #׷��Ԫ��
L.insert(index,var)
L.pop(var)      #�������һ��Ԫ�أ�����list��ɾ��֮
L.remove(var)   #ɾ����һ�γ��ֵĸ�Ԫ��
L.count(var)    #��Ԫ�����б��г��ֵĸ���
L.index(var)    #��Ԫ�ص�λ��,�������쳣 
L.extend(list)  #׷��list�����ϲ�list��L��
L.sort()        #����
L.reverse()     #����
#list ������:,+,*���ؼ���del
a[1:]       #Ƭ�β�������������list����ȡ
[1,2]+[3,4] #Ϊ[1,2,3,4]��ͬextend()
[2]*4       #Ϊ[2,2,2,2]
del L[1]    #ɾ��ָ���±��Ԫ��
del L[1:3]  #ɾ��ָ���±귶Χ��Ԫ��
list�ĸ���
L1 = L      #L1ΪL�ı�������C��˵����ָ���ַ��ͬ����L1��������L�������������������������ݵ�
L1 = L[:]   #L1ΪL�Ŀ�¡������һ��������
        
list comprehension
   [ <expr1> for k in L if <expr2> ]
                
2��dictionary�� �ֵ䣨��C++��׼���map��
dict = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}
ÿһ��Ԫ����pair������key��value�����֡�key��Integer��string���ͣ�value ���������͡�
����Ψһ�ģ��ֵ�ֻ�����һ�����ļ�ֵ��

dictionary�ķ���
D.get(key, 0)       #ͬdict[key]�����˸�û���򷵻�ȱʡֵ��0��[]û�������쳣
D.has_key(key)      #�иü�����TRUE������FALSE
D.keys()            #�����ֵ�����б�
D.values()          #���б����ʽ�����ֵ��е�ֵ������ֵ���б��пɰ����ظ�Ԫ��
D.items()           #�����е��ֵ������б�ʽ���أ���Щ�б��е�ÿһ�������(��,ֵ),�������ڷ���ʱ��û�������˳��         

D.update(dict2)     #���Ӻϲ��ֵ�
D.popitem()         #�õ�һ��pair�������ֵ���ɾ�������ѿ������쳣
D.clear()           #����ֵ䣬ͬdel dict
D.copy()            #�����ֵ�
D.cmp(dict1,dict2)  #�Ƚ��ֵ䣬(���ȼ�ΪԪ�ظ���������С����ֵ��С)
                    #��һ���󷵻�1��С����-1��һ������0
            
dictionary�ĸ���
dict1 = dict        #����
dict2=dict.copy()   #��¡������һ��������

3��tuple��Ԫ�飨���������飩
tuple = ('a', 'b', 'c', 'd', 'e')
������list�� [],:��������ȡԪ�ء����ǲ���ֱ���޸�Ԫ�ء�

4��string��     �ַ������������޸ĵ��ַ�list��
str = "Hello My friend"
�ַ�����һ�����塣�������ֱ���޸��ַ�����ĳһ���֣��ǲ����ܵġ��������ܹ������ַ�����ĳһ���֡�
���ַ�������ȡ
str[:6]
�ַ��������жϲ�������in��not in
"He" in str
"she" not in str

stringģ�飬���ṩ�˺ܶ෽������
S.find(substring, [start [,end]]) #��ָ��Χ�����Ӵ�����������ֵ�����򷵻�-1
S.rfind(substring,[start [,end]]) #�������
S.index(substring,[start [,end]]) #ͬfind��ֻ���Ҳ�������ValueError�쳣
S.rindex(substring,[start [,end]])#ͬ�Ϸ������
S.count(substring,[start [,end]]) #�����ҵ��Ӵ��ĸ���

S.lowercase()
S.capitalize()      #����ĸ��д
S.lower()           #תСд
S.upper()           #ת��д
S.swapcase()        #��Сд����

S.split(str, ' ')   #��stringתlist���Կո��з�
S.join(list, ' ')   #��listתstring���Կո�����

�����ַ��������ú���
len(str)                #������
cmp("my friend", str)   #�ַ����Ƚϡ���һ���󣬷���1
max('abcxyz')           #Ѱ���ַ����������ַ�
min('abcxyz')           #Ѱ���ַ�������С���ַ�

string��ת��
            
float(str) #��ɸ�������float("1e-1")  ���Ϊ0.1
int(str)        #������ͣ�  int("12")  ���Ϊ12
int(str,base)   #���base������������int("11",2) ���Ϊ2
long(str)       #��ɳ����ͣ�
long(str,base)  #���base���Ƴ����ͣ�

�ַ����ĸ�ʽ����ע����ת���ַ��������C���Եģ��ԣ�
str_format % (�����б�) �t#�����б�����tuple����ʽ����ģ������������иı�
>>>print ""%s's height is %dcm" % ("My brother", 180)
          #�����ʾΪ My brother's height is 180cm

������������������������������������

list �� tuple ���໥ת��

tuple(ls) 
list(ls)
