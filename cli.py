#!/usr/bin/env python

class Token():
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        self.piece = []

    def read_token(self): #Piece 1 6: ->Pieceと右の:を弾く(Pieceのサイズ)
        self.y, self.x = map(int, input()[:-1].split(' ')[1:])
        self.piece = []
        for _ in range(self.y):
            self.piece.append(input())  # pieceを受け取る

#Piece 2 2:
#**
#**
    def get_topleft_edge(self): #Pieceの左上か
        for i in range(self.y):
            for l in range(self.x): #yieldを使うことで都度都度returnしてるのと同じでbuffが必要なくなる
                if self.piece[i][l] == '*': yield i, l  #piece[y][x]が*だった場合はi, lを返す(その座標を返す)
        return None, None

    def get_bottomright_edge(self): #Pieceの右下から
        for i in range(self.y)[::-1]:
            for l in range(self.x)[::-1]:
                if self.piece[i][l] == '*': yield i, l # piece[y][x]が*だった場合はi,lを返す(その座標)
        return None, None

#Piece 2 2: -> return [0][0], [0][1], [1][0], [1][1]
#**
#**

#Piece 2 2: -> return [0][0], [1][0]
#*.
#*.

class Board():
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        self.board = []

    def read_board(self): #Plateau 15 17: ->Pleateauと右の:を弾く
        self.y, self.x = map(int, input()[:-1].split(' ')[1:])  #縦がy、横がx
        _ = input() #inputは使わない(01234567890123456)->mapの座標
        self.board = []
        for _ in range(self.y): #縦幅の数読み込む
            self.board.append(input().split(' ')[1]) #...のマップの部分だけ取る
#000 .................
#001 .................
#002 .................

class Player():

    def __init__(self, p, board, token):
        self.p = p  #player1 or player2
        self.char = 'o' if self.p == "p1" else 'x'  #p1だったらo
        self.enemy_char = 'x' if self.char == 'o' else 'o' #敵は,xまたはo
        self.board = board  #Boardクラス
        self.token = token  #Tokenクラス
        self.best = 100000000 #敵との距離の最適を入れる

    def check_overlap(self, x, y):
        token = self.token
        overlap_counter = 0

        for token_y in range(token.y):
            for token_x in range(token.x):  #pieceの大きさ

                if self.board.board[y + token_y][x + token_x] in (self.enemy_char, self.enemy_char.upper()): #敵の駒があるか
                    return 1

                if token.piece[token_y][token_x] == '*' and \
                    self.board.board[y + token_y][x + token_x] in \
                        (self.char, self.char.upper()): #自分の駒があるか
                            overlap_counter += 1        #一つでも隣接してれば置ける

        if overlap_counter != 1:
            return 1

        return 0

    def check_overflow(self, x, y):
        token = self.token
        board = self.board

        if ((x + token.x) > board.x) or ((y + token.y) > board.y): #mapからはみ出るか
            return 1
        return 0

    def put_token(self, token_y, token_x):  #token_y token_x は*の位置
        board = self.board
        save = []   #pieceを置ける座標
        enemies = [] #敵の位置

        for board_y in range(board.y):
            for board_x in range(board.x):  #mapを上から全部見ていく
                if board.board[board_y][board_x] is (self.enemy_char, self.enemy_char.upper()): #敵の位置を抑える
                    enemies.append(board_y, board_x)
                if board.board[board_y][board_x] in (self.char, self.char.upper()): #その座標に自分の駒がある場合
                    x = board_x - token_x #コマの座標から、*の位置を引く
                    y = board_y - token_y
                    if x < 0 or y < 0:
                        continue
                    if self.check_overflow(x, y) == 0 and self.check_overlap(x, y) == 0:
                        save.append([y,x])
#                        print(f"{y} {x}") # <got(X or O) [y, x] そのpieceの始まりの座標
#                        return True #置けたらtrue

        if len(save) == 0: #saveに要素ない場合
            return False
        ans = self.choose_the_closest_enemy(save, enemies, x, y)
        print(ans)
        return True

    def choose_the_closest_enemy(self, save:list, enemies: list, x, y): #|x_1 - x_2| + |y_1 - y_2|この距離が最短のものを出す
        closest = []
        for enemy_y, enemy_x in enemies:
            for save_y, save_x in save:
                distane = abs(save_x - enemy_x) + abs(save_y - enemy_y)
                if distance < score.best:
                    closest = [save_x, save_y]
        return closest

    def put_random(self):
        for token_y, token_x in self.token.get_topleft_edge():
            if self.put_token(token_y, token_x): return True #置けた場合はtrueを返す
        print("0 0")  #置けなかった
        return False
#Piece 2 2: -> return [0][0], [0][1], [1][0], [1][1] この場合4回put_tokenする
#**
#**

def main():
    _, _, p, _, _ = input().split(' ')  #$$$ exec p1 : [ryaoi_filler]
# resources/filler_vm -p1 ./resources/players/abanlin.filler -p2 carli.filler -f map

    p = Player(p, Board(), Token()) #playerの登録 p1 or p2
    while True:
        p.board.read_board() #都度都度更新されるmapを確認する
        p.token.read_token() #Pieceを受け取る
        check = p.put_random() #座標の頂点から見ていって置けるとこに置く
        if not check: #put_randomがFalseを返したときbreakする
            break

if __name__ == "__main__":
    main()

#置けるとこをlistで保持して,最も敵に近い位置に置くようにする
