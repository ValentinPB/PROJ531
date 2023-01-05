# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 09:41:14 2023

@author: chafi
"""
import hashlib

with open(r'C:\Users\chafi\OneDrive\Bureau\PROJ531\Utilisateurs\utilisateurs.txt','r') as u :
    content = u.readlines()
u.close()
print(content)
def authentification(Id, password):
    USER = ''
    MDP=''
    j=0
    while Id != USER:
        USER=''
        i=0
        while content[j][i] !=',':
            USER += content[j][i]
            i += 1
        j+=1
        print(USER)
        if USER != Id and j== len(content)-1:
            raise ValueError("ce nom d'utilisateur n'existe pas")
    while content[j-1][i+1] !=',':
            MDP += content[j-1][i+1]
            i += 1
    
    HASH = hashlib.sha256( password.encode('utf-8')).hexdigest()
    
    print(MDP)
    if MDP == HASH:
        return True
    else:
        raise ValueError("Mauvais identifiant / mot de passe.")



def NEW_ACCOUNT(USER, MDP):
    
    with open(r'C:\Users\chafi\OneDrive\Bureau\PROJ531\Utilisateurs\utilisateurs.txt','a') as file :
        HASH= hashlib.sha256( MDP.encode('utf-8')).hexdigest()
        file.write('\n' + USER +',' + HASH +',0;')
        file.close()


