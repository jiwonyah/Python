"""
    클래스에 대해 알아보자.
    클래스를 정의함으로써 클래스에 해당하는 여러 객체(인스턴스)를 만들 수 있다.
    --> 클래스만 잘 만들어 놓으면 객체를 마구 싸지를 수 있음.

    *** 클래스 안에 있는 함수는 뭐다? 메소드다~ ***
    
""" 

# class Dog:
#     def __init__(self, name, age, breed): # 무조건 이 메소드로 시작 / 그리고 첫번째 인자는 무조건 self (걍 외우셈)
#         """
#             생성된 클래스의 객체는 self를 참조하게 돼있음.
#             여기서 클래스 객체의 속성값을 설정해줄 수 있음.
#         """ 
#         self.name= name
#         self.age= age # 생성된 객체의 age 속성은 입력된 파라미터 age를 따라갈거임
#         self.breed = breed  
        
    

# 똘복 = Dog()        #똘복은 이제 "개"다. --> 여기서 self와 똘복은 동일 개념 (클래스 dog의 객체임을 의미)
                    # 객체를 생성하는 순간에 __init__ 메소드는 자동 호출임. --> 실행하면 print(self) 출력될거임
                    


#Inheritance--------------------------------------------------------------------

class Player:
    def __init__(self, name, team, xp):
        self.name = name
        self.team = team
        self.xp = xp
    def introduce(self):
        print(f"Hi, I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players=[]
        self.players_dict = []
        
    def add_player(self, name, xp):
        new_player = Player(name.capitalize(), self.team_name ,xp)
        self.players.append(new_player) #오브젝트 상태로 저장       
        
    # code challenge    
    def remove_players(self):
        #여러명을 받아.
        players = list(map(str, input("Enter players' names to remove: ").split()))
        print(players) # 오브젝트 형태
        for existing_player in self.players: #팀의 기존 멤버들 중..
            for to_remove in players: #삭제될 멤버들 중.. --> 입력된(삭제될) 멤버들 capitalize
                to_remove = to_remove.capitalize()
                if to_remove == existing_player.name:
                    self.players.remove(existing_player)
                    print(f"{to_remove} is successfully removed")
        
    def show_players(self):
        for player in self.players:
            player.introduce()
            
    def players_info(self):
        for player in self.players:
            player_info = {'name':player.name, 'xp': player.xp}
            self.players_dict.append(player_info)
        print(self.players_dict)
        
    # code challenge   
    def xp_sum(self):
        sum = 0
        for player in self.players:
            sum += player.xp
        print(f"The total xp of the team {self.team_name} is {sum}")
            
player1 = Player("Jiwon", "Team_Blue", 1500)

# 팀 블루에는 지원, qewr이 있음
blue = Team("Team Blue")
blue.add_player("jIwon", 1500)
blue.add_player("qewr", 2000)
print(blue.players) # 오브젝트 형태 --> [__main__.Player object at~, ...]

# 아직 jiwon 있을 때
blue.show_players()
blue.xp_sum()

# jiwon 제적 당한 후
blue.remove_players()
blue.show_players()
blue.xp_sum()

blue.players_info() # players가 업데이트 됐으므로 얘도 업데이트 반영된 결과 출력

























        