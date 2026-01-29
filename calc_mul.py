#!/usr/bin/python3

import re
                
def calc(A,B):
        # A, B は「整数」だけを許可（boolも弾くため type を使う）
        if type(A) is not int or type(B) is not int:
                return -1

        # 範囲チェック：1〜999のみ有効
        if not (1 <= A <= 999) or not (1 <= B <= 999):
                return -1

        # 有効なら積を返す
        return A * B
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()

