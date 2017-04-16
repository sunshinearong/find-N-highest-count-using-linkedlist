import csv
import string
import sys
class Node:
    def __init__(self,word):#init variable
        self._word = word
        self._count = 1
        self._next = None
    def word(self):# get word
        return self._word
    def count(self):#get count
        return self._count
    def next(self):#get next
        return self._next
    def set_next(self,next):#set next
        self._next = next
    def incr(self):#add 1
        self._count += 1
    def __str__(self):#print object
        return "{} : {:d}".format(self._word, self._count)
    
class LinkedList:
    def __init__(self):#init _head
        self._head = None
    def is_empty(self):#Linklist is empty
        if self._head == None:
            return True
        else:
            return False
    def head(self):#get head
        return self._head
    def update_count(self, word): #update count
        if self.head() == None:#empty,add word to it
            self._head = Node(word)
            return
        h=self.head()
        while(h):
            if h._word == word:#already exists,add 1
                h.incr()
                return
            else:
                if h.next() == None:#last element,append word to it
                    h._next = Node(word)
                    return
                h=h.next()
    def rm_from_hd(self): #remove first element
        if self._head ==None:#empty,error
            print 'error:An empty list'
        else:
            h=self._head
            self._head = h.next()
            h.set_next(None)
            return h
    def insert_after(self, node1, node2):#insert node2 after node1
        temp= node1.next()
        node1.set_next(node2)
        node2.set_next(temp)
        return node1
    def sort(self):
        
        head_sorted = self.rm_from_hd()#get first element
        h=head_sorted
        while(self._head):
            node2 = self.rm_from_hd()#get first element
            h=head_sorted
            while(h):
                if h.count() <= node2.count():# node2 count bigger than the first element,make node2 head
                    node2._next = h
                    h = node2
                    head_sorted = h
                    break
                else:
                    if h.count()>=node2.count() and h.next() == None:#head_sorted just has one element
                        h = self.insert_after(h,node2)
                        break
                    if h.count()<node2.count() and h.next() == None:#head_sorted just has one element
                        h = self.insert_after(node2,h)
                        break
                        
                    if h.count() > node2.count() and h.next().count() <= node2.count():#insert node2 to head_sorted
                        h = self.insert_after(h,node2)
                        #print head_sorted.next()
                        break
                
                h=h.next()
        self._head = head_sorted#change self._head to sorted head
        return head_sorted
    def get_nth_highest_count(self, n):
        self.sort()#sort linklist
        temp = self._head
        for i in range(n):
            temp = temp.next()
        return temp.count()# nth element
    def print_upto_count(self, n):
        h=self._head
        while(h):
            if h.count() >=n:#print all element bigger than n
                print h
            else:
                break
            h = h.next()
    def __str__(self):
        s = ''
        h=self._head
        while(h):
            s += h.__str__()+'\n'#all element
            h=h._next
        return s
    
filename = raw_input('File: ') #input file
try:
    f=open(filename,'r')
    cf=csv.reader(f)#read file
except Exception,e:
    print "ERROR: Could not open file " + filename
    sys.exit(0)
data=[]#record all titles
for line in cf:
    if line[0][0]=='#':#ignore comment
        continue
    else:
        data.append(line[4])
try:
    N = int(raw_input('N: ')) #input N
except Exception,e:       
    print "ERROR: Could not read N"
assert N>=0
linklist = LinkedList()#create a Linkedlist instance
for d in data:
    words = []#contain words splited
    split_place = []#record place to split
    for i in range(len(d)):
        if d[i] == ' ' or d[i] in string.punctuation:#split character
            split_place.append(i)
    if split_place == []:#null
        continue
    if split_place[0]>0:
        words.append(d[:split_place[0]])#the first word 
    for i in range(len(split_place)-1):
        words.append(d[split_place[i]+1:split_place[i+1]])#the second word to the second last one
    if split_place[len(split_place)-1]+1 < len(d):
        words.append(d[split_place[len(split_place)-1]+1:])#the last word
    words_filtered = []
    for word in words:
        if word == '' or len(word)<=2:#remove whitespace and word whose length smaller than 3
            pass
        else:
            words_filtered.append(word.lower())
    for word in words_filtered:
        linklist.update_count(word)#update linklist
#print linklist
#sort_link = linklist.sort()
# while(sort_link):
#     print sort_link
#     sort_link = sort_link.next()

k = linklist.get_nth_highest_count(N)#get nth highest
linklist.print_upto_count(k)
