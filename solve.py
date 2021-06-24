
class Solve():
    def choose_the_closest_center(self, save:list):
        ans = []
        for s in save:
            distance = abs(s[0] - self.x//2) + abs(s[1] - self.y//2)
            if self.best < distance:
                ans = [s[0], s[1]]

        print(f"{ans[0]} {ans[1]}") #最も中央に近い位置に置く
        return True

    def choose_the_closest_enemy(self, save:list, enemies:list): #|x_1 - x_2| + |y_1 - y_2|距離が最短のものを出す
        closest = []
        for enemy in enemies:
            for s in save:
                distance = abs(s[0] - enemy[0]) + abs(s[1] - enemy[1])
                if distance < self.best:
                    closest = [s[0], s[1]] #最も敵との位置が近い
                    self.best = distance #bestを更新する
        return closest

    def manhattan(x,y):
        mini = 1000000000
        for j in range(self.y):
            for i in range(self.x):
                if mp[j][i] == enemy:
                    dist = abs(i - x) +　abs(j - y)
                    if dist < mini:
                        mini = dist
        return mini

    def heat_map()
        for y in range(self.y):
            for x in range(self.x):
                if mp[y][x] is empty:
                    mp[y][x] = manhattan(x,y)
