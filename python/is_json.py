#!/usr/bin/env python
#-*-coding:utf-8-*-
import json
import sys
import os
import glob

class Is_json:
    path = os.path.split(os.path.realpath(__file__))[0]


    def is_json(self, json_file):
        try:
            with open(json_file,'r') as f:
                load_dict = json.load(f)
                print(json_file +  ' True')
        except Exception as e:
            print(json_file +  ' ERROR')
            print(e)

    @property
    def json_list(self):
        try:    
            json_name = sys.argv[1]
            json_list = []       
            for json_name in sys.argv[1:]:
                json_list.append(json_name)           
        except:   
            json_list = glob.glob(os.path.join(self.path,'*.json'))
        return json_list

    @classmethod
    def run(cls):
        for json_file in cls().json_list:
            cls().is_json(json_file)

if __name__ == '__main__':
    Is_json.run()

