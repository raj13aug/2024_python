class Tag():
    
    def __init__(self):
        self.tags = {}
        
    def log(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
        
cloud = Tag()
cloud.log("python")
cloud.log("python")

print(cloud.tags)