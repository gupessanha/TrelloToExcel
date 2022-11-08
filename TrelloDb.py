import requests
import json
import numpy as np


class Board:
    def __init__(self, key='fc23aaf60dd87002c17a29e2fc039d19', token='8b87e84eab71efca714b5c58277867922cd63a26087236eb3bc5d8db0e82dd28', main_endpoint='https://api.trello.com/1/', boardData = None, boardID = input(), boardLists = None) -> None:
        self.key = key
        self.token = token
        self.main_endpoint = main_endpoint
        self.boardId = boardID
        self.boardData = boardData
        self.boardLists = boardLists
    
    def get_board(self):
        #Pega url base e acrescenta a parte do link faltante nesse caso "boards"
        url = self.main_endpoint +'boards/'+self.boardId
        params = {'key': self.key, 'token': self.token}
        response = requests.get(url=url, params=params)
        #Salva o jsonObj na variável boardData em forma de dicionário
        self.boardData = response.json()
        return self.boardData

    def get_board_name(self):
        #Verifica se as informações já foram puxadas do Trello
        if self.boardData == None:
            self.get_board()

        boardName = self.boardData['name']
        return(boardName)

    def get_board_id(self):
        #Verifica se as informações já foram puxadas do Trello
        if self.boardData == None:
            self.get_board()

        boardIdLocal = self.boardData['id']
        print(boardIdLocal)

    def get_board_lists(self):
        #Acrescenta palavra ao link '/lists' 
        url = self.main_endpoint +'boards/'+self.boardId+'/lists'
        params = {'key': self.key, 'token': self.token}
        response = requests.get(url=url, params=params)
        self.boardLists = response.json()
        
        return self.boardLists

    def get_board_lists_names(self):
        if self.boardLists == None:
            self.get_board_lists()

        numberOfNames = len(self.boardLists)
        holder = None
        nameList = []  
        for i in range(numberOfNames):
            holder = dict(self.boardLists[i])
            nameList.append(holder['name'])
        print(nameList)
            