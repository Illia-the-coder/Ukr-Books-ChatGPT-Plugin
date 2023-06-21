import pandas as pd
import random as rnd
import json


class DB:
    def __init__(self, grade,type):
        type=  'Ukrainian' if 'ukr' in type.lower() else 'World`s'
        main_DB=json.load(open(f"resource/data_all.json"))[f'_{grade} grade {type}']
        self.data_ = pd.DataFrame(main_DB[f'books'])
        self.pres_data = main_DB['pres']
        self.authors =list(self.data_.columns)

    def list_all(self):
        
        text=''
        for item in self.authors:
            text+=f'<b>📑{item}</b>\n'
            for book in self.data_[item]['books'].keys():
            #     read_all=self.data_[item]['books'][book]['Читати повністю'].split('\n')[1]
                text+=f"--> <i>{book}</i>\n" #{read_all}\n
        return text

    def get_presentation(self):
        data={}
        for author in self.authors:
            PA=self.data_[self.data_[0].str.contains(author.lower())]
            if len(PA): 
                data[f'🔖{author}']={}
                for name,link in zip(PA[1],PA[2]):
                    data[f'🔖{author}'][name] = link
        return data
    def get_books(self, author):
        return list(self.data_[author]['books'].keys())
    
    def get_bio(self, author):
        return dict(self.data_[author][:2])
    
    def get_content(self, author, name):
        return self.data_[author]['books'].get(name)

    def get_rnd(self):
        self.rnd_auth=rnd.choice(self.authors)
        self.rnd_book=rnd.choice(self.get_books(self.rnd_auth))
        BIO =self.get_bio(self.rnd_auth)
        BIO.update({'book':self.get_content(self.rnd_auth,self.rnd_book)})
        return BIO
    
    def get_adding(self,command):
        modes = {'📔Shortly croped':'Shortly', '📗Review':'Review', '🔉Audiobooks':'Audiobook'}
        data={}
        for author in self.authors:
            data_={}
            for book in self.get_books(author):
               for key in self.get_content(author, book):
                   if  modes[command] == key:
                       data_[f"{command[0]}{book}"] = f'<b>{book}</b>\n{self.get_content(author, book)[key]}'
                       break
            if len(data_.keys()):
                data[f'{command[0]}{author}']=data_
        return data
# DF=DB('9 клас World`s')
# for i in DF.authors:
#     print(DF.get_bio(i))   
# # DF=DF[DF[0].str.contains('Свіфт')]