# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 09:41:14 2023

@author: chafi
"""
import hashlib

with open(r'C:\Users\chafi\OneDrive\Bureau\Nouveau dossier (2)\utilisateurs.txt','r') as u :
    content = u.readlines()
u.close()


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
        if USER != Id and j>= len(content)-1:
            return False

    while content[j-1][i+1] !=',':
            MDP += content[j-1][i+1]
            i += 1
    
    HASH = hashlib.sha256( password.encode('utf-8')).hexdigest()
    
    if MDP == HASH:
        return True
    else:
        return False



def NEW_ACCOUNT(USER, MDP):
    
    with open(r'C:\Users\chafi\OneDrive\Bureau\Nouveau dossier (2)\utilisateurs.txt','a') as file :
        HASH= hashlib.sha256( MDP.encode('utf-8')).hexdigest()
        file.write('\n' + USER +',' + HASH +',;')
        file.close()
        
def est_admin(Id, password):
    with open(r'C:\Users\chafi\OneDrive\Bureau\Nouveau dossier (2)\admin.txt','r') as admin_log :
        log = admin_log.readlines()
    admin_log.close()

    USER = ''
    MDP=''
    j=0
    while Id != USER:
        USER=''
        i=0
        while log[j][i] !=',':
            USER += log[j][i]
            i += 1
        j+=1
        if USER != Id and j>= len(log)-1:
            return False

    while log[j-1][i+1] !=',':
            MDP += content[j-1][i+1]
            i += 1
    
    HASH = hashlib.sha256( password.encode('utf-8')).hexdigest()
    
    if MDP == HASH:
        print('Bon')
        return True
    else:
        return False
    

def ajout_score(Id, score,titre_quiz):
    if int(score)<=9:
        file =open(r'C:\Users\chafi\OneDrive\Bureau\Nouveau dossier (2)\utilisateurs.txt','r')
        lignes=file.readlines()
        file.close()
        USER = ''
        MDP=''
        j=0
        while Id != USER:
            USER=''
            i=0
            while lignes[j][i] !=',':
                USER += lignes[j][i]
                i += 1
            j+=1
        while content[j-1][i+1] !=',':
            MDP += content[j-1][i+1]
            i += 1
    
        
        lignes[j-1]= Id +',' + MDP +',' + titre_quiz + ':' + score +';'
        
        file= open(r'C:\Users\chafi\OneDrive\Bureau\Nouveau dossier (2)\utilisateurs.txt','w')
        file.writelines(lignes)
        file.close()
   
        

            





