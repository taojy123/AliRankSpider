
import urllib2
import time
import re
import traceback
import json
import xlwt
import random

def input_search(input_file_name, output_file_name, frame=None, max_page=10, random_time="1-3"):

    workBook = xlwt.Workbook()
    workBook.add_sheet("rank")
    sheet = workBook.get_sheet(0)

    lines = open(input_file_name).readlines()
    row = 0
    for line in lines:
        if frame:
            frame.gauge1.SetRange(len(lines))
            frame.gauge1.SetValue(row+1)

        target, keyword, oid = line.strip().split("----")
        print target, keyword, oid
        url = "http://www.alibaba.com/products/F0/%s/1.html" % keyword
        p = urllib2.urlopen(url).read()
        
        nums = re.findall(r"\|n=(\w+?)\|s=p\|t={{attr target}}'\"><span", p)
        nums = [int(num) for num in nums]
        ad_rank = max(nums)

        rank = u'\u65e0\u6392\u540d'
        for i in range(1, max_page):
            url = "http://www.alibaba.com/products/F0/%s/%d.html" % (keyword, i)
            print url
            if i > 1:
                p = urllib2.urlopen(url).read()
            if '<span class="active">' not in p:
                if '<span class="current">' not in p:
                    print "Exceed"
                    break
            index = p.find(target)
            if index > -1:
                p = p[index:]
                pid = re.findall(r",pid:(.*?),", p)[0]
                n = re.findall(r"'\|n=(\w+?)'", p)[0]
                rank = "%s#%s" % (i, n)
                break

        print rank
        sheet.write(row, 0, row+1)
        sheet.write(row, 1, target)
        sheet.write(row, 2, keyword)
        sheet.write(row, 5, oid)
        if rank != u'\u65e0\u6392\u540d':
            sheet.write(row, 3, rank)
            sheet.write(row, 4, pid)
            if pid == oid:
                sheet.write(row, 6, "")
            else:
                sheet.write(row, 6, u'\u4e0d\u5339\u914d')
        else:
            sheet.write(row, 3, u'\u65e0\u6392\u540d')        
        row += 1
        t1, t2 = random_time.strip().split("-")
        t = random.randint(int(t1), int(t2))
        print "sleep", t, "s"
        time.sleep(t)

    workBook.save(output_file_name)

    print "ok"

    return True


if __name__ == "__main__":
    input_search("input.txt", "output.xls")



