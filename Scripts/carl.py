import requests
 
### Brought to you by https://twitter.com/LNKRdev
# Flappy Carl Python Game Solver
# Don't forget to change cookie
 
class FuckinFlappy():
    # change this
    cookies = {'bitlagoon': ''}
 
    # don't change this

    target_score = 103
    url = 'https://www.mrriddle.com/carl/api/do-event'
    data={
        "velocity": 0,
        "gravity":0,
        "jump": 0,
        "event": "none",
        "position": 0,
        "rotation": 0,
        "score":0,
        "pipeheight": 0
    }
 
 
    def start(self):
        self.data["event"] = "start"
        r = requests.post(self.url, cookies=self.cookies, data=self.data)
 
    def jump(self):
        self.data["event"] = "jump"
        self.data["position"] += 150
        r = requests.post(self.url, cookies=self.cookies, data=self.data)
 
    def score(self):
        self.data["event"] = "score"
        self.data["score"] += 1
        r = requests.post(self.url, cookies=self.cookies, data=self.data)
        print(r.content)
 
    def dead(self):
        self.data["event"] = "dead"
        r = requests.post(self.url, cookies=self.cookies, data=self.data)
 
    def run(self):
        self.start()
        while self.data["score"] < self.target_score:
            self.jump()
            self.score()
        self.dead()
        print("Done")
 
ff = FuckinFlappy()
ff.run()
